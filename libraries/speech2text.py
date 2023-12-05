# this code is to use whisper api to transcribe speech to text
# the frist step is to create a 10s voice record
# the second step is to use whisper api to transcribe the voice record to text
import pyaudio
import wave
import whisper


def recordingVoice():
    # Parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"

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

    # Write to .wav file
    with wave.open(WAVE_OUTPUT_FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))


def transcribe_audio(file_path):
    # Load the model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(file_path)

    # Return the transcription
    return result["text"]


if __name__ == "__main__":
    recordingVoice()

    # Path to your WAV file
    wav_file = "output.wav"

    # Get the transcription
    transcription = transcribe_audio(wav_file)

    # Print the transcription
    print(transcription)
