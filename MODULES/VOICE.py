import os
import sounddevice as sd
import wavio as wv
from numpy import clip as np_clip
from gtts import gTTS
from pydub import AudioSegment
from groq import Groq

class voice():
    def __init__(self, api_key):
        self.key = api_key
        self.client = Groq(api_key=api_key)

    def speechToText(self, filename: str, language: str = "tr"):
        with open(filename, "rb") as file:
            transcription = self.client.audio.transcriptions.create(
                file=(filename, file.read()),
                model="whisper-large-v3",
                response_format="json",
                language="tr",
                temperature=0.0 
            )
            return transcription.text

    def textToSpeech(self, message: str, filename: str) -> None:
        complete = gTTS(
            text=message,
            lang="tr",
            slow=False
        ).save(filename)

    def get_length(self, filename: str) -> int:
        audio = AudioSegment.from_mp3(filename)
        return (len(audio) / 1000)+1

    def record(self, freq: int = 44100, duration: int = 5, volume: float = 5.5) -> str:
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
        sd.wait()

        amplified_recording = np_clip(recording * volume, -1, 1)
        output_path = os.path.join("SOUNDS", "tts.wav")
        wv.write(output_path, amplified_recording, freq, sampwidth=2)
        print(f"Recording saved to {output_path}")

        return output_path