# import ctypes
import json
import os
import random
import smtplib
import subprocess
import time
from datetime import datetime
from tkinter import *
from tracemalloc import Frame

import PyPDF2
import clipboard
import cv2
import pyperclip
from cryptography.fernet import Fernet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from selenium.webdriver.common.by import By

from ai_files.detection.detection import detection
from recogniser import *

key = b'sk2hnlOOdclmPRUB6UJG9MdnUMLgZU2-XOKSyZkSF6U='
en_line = []
lis = []
de_line = []

try:
    import wolframalpha as wolframalpha
    import speedtest
    # from nltk.sentiment import SentimentIntensityAnalyzer
    import webbrowser
    from urllib.request import urlopen
    from selenium.webdriver.chrome.service import Service
    import requests
    import pandas
    import re as ra
    import selenium
    from selenium import webdriver
    import pywhatkit
except:
    print("no internet")


def studentResult():  # extracting student result
    pin = []
    name = []
    result = []
    sgpa = []
    for num in range(1, 55):
        try:
            strin = "20189-CM-" + '%03d' % num
            raw = requests.get(
                "https://www.sbtet.telangana.gov.in/API/api/Results/GetStudentWiseReport?ExamMonthYearId=62&ExamTypeId=5&Pin=" + strin + "&SchemeId=5&SemYearId=4&StudentTypeId=1",
                verify=False)
            raw_data = raw.json()
            print("student pin::", raw_data[0]['studentInfo'][0]['Pin'])
            print("Student name::", raw_data[0]['studentInfo'][0]['StudentName'])
            print("result::", raw_data[0]['studentSubjectTotal'][0]['Result'])
            print("Student sgpa::", raw_data[0]['studentSGPACGPAInfo'][0]['SGPA'])
        except Exception as err:
            print("err in connecting")

        try:
            pin.append(raw_data[0]['studentInfo'][0]['Pin'])
            name.append(raw_data[0]['studentInfo'][0]['StudentName'])
            result.append(raw_data[0]['studentSubjectTotal'][0]['Result'])
            sgpa.append(raw_data[0]['studentSGPACGPAInfo'][0]['SGPA'])

        except Exception as err:
            print(err)

    dataframe = pandas.DataFrame({'pin': pin,
                                  'name': name,
                                  'result': result,
                                  'sgpa': sgpa
                                  })
    dataframe.to_csv("marks2.csv", index=False)


def whats_app():  # whatsapp message sender

    speak("do you want to message a number or a contact")
    yon = test_recogniser()
    if "number" in yon:
        try:
            speak("please say a number to send the message")
            number = test_recogniser()
            speak("what message do you want to send")
            message = test_recogniser()
            speak("do you want to send message now?")
            rawdes = test_recogniser()
            if "yes" in rawdes:
                pywhatkit.sendwhatmsg_instantly('+91' + number.strip(), message, wait_time=5)
            else:
                speak("at what hour do you what to send message")
                hour = test_recogniser()
                speak("at what minute do you want to send message")
                minu = test_recogniser()
                pywhatkit.sendwhatmsg('+91' + number, message, hour, minu)
                pg.hotkey('enter')
        except Exception as err:
            print(err)

    else:
        speak("please make sure that you had already connected web whatsapp to this pc")
        time.sleep(1)
        speak("to who whom you want to send message")
        name = test_recogniser()
        speak("what is the message you want to send?")
        message = test_recogniser()
        options = webdriver.ChromeOptions()
        path = os.path.expanduser("~\\")
        options.add_argument(f'--user-data-dir={path}AppData\\Local\\Google\\Chrome\\User Data\\Default')
        options.add_argument('--profile-directory=Default')
        options.add_experimental_option("detach", True)

        chrome_browser = webdriver.Chrome(executable_path=r'E:\project\chromedriver.exe', options=options)
        chrome_browser.get('https://web.whatsapp.com/')
        time.sleep(30)
        # search bar
        s = chrome_browser.find_element(By.CSS_SELECTOR,
                                        "#side > div.uwk68 > div > div > div._16C8p > div > div._13NKt.copyable-text.selectable-text")
        s.click()  # clicking search bar
        s.send_keys(name)  # entering name
        time.sleep(2)
        chrome_browser.find_element(By.CSS_SELECTOR,
                                    "#pane-side > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div > div._3OvU8").click()
        # clixking in name --^
        time.sleep(2)
        s = chrome_browser.find_element(By.CSS_SELECTOR,
                                        "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div.fd365im1.to2l77zo.bbv8nyr4.mwp4sxku.gfz4du6o.ag5g9lrv")
        # clicking in chat box __^
        s.click()
        s.send_keys(message)
        s = chrome_browser.find_element(By.CSS_SELECTOR,
                                        '#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k')
        s.click()


def getIP():
    d = str(urlopen('http://checkip.dyndns.com/').read())
    return ra.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)


import asyncio
import winsdk.windows.devices.geolocation as wdg

aapikey = ""
import googlemaps

gmaps = googlemaps.Client(key=aapikey)


############################################location and nearby
async def getCoords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.latitude, pos.coordinate.longitude]


def getLoc():
    try:
        return asyncio.run(getCoords())
    except PermissionError:
        print("ERROR: You need to allow applications to access you location in Windows settings")


