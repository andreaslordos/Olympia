import datetime
from time import sleep
def alarmclock():
    try:
        datetime.datetime.now()
        f=open("reminders.txt","r")
        contents=f.read()
        try:
            contents=contents.split("#")[:-1]
        except:
            pass
        if contents==[""]:
            return
        soonest=None
        now=datetime.datetime.now()
        for dates in contents:
            year=int(dates.split("-")[0])
            month=int(dates.split("-")[1])
            day=int(dates.split("-")[2].split()[0])
            secondSegment=dates.split(" ")[1]
            hour=int(secondSegment.split(":")[0])
            minutes=int(secondSegment.split(":")[1])
            seconds=int(secondSegment.split(":")[2])
            alarmTime=datetime.datetime(year, month, day, hour, minutes, seconds, 0)
            if soonest==None and (alarmTime-now).total_seconds()>0:
                soonest=(alarmTime-now).total_seconds()
            elif soonest>(alarmTime-now).total_seconds() and (alarmTime-now).total_seconds()>0:
                soonest=(alarmTime-now).total_seconds()
        print(soonest)
        sleep(soonest)
        from play_music import playMusic
        p=playMusic("country road",True)
        input()
        p.stop()
        try:
            contents.remove(str(alarmTime))
            writeToFile='#'.join(contents)+"#"
            open('reminders.txt', 'w').close()
            f=open("reminders.txt","w")
            if writeToFile!="#":
                f.write(writeToFile)
            f.close()
            alarmclock()
        except Exception as e:
            print(e)
            input()
    except Exception as e:
        print(e)
        input()

alarmclock()