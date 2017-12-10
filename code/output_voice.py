from gtts import gTTS as tts
from tinytag import TinyTag as tt
from time import sleep
from changeDir import changeDirectory
import subprocess

def voiceOutput(textToSay):
    try:
        changeDirectory("resources")
        fullstr=""
        for strings in textToSay:
            fullstr+=strings+". "
        fullstr=fullstr[:-1]
        whatToSay=tts(text=fullstr,lang='en')
        whatToSay.save("output.mp3")
        audio=tt.get("output.mp3")
        subprocess.run("output.mp3",shell=True)
        sleep(audio.duration)
    except ConnectionError:
        print("connection error")
    return
