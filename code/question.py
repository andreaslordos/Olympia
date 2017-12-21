def answer(userinput):
    from urllib import request
    def getSpoken(app_id,query):
        url="http://api.wolframalpha.com/v1/spoken?appid="+app_id+"&i="+query
        url='+'.join(url.split())
        html=request.urlopen(url)
        contents=html.read()
        contents=contents.decode('utf-8')
        return contents
    
    def cleanUp(answer):
        for x in range(len(answer)):
            if answer[x]=="\n":
                answer=answer[0:x]+" "+answer[x+1:]
                return answer
        return answer
    
    try:
        app_id="GET YOUR OWN APP_ID AT https://developer.wolframalpha.com"
        answer=getSpoken(app_id,userinput.lower())
        return answer
    except:
        print("Sorry, but you need to get your own app ID. You can get one at developer.wolframalpha.com to enable the Wolfram Alpha API")
        return "Sorry, you need your own app I.D."

