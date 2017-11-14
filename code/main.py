#Main - calling program
import os
os.chdir("C:\\Users\\user\\Desktop\\Personal Assistant")

import speech_recognition as sr
import pyttsx
#import urllib.request
#import pafy
import vlc
import datetime
#import yweather
from pygame import mixer
from random import randint
from time import sleep
from determiner import determine
from setup import setMeUp
from gtts import gTTS as tts
from mutagen.mp3 import MP3
import threading
from subprocess import call

now=datetime.datetime.now()
year=now.year

def voiceInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

    try:
        mixer.music.load("2beep.mp3")
        mixer.music.play()
        voicequery=r.recognize_google(audio)
    except sr.UnknownValueError:
        #voiceOutput(["Sorry, I didn't quite get that."])
        return("ERROR_ID 000")
    except sr.RequestError as e:
        voiceOutput(["Network Error"])
        return("")
    return(voicequery)

def firstInput():
    print("Entered firstInput")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        audio=r.listen(source)
        print("Done listening!")
    try:
        print("Sending shit to google..")
        voicequery=r.recognize_google(audio)
    except sr.UnknownValueError:
        print("error")
        return("")
    except sr.RequestError as e:
        print("error")
        return("")
    print("Exiting with vq")
    return(voicequery)


def voiceOutput(textToSay):
    try:
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
        for strings in text:
            engine.say(strings)
        engine.runAndWait()
    

def thread_second():
    call(["python","alarmclock.py"])

def runAlarm():
    processThread = threading.Thread(target=thread_second)
    processThread.start()
    return

def checkForBirthday(dateofbirth):
    dateofbirth=dateofbirth[5:]
    datetoday=str(now)
    if datetoday[5:10]==dateofbirth:
        return True
    return False

def brackets_remove(string):
    returnString=""
    foundBracket=False
    for x in range(len(string)):
        if string[x]!="(" and string[x]!=")" and foundBracket==False:
            returnString+=string[x]
        elif string[x]=="(":
            foundBracket=True
            returnString=returnString[0:-1]
        elif string[x]==")":
            foundBracket=False
    return returnString


mixer.init()
engine=pyttsx.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-60)
volume=engine.getProperty('volume')
engine.setProperty('volume',1)

jokes=["It’s hard to explain puns to kleptomaniacs because they always take things literally.","A soldier survived mustard gas in battle, and then pepper spray by the police. He's now a seasoned veteran.","What's the best thing about Switzerland? I don't know, but their flag is a huge plus.","A Buddhist walks up to a hotdog stand and says, Make me one with everything.","What's the difference between my ex and the titanic? The titanic only went down on 1,000 people.","Two fish are sitting in a tank. One looks over at the other and says: 'Hey, do you know how to drive this thing?'","I told my doctor that I broke my arm in two places. He told me to stop going to those places.","How do you keep an stupid person in suspense?","I hate Russian dolls. They're so full of themselves.","My granddad has the heart of a lion and a lifetime ban from the San Diego Zoo.","Rick Astley will let you borrow any movie from his Pixar collection, except one. He's never gonna give you up."]

name,dateofbirth,gender,location=setMeUp(False,False,False,False)

isBirthday=checkForBirthday(dateofbirth)

if isBirthday==True:
    voiceOutput(["Happy birthday "+name, "I hope you have a wonderful day!"])
