from gtts import gTTS as tts
from mutagen.mp3 import MP3
from pygame import mixer
from time import sleep
from os import chdir
mixer.init()
def voiceOutput(textToSay):
    try:
        chdir("C:\\Users\\user\\Desktop\\Personal Assistant")
        fullstr=""
        for strings in textToSay:
            fullstr+=strings+". "
        fullstr=fullstr[:-1]
        whatToSay=tts(text=fullstr,lang='en')
        whatToSay.save("output.mp3")
        mixer.music.load("output.mp3")
        mixer.music.play()
        audio=MP3("output.mp3")
        sleep(audio.info.length+2)
        mixer.music.stop()
    except ConnectionError:
        import pyttsx
        engine=pyttsx.init()
        rate=engine.getProperty('rate')
        engine.setProperty('rate',rate-60)
        volume=engine.getProperty('volume')
        engine.setProperty('volume',1)
        for strings in text:
            engine.say(strings)
        engine.runAndWait()
    return
