from gtts import gTTS as tts
from os import chdir
from tinytag import TinyTag as tt
from time import sleep
import subprocess
dirFile=open("dir.txt","r")
directory=dirFile.read()
dirFile.close()
def voiceOutput(textToSay):
    try:
        chdir(directory+"\\resources")
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
