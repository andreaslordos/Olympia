from gtts import gTTS as tts
from tinytag import TinyTag as tt
from pygame import mixer
from time import sleep
from os import chdir
from os import remove
from os import getcwd
from changeDir import changeDirectory
def voiceOutput(textToSay):
    try:
        changeDirectory("resources")
        fullstr=""
        for strings in textToSay:
            fullstr+=strings+". "
        fullstr=fullstr[:-1]
        whatToSay=tts(text=fullstr,lang='en')
        whatToSay.save("output.mp3")
        mixer.init()
        mixer.music.load("output.mp3")
        mixer.music.play()
        try:
            changeDirectory("resources")
            audio=tt.get("output.mp3")
        except:
            print(getcwd())
            changeDirectory("code")
            audio=tt.get("output.mp3")
        sleep(audio.duration)
        mixer.music.stop()
        mixer.quit()
    except ConnectionError:
        print("connection error")
    return
