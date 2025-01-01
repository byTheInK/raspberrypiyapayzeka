import os
import json
import re
from time import sleep
from subprocess import CalledProcessError, DEVNULL, run
import MODULES.AI as AI
from MODULES.VOICE import voice

WINDOWS = os.name == "nt"
CLEAR_PREFIX = "cls" if WINDOWS else "clear"

SES_KAYIT_KAYIT_SURESI: int = 6
SES_KAZANC_BOYUTU: int = 10
SES_FREKANS_DEGERI: int = 44100
BASLANGICTA_HAFIZAYI_SIL: bool = True
HAFIZAYI_AKILDA_TUTMA_SINIRI: bool = 2000
SABIT_DEGERLER: dict = {"Language": "Türkçe"}

with open("API", "r") as file:
    GROQ_API_KEY = file.read()
    print("API KEY LOADED")

textEngine = AI.text(GROQ_API_KEY, "memory.json", SABIT_DEGERLER, HAFIZAYI_AKILDA_TUTMA_SINIRI)
print("TEXT LOADED")
voiceEngine = voice(GROQ_API_KEY)
print("VOICE LOADED")
print("WINDOWS" if WINDOWS else "LINUX", "İŞLETİM SİSTEMİNDE ÇALIŞIYOR")

def kill_vlc():
    try:
        if WINDOWS:
            run(["powershell", "-Command", "Stop-Process -Name 'vlc' -Force"], shell=True, check=True, stderr=DEVNULL)
        else:
            run(["pkill", "vlc"], check=True, stderr=DEVNULL)
    except CalledProcessError:
        print("VLC kapatılmış bu nedenle bulunamadı")
        return

def mainVoice():
    print("Başlangıçta hafızayı sil:", BASLANGICTA_HAFIZAYI_SIL)
    if BASLANGICTA_HAFIZAYI_SIL:
        with open("memory.json", "r+") as memory_file:
            memory_file_content = memory_file.read().strip()
            if memory_file_content:
                memory_data = json.loads(memory_file_content)
            else:
                memory_data = None
            with open("OTHER\\yedek.json" if WINDOWS else "OTHER/yedek.json", "w") as f:
                if memory_data is not None:
                    json.dump(memory_data, f, indent=4)
            if memory_data is not None:
                memory_file.seek(0)
                memory_file.truncate()

    while True:
        input()
        print("Ses Kaydı Başladı")
        voiceEngine.record(freq=SES_FREKANS_DEGERI, duration=SES_KAYIT_KAYIT_SURESI, volume=SES_KAZANC_BOYUTU)
        print("Ses Kaydı Bitti")

        question = voiceEngine.speechToText("SOUNDS\\tts.wav" if WINDOWS else "SOUNDS/tts.wav")
        print(f"Recognized question: {question}")

        if question == " Altyazı M.K.":
            question = ""

        response = textEngine.createResponseWithData(question, "user")
        Edited_R = re.sub(r'[^\w\s,.!?]', '', response)

        voiceEngine.textToSpeech(Edited_R, "SOUNDS\\tts.mp3")
        #os.system("start SOUNDS\\tts.mp3" if WINDOWS else "mpg123 SOUNDS/tts.mp3")
        print("CEVAP:\n", response)

        print("SORU:\n", question)

        sleep(voiceEngine.get_length("SOUNDS\\tts.mp3"))
        kill_vlc()

if __name__ == "__main__":
    mainVoice()