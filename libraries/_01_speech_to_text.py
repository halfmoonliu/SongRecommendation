"""
Voice Transcription Script

This script provides functions for recording audio from a microphone, loading the audio data,
and transcribing the speech using a pre-trained Whisper ASR (Automatic Speech Recognition) model.
"""
# _01_speech_to_text.py

import sounddevice as sd
import numpy as np
import wave
import azure.cognitiveservices.speech as speechsdk
import whisper
import os
from config import AZURE_SPEECH_SUBSCRIPTION_KEYENV, AZURE_SPEECH_REGIONENV

def recordingVoice(save_path="data/output.wav"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    duration = 10  # Set the duration of recording in seconds

    # Create a speech configuration object using Azure Speech SDK credentials
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SPEECH_SUBSCRIPTION_KEYENV,
        region=AZURE_SPEECH_REGIONENV
    )

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Create a speech recognizer with Azure Speech SDK
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Start speech recognition
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        audio_data = np.frombuffer(result.audio_data, dtype=np.int16)
        # Save the recorded audio to a WAV file
        with wave.open(save_path, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(44100)
            wf.writeframes(audio_data.tobytes())

        return audio_data.tobytes()

    else:
        print("Speech recognition failed:", result.reason)
        return b""


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

