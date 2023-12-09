"""
Voice Transcription Script

This script provides functions for recording audio from a microphone, loading the audio data,
and transcribing the speech using a pre-trained Whisper ASR (Automatic Speech Recognition) model.
"""
import os
import pyaudio
import whisper
from scipy.io.wavfile import read
import numpy as np
import wave

def recordingVoice(save_path="data/output.wav"):
    """
    Records audio from the microphone for a specified duration and saves it to a WAV file.

    Args:
    save_path (str): The path to save the recorded audio file.

    Returns:
    bytes: The recorded audio data as bytes.
    """
    # Create the "data" folder if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10

    # Initialize pyaudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print("Recording...")

    frames = []

    # Record for 10 seconds
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(save_path, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

    return b"".join(frames)  # Return the audio data as bytes



def load_audio(audio_data):
    """
    Converts audio data from bytes to a NumPy array.

    Args:
    audio_data (bytes): The audio data in bytes.

    Returns:
    numpy.ndarray: The audio data as a NumPy array.
    """
    return np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32767.0


def transcribe_audio(audio_data):
    """
    Transcribes audio data using a pre-trained Whisper ASR model.

    Args:
    audio_data (bytes): The audio data to transcribe.

    Returns:
    str: The transcribed text.
    """
    # Load the model
    model = whisper.load_model("base")

    # Load the audio using the new function
    audio = load_audio(audio_data)

    # Run the transcription process
    result = model.transcribe(audio)

    return result["text"]
