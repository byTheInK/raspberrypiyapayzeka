import os
from groq import Groq
from gtts import gTTS
from pydub import AudioSegment
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from json import load
from numpy import clip as np_clip

class voice():
    def __init__(self,api_key):
        
        self.key = api_key
        self.client = Groq(api_key=api_key)
    
    def speechToText(self,filename: str, language: str = "tr"):
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


    def get_length(self,filename: str) -> int:
        audio = AudioSegment.from_mp3(filename)
        return (len(audio)/1000)

    def record(self, freq: int = 44100, duration: int = 5, volume: float = 5.5) -> str:
        print("Recording started...")
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait()
        print("Recording finished")

        amplified_recording = np_clip(recording * volume, -1, 1)
        output_path = os.path.join("SOUNDS", "tts.wav")
        wv.write(output_path, amplified_recording, freq, sampwidth=2)
        print(f"Recording saved to {output_path}")

        return output_path

if __name__ == "__main__":
    with open("API.json") as f: 
        GROQ_API_KEY = load(f)["groq"]
    
    voice(GROQ_API_KEY).record(volume=10)