def locbyco(latitude, longitude):
    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    test1 = reverse_geocode_result
    # print(test1)
    return (test1)


def mylocation():
    [lat, lon] = getLoc()
    return lat, lon


def nearby(wplace):
    from googleplaces import GooglePlaces
    placename_list = []
    address_list = []
    phone_list = []
    url_list = []
    google_places = GooglePlaces(aapikey)
    lat, lon = mylocation()
    query_result = google_places.nearby_search(
        lat_lng={"lat": lat, "lng": lon}, keyword=wplace, rankby="distance")
    print(query_result)
    if query_result.has_attributions:
        print(query_result.html_attributions)

    # Iterate over the search results
    for place in query_result.places:
        # print(type(place))
        # print(place.get_details())
        # print(place.name)
        placename_list.append(place.name)
        # print(place.geo_location['lat'],place.geo_location['lng'])
        id = locbyco(place.geo_location['lat'], place.geo_location['lng'])[0]["place_id"]
        url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={id}&key={aapikey}"
        phoneQuery = requests.get(url)
        phoneNumbs = phoneQuery.json()['result']
        # print(phoneNumbs)
        # print(phoneNumbs.get("formatted_phone_number"))
        # print(phoneNumbs.get("formatted_address"))
        url_list.append(phoneNumbs.get("url"))
        phone_list.append(phoneNumbs.get("formatted_phone_number"))
        address_list.append(phoneNumbs.get("formatted_address"))
    # open chrome and search address_list[0]
    # print(address_list[0])
    from tkinter import ttk
    import tkinter

    window = tkinter.Tk()
    window.title("Places Near You")
    window.geometry("1800x1500")
    # bg = tkinter.PhotoImage(file=r"C:\project\nowt\project\nearbylocation.png")
    window.configure(bg="white")
    # label1 = tkinter.Label(window, image=bg)
    # label1.place(x=0, y=0)
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)

    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    label = tkinter.Label(window, text="Places Near You", font=("Arial", 20))
    label.pack()
    # placename_list, address_list, phone_list, url_list = nearby("theaters")
    # print place-name_list , address_list, phone_list, url_list in labels
    for i in range(0, len(placename_list)):
        label = tkinter.Label(second_frame, text=placename_list[i], font=("Arial", 10), border=0)
        label.pack()
        label = tkinter.Label(second_frame, text=address_list[i], font=("Arial", 10), border=0)
        label.pack()
        label = tkinter.Label(second_frame, text=phone_list[i], font=("Arial", 10), border=0)
        label.pack()
        label = tkinter.Label(second_frame, text=url_list[i], font=("Arial", 10), border=0, fg="blue", cursor="hand2")
        label.pack()
        label.bind("<Button-1>", lambda e: webbrowser.open(url_list[i]))
        label = tkinter.Label(second_frame, text="", background="white", font=("Arial", 10))
        label.pack()
        label = tkinter.Label(second_frame, text="", background="white", font=("Arial", 10))
        label.pack()
    window.mainloop()
    speak("redirecting to google maps")
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url_list[0])


# nearby()
def wolfRam(query):
    api_key = ""
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text

        return Answer
    except Exception as err:
        speak(err)


def speedteest():
    s = speedtest.Speedtest()
    download_speed = s.download()
    upload_speed = s.upload()
    s.get_best_server()
    ping = s.get_servers()
    s = 'Download Speed is {:5.2f} Mb'.format(download_speed / (1024 * 1024)) + ' upload Speed is {:5.2f} Mb'.format(
        upload_speed / (1024 * 1024)) + " and the ping is " + str(s.results.ping)
    return s


def news():
    news_headlines = []
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=0a7ce9b1b19e4608acc8535ac05b16d9')
    response = requests.get(url)
    raw_article = response.json()
    articles = raw_article['articles']
    for article in articles:
        news_headlines.append(article["title"])
    return (news_headlines[:5])


def openweather():
    api_key = ""
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'  # "https://api.openweathermap.org/data/2.5/weather?"
    jlan, jlon = mylocation()

    complete_url = base_url + f'lat={jlan}&lon={jlon}&' + "appid=" + api_key
    print(complete_url)
    try:
        response = requests.get(complete_url)
        x = response.json()
        print(x)
        if x["cod"] != "404":
            y = x["main"]
            print(y)
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            print("z", z)
            weather_description = z[0]["description"]
            print("weather_descriptionweather_description", weather_description)
            speak(f'''weather at your location {locbyco(jlan, jlon)[3]["formatted_address"].split(",")[1]} is''')
            speak(" Temperature in degree celsius unit is " +
                  str('%.2f' % (current_temperature - 273)) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
        else:
            speak(" City Not Found ")
    except:
        speak("something went wrong please try again")


def killtask(app):
    # os.system("taskkill /f /im "+app+".exe")
    progname = []
    progid = []
    progdesc = []
    cmd = 'powershell "gps | ? {$_.mainwindowhandle } | select ProcessName | ft -HideTableHeaders"'
    cmd2 = 'powershell "gps | ? {$_.mainwindowhandle } | select description | ft -HideTableHeaders"'
    cmd1 = 'powershell "gps | ? {$_.mainwindowhandle } | select id | ft -HideTableHeaders"'

    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    proc1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        st = progname.append(line.decode('utf-8').rstrip())
        progname.append(st)
    for line in proc1.stdout:
        st = progid.append(line.decode('utf-8').rstrip())
        progid.append(st)
    for line in proc2.stdout:
        st = progdesc.append(line.decode('utf-8').rstrip())
        progdesc.append(st)

    for name, desc, id in zip(progname, progdesc, progid):
        if app.lower() in str(desc).lower() or app in str(name).lower():
            os.system("taskkill /F /PID " + str(id))

            # break
    if "explorer" in app:
        os.system('explorer.exe')
    return f'{app} is closed'


def changevoice():
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[1].id)
    speak("voice changed")
    print(engine.getProperty())


