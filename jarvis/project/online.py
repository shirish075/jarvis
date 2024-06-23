from wikipedia import WikipediaException

from offline import *

try:
    import lxml  # for web scrapping
    import pywhatkit  # for using WhatsApp & others like browsers,google search ,YT
    # for requesting the url for data
    from bs4 import BeautifulSoup  # for formatting the file
    import wikipedia
except Exception as err:
    print(err)


# # configuring the voice----
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 150)
# # end of configuring----------


# def recogniser.speak(text):
#     engine.say(text)
#     print(text)
#     engine.runAndWait()


def mainfunc(funcname, query):
    # Thinking()
    if "greetings" in funcname:
        say_greetings()
    elif "identity" in funcname:
        say_introduce()
    elif "bye" in funcname:
        recogniser.speak("bye sir")
        recogniser.speak("dont hesitate to call me when i needed")
        exit()
    elif "google" in funcname:
        try:
            query = query.replace("search", "")
            query = query.replace("google", "")
            query = query.replace("for", "")
            query = query.replace("in", "")
            query = query.replace("on", "")
            pywhatkit.search(query)
        except Exception as err:
            print(err)

    elif "open" in funcname or "open app" in funcname or "open application" in funcname or "launch" in funcname:
        open_applications(query)
    elif "time" in funcname:
        say_time()

    elif "WhatsApp message".lower() in funcname.lower():
        whats_app()

    elif "quiz" in funcname:
        pass

    elif "student results" in funcname:
        studentResult()
    elif "joke" in funcname:
        headers = {
            'Accept': 'application/json'
        }
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        recogniser.speak(res["joke"])
    elif "date" in funcname:
        say_date()
    elif "youtube" in funcname:
        recogniser.speak("what to search on youtube")
        search = recogniser.test_recogniser()
        if search != None and search != "" and search != " ":
            pywhatkit.playonyt(search)
    elif "screenshot" in funcname:
        say_screenshot()
    elif "advice" in funcname:
        res = requests.get("https://api.adviceslip.com/advice")
        advice = res['slip']['advice']
        recogniser.speak(advice)

    elif "weather" in funcname:
        openweather()
        # recogniser.speak("at what location do you want to know")
        # loc = recogniser.test_recogniser()
        # url = f"https://www.google.com/search?q=temperature+in+{loc}"
        # r = requests.get(url)
        # data = BeautifulSoup(r.text, "html.parser")
        # temp = data.find("div", class_="BNeawe").text
        # recogniser.speak(temp)
    elif "wikipedia search" in funcname:
        try:
            query = query.replace("wikipedia", "")
            query = query.replace("for", "")
            query = query.replace("in", "")
            query = query.replace("search", "")

            recogniser.speak("1." + wikipedia.suggest(query))
            recogniser.speak("2." + str(wikipedia.search(query, results=1)))
            recogniser.speak("do ypu wanna search for 1 or 2")
            ot = recogniser.test_recogniser()
            if ot == 1 or "one" in ot:
                wikipedia.summary(wikipedia.suggest(query))
            else:
                e = wikipedia.search(query, results=1)
                print(e[0])
                recogniser.speak(wikipedia.summary(e[0]))

        except WikipediaException as err:
            print(err)
    elif "location" in funcname:
        jlan, jlon = mylocation()
        speak("you are at")
        speak(locbyco(jlan, jlon)[3]["formatted_address"])
    elif "ip" in funcname:
        speak(getIP())
    elif "calculations" in funcname:
        while True:
            recogniser.speak("what do you want to compute")
            query = recogniser.test_recogniser()
            if "exit" in query:
                break
            else:
                try:
                    recogniser.speak(wolfRam(query))
                except Exception as err:
                    print(err)
    elif "speedteest" in funcname:
        recogniser.speak("testing your internet speed")
        recogniser.speak(speedteest())
    elif "news" in funcname:
        head = news()
        recogniser.speak("reading top 5 news head lines")
        for h in head:
            recogniser.speak(h)
    elif "shutdown" in funcname:
        say_shutdown()
    elif "restart" in funcname:
        say_restart()
    elif "sleep" in funcname:
        say_sleep()
    elif "email" in funcname:
        send_mail()
    elif "send_message" in funcname:
        recogniser.speak("to whom you want to send the message")
        who = recogniser.test_recogniser()
        recogniser.speak("what is the message")
        msg = recogniser.test_recogniser()
        recogniser.speak(f"sending message {msg} to {who}")
        send_message(who, msg)
    elif "callto" in funcname:
        recogniser.speak("to whom you want to call")
        name = recogniser.test_recogniser()
        callto(name)
    elif "translate" in funcname:
        translate()
    elif "nearby" in funcname:
        speak("what do you want to search")
        loc = test_recogniser()
        nearby(loc)
    elif "get_trending_movies" in funcname:
        get_trending_movies()
    elif "iot" in funcname:
        iot(query)
    elif "emergency" in funcname:
        emergency()
    elif "advance_speak" in funcname:
        while True:
            question = test_recogniser()
            if "exit" == question:
                break
            speak(ReplyBrain(question))
            # SititngTalking()

    else:
        if query != None:
            pass
    time.sleep(4)
    #         recogniser.speak(f"can i search in google for {query}")
    #         yon = recogniser.recogniser.test_recogniser()
    #         if "yes" in yon :
    #             recogniser.speak("I found these results in google")
    #             webbrowser.open(query)
