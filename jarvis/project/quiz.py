import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import requests

from recogniser import speak

point = 0
page = []
crcansw = []
crindex = []
optioni = 0
speak("how many questions do you need?::")
questions = str(5)  # test_recogniser()
questions = questions.replace("questions", "").replace("question", "")
questions = int(questions)
raw = requests.get(
    "https://the-trivia-api.com/api/questions?limit=" + str(
        questions) + "&region=IN&difficulty=medium").json()
# print(raw)
window = tk.Tk()
window.title("Quiz Game")
window.geometry("500x200")


def check(option, croption, butname):
    global point
    global optioni
    if croption[optioni] == option:
        point += 1
        print("correct")
    else:
        print("wrong")
    messagebox.showinfo("The correct answer is ", butname[optioni])
    optioni += 1
    print(butname)
    move_next_page()


# main_frame = tk.Frame(window)

for i in range(0, questions):
    frame1 = tk.Frame(window)
    label = ttk.Label(frame1, text="category:" + raw[i]['category'])
    label1 = ttk.Label(frame1, text=f"{i + 1}.{raw[i]['question']}", font=("Arial", 12), background="black",
                       foreground="white")
    label.pack()
    label1.pack()
    lis = raw[i]["incorrectAnswers"]
    i = random.randint(0, 2)
    lis.insert(i, raw[i]["correctAnswer"])
    # print(raw[i]["correctAnswer"])
    crindex.append(i + 1)
    crcansw.append(raw[i]["correctAnswer"])
    # print(crindex)
    button1 = ttk.Button(frame1, text=f"{1}.{lis[0]}", width=20, command=lambda: check(1, crindex, crcansw))
    button1.pack()
    button2 = ttk.Button(frame1, text=f"{2}.{lis[1]}", width=20, command=lambda: check(2, crindex, crcansw))
    button2.pack()
    button3 = ttk.Button(frame1, text=f"{3}.{lis[2]}", width=20, command=lambda: check(3, crindex, crcansw))
    button3.pack()
    button4 = ttk.Button(frame1, text=f"{4}.{lis[3]}", width=20, command=lambda: check(4, crindex, crcansw))
    button4.pack()
    labelc = ttk.Label(frame1, text="")
    page.append(frame1)

page[0].pack()

count = 0


def move_next_page():
    global count
    if not count > len(page):
        print("count and page", count, page)
        for p in page:
            p.pack_forget()
        count += 1
        try:
            pages = page[count]
            pages.pack()
        except Exception as e:
            print(e)
            window.destroy()


window.mainloop()
speak("your score is " + str(point))