def sentiment_analysis(text):
    message = text
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(message)
    for k in ss:
        print('{0}: {1}, '.format(k, ss[k]), end='')
    if ss['compound'] >= 0.05:
        a = "positive"
        print('Positive')
    elif ss['compound'] <= - 0.05:
        a = "negative"
        print('Negative')
    else:
        a = "neutral"
        print('Neutral')
    return ss['compound'], a


focus_window = 0


def focus_submit(name):
    global focus_window
    focus_window.destroy()
    global enter

    time1 = name.get()
    time1 = time1.replace(":", '.')
    print(time1)
    time1 = float(time1)
    curtime = float(datetime.now().strftime("%H.%M"))
    time1 = float("{:.2f}".format(time1 + curtime))
    sleeptime = float("{:.2f}".format(time1 - curtime))
    sleeptime = sleeptime * 600
    '''C:\Windows\System32\drivers\etc\hosts'''
    # change hosts file
    webssites = ["www.facebook.com", "www.instagram.com", "www.twitter.com", "www.whatsapp.com", "www.tiktok.com"]
    redirect = "127.0.0.1"
    with open(r"C:\\Windows\\System32\\drivers\\etc\\hosts", "r+") as file:
        print("opened file")
        content = file.read()
        # file.seek(0, 0)
        for website in webssites:
            file.write(f"\n{redirect}  {website}")
        speak("completed writing")
        content = file.read()
        file.close()
        print(sleeptime)
        time.sleep(sleeptime)
        speak("waking up")
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w") as file:
            for line in content:
                if line in webssites:
                    file.write('')
                else:
                    file.write(line)
    speak("Focus mode completed")


def focus_mode():
    global enter
    global focus_window
    speak("entering into focus mode..")
    # time1 = input("enter how much time you want to spend in focus mode(eg:0hr:0min)")
    focus_window = Tk()
    name = StringVar()
    label1 = Label(focus_window, text="enter how much time you want to spend in focus mode(eg:0hr:0min)").pack()
    enter = Entry(focus_window, textvariable=name).pack()

    but = Button(focus_window, command=lambda: focus_submit(name), text="enter").pack()

    focus_window.mainloop()


def say_time():  # time function
    m = "am" if datetime.now().hour < 12 else "pm"
    speak(f"the time is {datetime.now().hour % 12}  {datetime.now().minute} {m} ")


def say_date():  # date function
    now = datetime.now()
    speak(now.strftime("%d-%m-%Y"))


def say_screenshot():  # function to capture screenshot
    speak("what name you want to give for screenshot?")
    name = test_recogniser()
    if name == "" or name == None:
        name = f"screenshot{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    path = os.path.expanduser("~\\")
    try:
        pg.screenshot(path + "Pictures\\Screenshots\\" + name + ".png")
    except:
        pg.screenshot(path + "OneDrive\\Pictures\\Screenshots\\" + name + ".png")
    speak("screenshot taken")


def say_sleep():
    speak("going to sleep")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def say_restart():
    speak("restarting")
    os.system("shutdown /r /t 1")


def say_shutdown():
    speak("shutting down")
    os.system("shutdown /s /t 1")


def say_greetings():
    speak("hello sirr")
    # hai()
    speak("this is jarvis your voice assistant tell me what can i do for you!!")


def say_introduce():
    speak(
        "i am jarvis your virtual assistant. you can tell ask me things like what is the time now ,date now. i can find your location if you give command find location, i can do any math and science related problems if you say help me in math, i can also open apps what ever you want try saying open file explore or something like that,you can play quiz game by saying quiz game, you can say things like open youtube i can search anything and everything in google by just saying search on google , i can also capable to send whatsapp messages i can take screen shot,say jokes , give advices , say weather at any location, search wikipedia ex at raa")