runAlarm()
voiceOutput(["Hello, "+name])
print("To activate me, say 'Olympia'")
print("Things I can do: play music, tell you the weather, give you the news, answer a question, do some math, define words and tell you a joke")
autoActivation=False
wikipediaFlag=False
while True:
    if autoActivation==False:
        choice=firstInput()
        print()
        print(choice)
        print()
    else:
        choice="olympia"
    print(choice)
    if "olympia" in choice.lower() or choice=="o":
        mixer.music.load("beep.mp3")
        mixer.music.play()
        choice=voiceInput()
        if choice=="ERROR_ID 000" and autoActivation==False:
            voiceOutput(["Sorry, I didn't quite get that."])
        whatToRun=determine(choice)
        if whatToRun=="tellMeMore" and wikipediaFlag!=True:
            voiceOutput("I haven't searched for anything!")
        elif whatToRun=="tellMeMore" and wikipediaFlag==True:
            import wikipedia
            outstring=brackets_remove([' '.join([wikipedia.summary(wiki_last_search,sentences=3)])])
            outstring=brackets_remove(outstring)
            voiceOutput([outstring])
        elif whatToRun=="music":
            choiceIsPure=False
            import play_music as pm
            if choice.split()[-1] == "music" or choice.split()[-2]=="music" or choice.split()[-1]=="song" or choice.split()[-2]=="song":
                voiceOutput(["What would you like to listen to?"])
                choice=voiceInput()
                choiceIsPure=True
            p=pm.playMusic(choice,choiceIsPure)
            input()
            p.stop()
        elif whatToRun=="math":
            from do_math import calculate
            answer=calculate(choice)
            if len(str(answer))>3000:
                voiceOutput(["This might take me a very long time.. Give me a moment please."])
            elif len(str(answer))>1000:
                voiceOutput(["This might take me a while. Are you writing all this down?"])
            voiceOutput([calculate(choice)])
        elif whatToRun=="weather":
            import weather_forecast as wf
            forecastedWeather=wf.Forecast(choice)
            voiceOutput([forecastedWeather])
            askedForWeather=False
        elif whatToRun=="drumpf":
            voiceOutput(["A demagogue"])
        elif whatToRun=="wiki":
            import wiki_search as ws
            wiki_tuple=ws.wikipedia(choice,1)
            mod=1
            while True:
                if len(wiki_tuple[0].split())<=2:
                    wiki_tuple=ws.wikipedia(choice,1+mod)
                    mod+=1
                else:
                    break
            wiki_result=wiki_tuple[0]
            wiki_last_search=wiki_tuple[1]
            wikipediaFlag=True
            wiki_result=brackets_remove(wiki_result)
            voiceOutput([wiki_result])
        elif whatToRun=="wolfram":
            voiceOutput(["What is your question?"])
            query=voiceInput()
            if query==None:
                voiceOutput(["Sorry, I didn't quite get that."])
            else:
                from question import answer
                answer=answer(query)
                answer=brackets_remove(answer)
                voiceOutput([answer])
        elif whatToRun=="xkcd":
            import xkcd_viewer as xv
            xv.xkcd()
        elif whatToRun=="dict":
            from word_knowledge import wordStuff
            voiceOutput([wordStuff(choice)])
        elif whatToRun=="news":
            import news_update as news
            newsTuple=news.getNews(choice)
            newsString=""
            for news in newsTuple:
                newsString+=news+".. "
            newsString=newsString[:-1]
            voiceOutput(["Sure "+name+". "+newsString])
        elif whatToRun=="chance":
            from chance import Chance
            voiceOutput([Chance(choice)])
        elif whatToRun=="alarm":
            from reminder import setAlarm
            playTime=setAlarm(choice)
            voiceOutput(["Alarm set for "+str(playTime)])
            runAlarm()
        elif whatToRun=="bohemian":
            try:
                pm.playMusic("Bohemian Rhapsody",True)
            except NameError:
                import play_music as pm
                pm.playMusic("Bohemian Rhapsody",True)
        elif choice.lower()=="what is the meaning of life" or choice.lower()=="what is the meaning of life the universe and everything?":
            voiceOutput(["42."])
        elif "joke" in choice.lower():
            try:
                usedjokes=usedjokes
            except NameError:
                usedjokes=["a"]
            if len(usedjokes)==len(jokes):
                usedjokes=["a"]
            joke="a"
            while joke in usedjokes:
                whichJoke=randint(0,len(jokes)-1)
                joke=jokes[whichJoke]
            voiceOutput([joke])
            usedjokes.append(joke)
        elif "auto" in choice.lower() and "activat" in choice.lower():
            if autoActivation==True:
                autoActivation=False
                voiceOutput(["Turning auto activation off."])
            else:
                autoActivation=True
                voiceOutput(["Turning auto activation on."])
        elif "bye" in choice:
            voiceOutput(["Goodbye!"])
            break
        elif whatToRun=="ERR":
            if autoActivation!=True:
                voiceOutput(["Sorry, I'm not sure what you want me to do."])
        elif whatToRun=="help":
            voiceOutput(["Which of these do you need help on?","Music? Weather? News? Wikipedia? Settings?"])
            helpChoice=voiceInput()
            if "music" in helpChoice:
                voiceOutput(["To play music, simply say","Can you play... and then tell me the name of the song","Alternatively, you can say","Put on some music and specify the song after I ask you."])
            elif "weather" in helpChoice:
                voiceOutput(["To get the weather, simply say","What's the weather like","and then specify the day that you're looking for.","For example, you could say.","Hey Brain, what's the weather like in four days","or you could even say","Hey Brain, what's the weather like in a week?","Please keep in mind that I can only see nine days into the future"])
            elif "wikipedia" in helpChoice.lower():
                voiceOutput(["To get information about a topic, simply say", "What is ... and then the name of the topic..", "Alternatively, you could say, 'wikipedia' and then the name of the topic"])
            elif "news" in helpChoice:
                voiceOutput(["To get the news, simply say", "Can you get me the news?", "Alternatively, you could say ","What are the headlines today?","Furthermore, you may specify which newspaper you would like to hear from - the current ones supported are: ","CNN, Fox News, The Economist, The Huffington Post, The New York Times and the Washington Post."])
            elif "settings" in helpChoice:
                voiceOutput(["You can change your settings here.","Currently, you can change your name, location, gender and birthday","Which of these would you like to change?"])
                settingToChange=voiceInput()
                settingToChange=settingToChange.lower()
                if "cancel" in settingToChange:
                    print("Cancelling")
                else:
                    didntGetThat=True
                    while didntGetThat==True:
                        didntGetThat=False
                        confirmedName=True
                        confirmedGender=True
                        confirmedBirthday=True
                        confirmedLocation=True
                        print(settingToChange)
                        if "name" in settingToChange:
                            os.remove("name.txt")
                            confirmedName=False
                        elif "gender" in settingToChange or "sex" in settingToChange:
                            os.remove("gender.txt")
                            confirmedGender=False
                        elif "birthday" in settingToChange or "birth" in settingToChange:
                            os.remove("birthday.txt")
                            confirmedBirthday=False
                        elif "location" in settingToChange or "city" in settingToChange:
                            os.remove("location.txt")
                            confirmedLocation=False
                        else:
                            voiceOutput(["Sorry, I didn't quite get that. Can you repeat?"])
                            settingToChange=voiceInput()
                            didntGetThat=True
                    name,dateofbirth,gender,location=setMeUp(confirmedName,confirmedGender,confirmedBirthday,confirmedLocation)
                    voiceOutput(["Change confirmed."])