def open_applications(query):  # opening applications
    from AppOpener import run, give_appnames
    apps = list(give_appnames())
    query = str(query).lower()
    try:
        query = query.replace("open", "")
        query = query.replace("application", "")
        query = query.replace("app", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        print(query)
        for i in apps:
            print(f"{query} in {i}")
            if query in str(i).replace(" ", ""):
                # print(f"query {query} i {i}")
                run(i)
    except Exception as e:
        print(e)
    time.sleep(7)
    pg.hotkey('win', 'up')


def reader():  # reader fun
    text = clipboard.paste()
    speak(text)


# send mail
def sendEmail(to, message):  # email sending
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shirishponaganti7@gmail.com', 'vtymmfmoqourrpvu')
    server.sendmail("shirishponaganti7@gmail.com", to, message)
    server.close()
    speak("email sent")


def send_mail():
    try:
        speak("what is the message")
        message = test_recogniser()
        speak("whom do you want to send")
        to = test_recogniser()
        sendEmail(to, message)  # calling the sendEmail method
        speak("Email has been sent !")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")


# play random songs from folder
def play_random_song():  # music playing method
    path = os.path.expanduser("~\\") + "Music\\"
    songs = os.listdir(path)
    os.startfile(os.path.join(path, songs[random.randint(0, len(songs) - 1)]))


# open documents
def open_documents():  # opening documents
    speak("what is the document name")
    name = str(test_recogniser())
    path = os.path.expanduser("~\\")
    if name != "" or name != None:
        for (root, dirs, files) in os.walk(f'{path}\\Documents\\', topdown=True):
            for file in files:
                if name in str(file):
                    os.startfile(str(root) + "/" + str(file))
                    break
                else:
                    speak("file not found")


def notepad():  # entering data into the notepad
    os.startfile("notepad")
    speak("say the text you want to enter. say exit 1 when you want to exit")
    while True:
        text = test_recogniser()
        if text is None or text == "":
            continue
        if "exit" in text and ("one" in text or "1" in text):
            break
        if "backspace" == text.strip() or "delete" == text or "back space" == text:
            pg.hotkey("ctrl", "backspace")
        if "selectedtext" == text or "selected text" == text:
            pg.hotkey("shift", "left")
        else:
            if "next line" in text:
                pg.press("enter")
            else:
                pg.typewrite(text)
    speak("give a name to save this file")
    name = test_recogniser()
    pg.hotkey("ctrl", "s")
    pg.typewrite(name + " ")
    pg.press("enter")
    speak("file saved")
    os.system("taskkill /im " + 'Notepad' + ".exe /f")


def open_folder():  # opening a desired folder
    speak("what is the drive name")
    dname = test_recogniser()
    dname.replace("drive", "")
    dname.replace("at", "")
    dname = dname.capitalize()
    dname = dname + ":"
    speak("what is the folder name")
    fname = test_recogniser()
    if (dname != "" or dname != None) and (fname != "" or fname != None):
        try:
            for (root, dirs, files) in os.walk(f'{dname}', topdown=True):
                for file in files:
                    if fname in str(file):
                        os.startfile(str(root) + "/" + str(file))
                        break
        except EXCEPTION as e:
            print(e)
            speak("folder not found")


def pdf_reader():  # reading pdf
    speak("what is the pdf name")
    name = test_recogniser()
    name = name.lower()
    path = os.path.expanduser('~\\Documents')
    if name != "" or name != None:
        for (root, dirs, files) in os.walk(path, topdown=True):
            for file in files:
                if name in str(file).lower():
                    os.startfile(str(root) + "/" + str(file))
                    break
    pdf = open(f'{path}\\{name}.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pages = pdfReader.numPages
    speak(f"total number of pages in this pdf is {pages}")
    speak("do you want to listen from starting or from a page number")
    some = test_recogniser()
    if "starting" in some:
        for num in range(0, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speak(text)
    elif "page" in some:
        speak("what is the page number")
        pagenum = int(test_recogniser())
        page = pdfReader.getPage(pagenum)
        text = page.extractText()
        speak(text)


def get_trending_movies():
    TMDB_API_KEY = ''
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:10]


def copy_files(q):  # copying the files
    s = ""
    if q == "copy":
        s = "c"
    elif q == "move":
        s = "x"
    speak("to copy files please make sure that you have already opened the folder")
    speak("can i copy selected files or all files")
    yoj = test_recogniser()
    if "all files" in yoj:
        pg.hotkey("ctrl", "a")
        pg.hotkey("ctrl", s)
    else:
        pg.hotkey("ctrl", s)
    time.sleep(2)
    speak("files copied")
    speak("at which drive files should be placed")
    drive = test_recogniser()
    drive = drive.replace("drive", "")
    drive = drive.replace("at", "")
    drive = drive.capitalize()
    drive = drive.strip() + ":"
    path = drive
    while True:
        speak("folder name to paste the files")
        folder = test_recogniser()
        if "that's all" in folder or "enough" in folder or "paste there" in folder:
            break
        for dirs in os.listdir(path):
            if folder in str(dirs):
                path = path + "/" + folder
                break
    os.startfile(path)
    time.sleep(5)
    pg.hotkey("ctrl", "v")
    speak("files pasted")


def learn():
    test = open(r"C:\project\nowt\project\ai_files\intents.json", "r")
    intents = json.load(test)
    e = True
    i = 0
    pattern = []
    responses = []

    tag = input("say what is the tag::")  # test_recogniser()
    speak("enter the pattern and say exit when patterns are enough:")
    while e:
        query = input()
        if query == "exit":
            break
        else:
            pattern.append(query)
        i += 1
    speak("enter the responses and say exit when responses are enough")
    i = 0
    while e:
        query = input()
        if query == "exit":
            break
        else:
            responses.append(query)
        i += 1
    intents["intents"] += [{'tag': f'{tag}', 'patterns': pattern, 'responses': responses}]
    test.close()

    with open(r"C:\project\nowt\project\ai_files\intents.json", "w") as file:
        file.write(json.dumps(intents))
    from ai_files.Train import Train
    Train()


def send_message(who, mssg):
    from pywinauto.application import Application
    open_applications("open app phone link")
    time.sleep(10)
    app = Application(backend="uia").connect(title="Phone Link", timeout=3000)
    # print(app.PhoneLink.print_control_identifiers())
    but = app.PhoneLink.child_window(best_match="TabItem", auto_id="MessagingNodeAutomationId",
                                     control_type="TabItem").wrapper_object()
    time.sleep(5)
    but.click_input()
    # app.Phonelink.print_control_identifiers()
    msgbut = app.PhoneLink.child_window(title="New message", auto_id="NewMessageButton",
                                        control_type="Button").wrapper_object().click_input()
    text = app.PhoneLink.child_window(title="To", control_type="Text").wrapper_object()
    text.type_keys(f"{who}", with_spaces=True)
    time.sleep(5)
    pg.hotkey("enter")
    time.sleep(5)
    app.PhoneLink.child_window(auto_id="InputTextBox", control_type="Edit").click_input()
    time.sleep(5)
    msg = app.PhoneLink.child_window(auto_id="InputTextBox", control_type="Edit").wrapper_object()
    time.sleep(5)
    msg.type_keys(f"{mssg}", with_spaces=True)
    time.sleep(5)
    # app.Phonelink.print_control_identifiers()
    app.PhoneLink.child_window(title="Send", auto_id="SendMessageButton", control_type="Button").click_input()
    time.sleep(5)


def emergency():
    l, b = mylocation()
    tex = locbyco(l, b)[3]["formatted_address"]
    send_message("shirish", f"it's an emergency. Come here {tex} coordinates are:{l},{b}")
    send_message("narandra", f"it's an emergency. Come here {tex} coordinates are:{l},{b}")
    send_message("pramod mekala", f"it's an emergency. Come here{tex} coordinates are:{l},{b}")


####################################################encryption
def encrypt():
    global en_line
    with open("passwr.txt", "rb") as file:
        lines = file.readlines()
        for line in lines:
            line = (line.replace(b"\n", b""))
            en_line.append(Fernet(key).encrypt(line))
        file.close()
    with open("passwr.txt", "wb") as file:
        for e in en_line:
            file.write(e + b"\n")
        file.close()


# encrypt()

#####################################decryption of corrupted file
def decrypt():
    with open("passwr.txt", "rb") as file:
        lines = (file.readlines())
        for line in lines:
            line = (line.replace(b"\n", b""))
            de_line.append(Fernet(key).decrypt(line))
        file.close()
    with open("passwr.txt", "wb") as wrfile:
        for d in de_line:
            wrfile.write(d)
        wrfile.close()


def add_password(id, pas, what):
    global de_line
    decrypt()
    with open("passwr.txt", "r") as wfile:
        f = json.loads(wfile.read())
        f = dict(f)
        f[f"{what}"] = {f"{id}": f"{pas}"}  # adding new password
        with open("passwr.txt", "w") as file:
            file.write(json.dumps(f))
            file.close()
            wfile.close()
    encrypt()


def read_password(what):
    decrypt()
    with open("passwr.txt", "r") as file:
        f = (json.loads(file.read()))
        f = dict(f)
        for ac, id_pass in dict(f).items():
            if what == ac:
                for id, pas in dict(id_pass).items():
                    # print(f"your id is {id} , your pass is {pas}")
                    # copy id and pass to clipboard
                    pyperclip.copy(f"{id}:{pas}")
                    speak("id and pass copied to clipboard")
    encrypt()


def callto(name):
    import pyautogui as pg
    from pywinauto import Application
    open_applications("open app phone link")
    time.sleep(7)

    app = Application(backend="uia").connect(title="Phone Link", timeout=3000)
    time.sleep(2)
    but = app.PhoneLink.child_window(best_match="TabItem", auto_id="CallingNodeAutomationId",
                                     control_type="TabItem").wrapper_object()
    time.sleep(5)
    but.click_input()
    app.PhoneLink.child_window(auto_id="TextBox", control_type="Edit").wrapper_object().type_keys(name)
    time.sleep(2)
    pg.press("enter")
    time.sleep(2)
    # app.PhoneLink.print_control_identifiers()
    app.PhoneLink.child_window(best_match="Button50", auto_id="ButtonCall",
                               control_type="Button").wrapper_object().click_input()


# callto("shirish")
# reading reminder
# list
def remainder():
    speak("What is the reminder?")
    data = test_recogniser()
    speak("You said to remember that " + data)
    reminder_file = open("data.txt", 'a')
    reminder_file.write('\n')
    reminder_file.write(data)
    reminder_file.close()


def say_remember():
    reminder_file = open("data.txt", 'r')
    speak("You said me to remember that: " + reminder_file.read())


def del_rem():
    reminder_file = open("data.txt", 'w')
    reminder_file.write('')
    reminder_file.close()


# changing voice
def voice_change(q):
    engine.setProperty('voice', voices[q].id)


def change_voice():
    speak("for female say female and, for male say male")
    q = test_recogniser()
    if "female" in q:
        voice_change(1)
    elif "male" in q:
        voice_change(0)


def day():
    day = datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)


def translate():
    from googletrans import Translator
    translator = Translator()
    speak("what do you want to translate?")
    query = test_recogniser()
    speak("To which language do you want to translate?")
    lang = test_recogniser()
    if "english" in lang:
        lang = "en"
    elif "hindi" in lang:
        lang = "hi"
    elif "french" in lang:
        lang = "fr"
    elif "german" in lang:
        lang = "de"
    elif "italian" in lang:
        lang = "it"
    elif "spanish" in lang:
        lang = "es"
    elif "japanese" in lang:
        lang = "ja"
    elif "korean" in lang:
        lang = "ko"
    elif "russian" in lang:
        lang = "ru"
    elif "chinese" in lang:
        lang = "zh-cn"
    elif "arabic" in lang:
        lang = "ar"
    elif "turkish" in lang:
        lang = "tr"
    elif "portuguese" in lang:
        lang = "pt"
    elif "dutch" in lang:
        lang = "nl"
    elif "greek" in lang:
        lang = "el"
    elif "swedish" in lang:
        lang = "sv"
    elif "norwegian" in lang:
        lang = "no"
    elif "danish" in lang:
        lang = "da"
    elif "finnish" in lang:
        lang = "fi"
    elif "polish" in lang:
        lang = "pl"
    elif "czech" in lang:
        lang = "cs"
    elif "romanian" in lang:
        lang = "ro"
    elif "slovak" in lang:
        lang = "sk"
    elif "slovenian" in lang:
        lang = "sl"
    elif "albanian" in lang:
        lang = "sq"
    elif "bulgarian" in lang:
        lang = "bg"
    elif "catalan" in lang:
        lang = "ca"
    elif "croatian" in lang:
        lang = "hr"
    elif "estonian" in lang:
        lang = "et"
    elif "galician" in lang:
        lang = "gl"
    translation = translator.translate(query, dest=lang, src="en")
    speak(translation.pronunciation)


# import cv2
from ffpyplayer.player import MediaPlayer
import pyautogui as pg
import ctypes


def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap


def running_videos(sourcePath):
    # Get the window size and calculate the center
    user32 = ctypes.windll.user32
    win_x, win_y = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    win_cnt_x, win_cnt_y = [user32.GetSystemMetrics(0) / 2, user32.GetSystemMetrics(1) / 2]
    camera = getVideoSource(sourcePath, 1519, 754)
    player = MediaPlayer(sourcePath)

    while True:
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            break

        frame = cv2.resize(frame, (win_x, win_y))
        cv2.imshow('', frame)
        # make full screen
        # cv2.moveWindow('Camera', 0, 0)
        # cv2.setWindowProperty('Camera', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        # if val != 'eof' and audio_frame is not None:
        # frame, t = audio_frame
        # print("Frame:" + str(frame) + " T: " + str(t))

    camera.release()
    cv2.destroyAllWindows()


def sleepjarvis():
    while True:
        wakeword = test_recogniser()
        if "wake up" in wakeword or "jarvis" in wakeword:
            break


def iot(query):
    if "bed light" in query and "on" in query:
        speak("Turning on the bed light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v1=1")
    elif "bed light" in query and "off" in query:
        speak("Turning off the bed light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v1=0")

    if "bedlight" in query and "on" in query:
        speak("Turning on the bed light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v1=1")
    elif "bedlight" in query and "off" in query:
        speak("Turning off the bed light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v1=0")

    if "room light" in query and "on" in query:
        speak("Turning on the room light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v2=1")
    elif "room light" in query and "off" in query:
        speak("Turning off the room light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v2=0")

    if "roomlight" in query and "on" in query:
        speak("Turning on the room light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v2=1")
    elif "roomlight" in query and "off" in query:
        speak("Turning off the room light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v2=0")

    if "flashlight" in query and "on" in query:
        speak("Turning on the flash light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v3=1")
    elif "flashlight" in query and "off" in query:
        speak("Turning off the flash light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v3=0")

    if "flash light" in query and "on" in query:
        speak("Turning on the flash light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v3=1")
    elif "flash light" in query and "off" in query:
        speak("Turning off the flash light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v3=0")

    if "all light" in query and "on" in query:
        speak("Turning on the all light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v2=1")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v1=1")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v3=1")

    elif "all light" in query and "off" in query:
        speak("Turning off the all light")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v2=0")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v1=0")
        requests.get("https://blr1.blynk.cloud/external/api/update?token=dqiw4Io1MRlBIVWuK3e9rlZLK3ZFsh3F&v3=0")


import openai
from dotenv import load_dotenv

openai.api_key = ""
load_dotenv()


# completion = openai.completion()
def ReplyBrain(question, chat_log=None):
    Filelog = open(r"E:\OPEN AI\chatlog.txt", "r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template
    # print("chatlog emp::",chat_log)
    prompt = f'{chat_log}\nyou:{question}\nJarvis:'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou:{question} \njarvis:{answer}"
    FileLog = open(r"E:\OPEN AI\chatlog.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer


# ------------------------------------------------------------------------------------animation function start here
#
# haiv=0
# def hai():
#     global haiv
#     if haiv==0:
#         anima.animations["hai"] = FrameAnimation3d('SIGMA/obj2/untitled', fps=35, loop=True, autoplay=True, scale=200,texture='SIGMA/maps/42.png', position=(2, 0, 2))
#         haiv=1
#     setting_state( 'hai')
#
# dancev=0
# def dance():
#     global dancev
#     if dancev==0:
#         anima.animations['Dance'] = FrameAnimation3d('SIGMA/Dance/Dance', fps=35, loop=False, autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#         position=(2, 0, 2))
#         dancev=1
#     setting_state( 'Dance')
#
#
# firstv = 0
# def first():
#     global firstv
#     if firstv == 0:
#         anima.animations['03'] = FrameAnimation3d('SIGMA/03/03', fps=35, loop=False, autoplay=True, scale=200,
#                                                   texture='SIGMA/maps/42.png',
#                                                   position=(2, 0, 2))
#         firstv = 1
#     setting_state( '03')
#
# ArmmStrctigv = 0
# def ArmmStrctig():
#     global ArmmStrctigv
#     if ArmmStrctigv == 0:
#         anima.animations['Armm Strctig'] = FrameAnimation3d('SIGMA/Armm Strctig/Armm Strctig', fps=35, loop=False,
#                                                         autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                         position=(2, 0, 2))
#         ArmmStrctigv = 1
#     setting_state( 'Armm Strctig')
#
# Dancev = 0
# def Dance():
#     global Dancev
#     if Dancev == 0:
#         anima.animations['Dance'] = FrameAnimation3d('SIGMA/Dance/Dance', fps=35, loop=False, autoplay=True, scale=200,
#                                                      texture='SIGMA/maps/42.png',
#                                                      position=(2, 0, 2))
#         Dancev = 1
#     setting_state( 'Dance')
#
# Dyingv = 0
# def Dying():
#     global Dyingv
#     if Dyingv == 0:
#         anima.animations['Dying'] = FrameAnimation3d('SIGMA/Dying/Dying', fps=35, loop=False, autoplay=True, scale=200,
#                                                      texture='SIGMA/maps/42.png',
#                                                      position=(2, 0, 2))
#         Dyingv = 1
#     setting_state( 'Dying')
#
# Entryv = 0
# def Entry():
#     global Entryv
#     if Entryv == 0:
#         anima.animations['Entry'] = FrameAnimation3d('SIGMA/Entry/Entry', fps=35, loop=False, autoplay=True, scale=200,
#                                                      texture='SIGMA/maps/42.png',
#                                                      position=(2, 0, 2))
#         Entryv = 1
#     setting_state( 'Entry')
#
# Fallingv = 0
# def Falling():
#     global Fallingv
#     if Fallingv == 0:
#         anima.animations['Falling'] = FrameAnimation3d('SIGMA/Falling/Falling', fps=35, loop=False, autoplay=True,
#                                                        scale=200, texture='SIGMA/maps/42.png',
#                                                        position=(2, 0, 2))
#         Fallingv = 1
#     setting_state( 'Falling')
#
# Flairv = 0
# def Flair():
#     global Flairv
#     if Flairv == 0:
#         anima.animations['Flair'] = FrameAnimation3d('SIGMA/Flair/Flair', fps=35, loop=False, autoplay=True, scale=200,
#                                                      texture='SIGMA/maps/42.png',
#                                                      position=(2, 0, 2))
#         Flairv = 1
#     setting_state( 'Flair')
#
# IDLEv = 0
# def IDLE():
#     global IDLEv
#     if IDLEv == 0:
#         anima.animations['IDLE'] = FrameAnimation3d('SIGMA/IDLE/IDLE', fps=35, loop=False, autoplay=True, scale=200,
#                                                     texture='SIGMA/maps/42.png',
#                                                     position=(2, 0, 2))
#         IDLEv = 1
#     setting_state( 'IDLE')
#
# LIDLEv = 0
# def LIDLE():
#     global LIDLEv
#     if LIDLEv == 0:
#         anima.animations['L IDLE'] = FrameAnimation3d('SIGMA/L IDLE/L IDLE', fps=35, loop=False, autoplay=True, scale=200,
#                                                   texture='SIGMA/maps/42.png',
#                                                   position=(2, 0, 2))
#         LIDLEv = 1
#     setting_state( 'L IDLE')
#
# NerviouslyLookingAroundv = 0
# def NerviouslyLookingAround():
#     global NerviouslyLookingAroundv
#     if NerviouslyLookingAroundv == 0:
#         anima.animations['Nerviously Looking Around'] = FrameAnimation3d(
#         'SIGMA/Nerviously Looking Around/Nerviously Looking Around', fps=35, loop=False, autoplay=True, scale=200,
#         texture='SIGMA/maps/42.png',
#         position=(2, 0, 2))
#         NerviouslyLookingAroundv = 1
#     setting_state( 'Nerviously Looking Around')
#
# obj2v = 0
# def obj2():
#     global obj2v
#     if obj2v == 0:
#         anima.animations['obj2'] = FrameAnimation3d('SIGMA/obj2/obj2', fps=35, loop=False, autoplay=True, scale=200,
#                                                     texture='SIGMA/maps/42.png',
#                                                     position=(2, 0, 2))
#         obj2v = 1
#     setting_state( 'obj2')
#
# Phonev = 0
# def Phone():
#     global Phonev
#     if Phonev == 0:
#         anima.animations['Phone'] = FrameAnimation3d('SIGMA/Phone/Phone', fps=35, loop=False, autoplay=True, scale=200,
#                                                      texture='SIGMA/maps/42.png',
#                                                      position=(2, 0, 2))
#         Phonev = 1
#     setting_state( 'Phone')
#
#
# PointigForwardv = 0
# def PointigForward():
#     global PointigForwardv
#     if PointigForwardv == 0:
#         anima.animations['Pointig Forward'] = FrameAnimation3d('SIGMA/Pointig Forward/Pointig Forward', fps=35, loop=False,
#                                                            autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                            position=(2, 0, 2))
#         PointigForwardv = 1
#     setting_state( 'Pointig Forward')
# Prayingv = 0
# def Praying():
#     global Prayingv
#     if Prayingv == 0:
#         anima.animations['Praying'] = FrameAnimation3d('SIGMA/Praying/Praying', fps=35, loop=False, autoplay=True,
#                                                        scale=200, texture='SIGMA/maps/42.png',
#                                                        position=(2, 0, 2))
#         Prayingv = 1
#     setting_state( 'Praying')
#
# SititngClapv = 0
# def SititngClap():
#     global SititngClapv
#     if SititngClapv == 0:
#         anima.animations['Sititng Clap'] = FrameAnimation3d('SIGMA/Sititng Clap/Sititng Clap', fps=35, loop=False,
#                                                         autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                         position=(2, 0, 2))
#         SititngClapv = 1
#     setting_state( 'Sititng Clap')
#
# SititngTalkingv = 0
# def SititngTalking():
#     global SititngTalkingv
#     if SititngTalkingv == 0:
#         anima.animations['Sititng Talking'] = FrameAnimation3d('SIGMA/Sititng Talking/Sititng Talking', fps=35, loop=False,
#                                                            autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                            position=(2, 0, 2))
#         SititngTalkingv = 1
#     setting_state( 'Sititng Talking')
#
# Standingv = 0
# def Standing():
#     global Standingv
#     if Standingv == 0:
#             anima.animations['Standing'] = FrameAnimation3d('SIGMA/Standing/Standing', fps=35, loop=False, autoplay=True,
#                                                         scale=200, texture='SIGMA/maps/42.png',
#                                                         position=(2, 0, 2))
#             Standingv = 1
#     setting_state( 'Standing')
#
# StandingClApv = 0
# def StandingClAp():
#     global StandingClApv
#     if StandingClApv == 0:
#         anima.animations['Standing ClAp'] = FrameAnimation3d('SIGMA/Standing ClAp/Standing ClAp', fps=35, loop=False,
#                                                          autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                          position=(2, 0, 2))
#         StandingClApv = 1
#     setting_state( 'Standing ClAp')
#
# StandingJumpv = 0
# def StandingJump():
#     global StandingJumpv
#     if StandingJumpv == 0:
#         anima.animations['Standing Jump'] = FrameAnimation3d('SIGMA/Standing Jump/Standing Jump', fps=35, loop=False,
#                                                          autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                          position=(2, 0, 2))
#         StandingJumpv = 1
#     setting_state( 'Standing Jump')
#
# Thankfulv = 0
# def Thankful():
#     global Thankfulv
#     if Thankfulv == 0:
#         anima.animations['Thankful'] = FrameAnimation3d('SIGMA/Thankful/Thankful', fps=35, loop=False, autoplay=True,
#                                                         scale=200, texture='SIGMA/maps/42.png',
#                                                         position=(2, 0, 2))
#         Thankfulv = 1
#     setting_state( 'Thankful')
#
# Thinkingv = 0
# def Thinking():
#     global Thinkingv
#     if Thinkingv == 0:
#         anima.animations['Thinking'] = FrameAnimation3d('SIGMA/Thinking/Thinking', fps=35, loop=False, autoplay=True,
#                                                         scale=200, texture='SIGMA/maps/42.png',
#                                                         position=(2, 0, 2))
#         Thinkingv = 1
#     setting_state( 'Thinking')
#
# Walkingv = 0
#
#
# def Walking():
#     global Walkingv
#     if Walkingv == 0:
#         anima.animations['Walking'] = FrameAnimation3d('SIGMA/Walking/Walking', fps=35, loop=False, autoplay=True,
#                                                        scale=200, texture='SIGMA/maps/42.png',
#                                                        position=(2, 0, 2))
#         Walkingv = 1
#     setting_state( 'Walking')
#
# WaveHIPHOPv = 0
# def WaveHIPHOP():
#     global WaveHIPHOPv
#     if WaveHIPHOPv == 0:
#         anima.animations['Wave HIP HOP'] = FrameAnimation3d('SIGMA/Wave HIP HOP/Wave HIP HOP', fps=35, loop=True,
#                                                         autoplay=True, scale=200, texture='SIGMA/maps/42.png',
#                                                         position=(2, 0, 2))
#         WaveHIPHOPv = 1
#     setting_state( 'Wave HIP HOP')
#
#
# WOBLINGv = 0
# def WOBLING():
#     global WOBLINGv
#     if WOBLINGv == 0:
#         anima.animations['WOBLING'] = FrameAnimation3d('SIGMA/WOBLING/WOBLING', fps=35, loop=False, autoplay=True,
#                                                        scale=200, texture='SIGMA/maps/42.png',
#                                                        position=(2, 0, 2))
#     WOBLINGv = 1
#     setting_state( 'WOBLING')
#
# def setting_state(stname):
#     anima.state= stname

def person_detection():
    detection()


def finish():
    playsound(r"finishing.wav")


# iot("on")
time.sleep(3)
