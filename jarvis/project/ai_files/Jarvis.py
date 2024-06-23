import json
import random
import sys
import time
from datetime import datetime

import recogniser
import torch
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from ai_files.Brain import NeuralNet
from ai_files.NeuralNetwork import bag_of_words, tokenize
from ai_files.animate import *
# from PyQt5.uic import loadUiType
from interface import *
from interface import Ui_Jarvis
from face_recognition import Face_recognition
from jarvis_password import passwordprotect
from offline import offlinefunc
from online import mainfunc
# import numpy
from recogniser import speak

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
with open(r"intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "../ai_files/TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

from functions import running_videos

# /|\ ,setting_state

running_videos(r"C:\Users\arige\OneDrive\Desktop\intro.mp4")
time.sleep(3)
running_videos(r"C:\Users\arige\OneDrive\Desktop\sintro.mp4")
# --------------------------------------------------------
testt = " "
Name = "Jarvis"
# os.system("taskkill /f /t /im explorer.exe")
speak("starting face recognition.")
if Face_recognition.reco():
    pass
elif passwordprotect():
    pass
else:
    sys.exit(0)
# os.system("start explorer.exe")
# os.startfile("explorer.exe")
speak("system loading")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Main()

    def Main(self):
        while True:
            # setting_state('L IDLE')
            jarvis.ui.liestening.setVisible(True)
            self.sentence = recogniser.test_recogniser()
            jarvis.ui.liestening.setVisible(False)
            # setting_state('Thinking')
            self.result = str(self.sentence)
            global testt
            testt = self.result

            if "bye" in self.sentence or "exit" == self.sentence:
                exit(0)
            if "" == self.sentence or " " == self.sentence:
                pass
            else:
                self.sentence = tokenize(self.sentence)

                X = bag_of_words(self.sentence, all_words)
                X = X.reshape(1, X.shape[0])
                X = torch.from_numpy(X).to(device)

                output = model(X)

                _, predicted = torch.max(output, dim=1)

                tag = tags[predicted.item()]

                probs = torch.softmax(output, dim=1)
                prob = probs[0][predicted.item()]

                if prob.item() > 0.75:

                    for intent in intents['intents']:
                        if tag == intent["tag"]:
                            reply = random.choice(intent["responses"])
                            if "offline" in reply:
                                try:
                                    offlinefunc(tag, self.result)
                                except Exception as e:
                                    speak(e)
                            elif "online" in reply:
                                try:
                                    mainfunc(tag, self.result)
                                except Exception as e:
                                    speak(e)
                            else:
                                recogniser.speak(reply)
                                reply = " "
                            tag = ""
                            reply = ""
                self.sentence = ""

                time.sleep(1)
                # anima.state='L IDLE'


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Jarvis()
        self.ui.setupUi(self)
        # self.liestening.setHidden(True)
        self.ui.startbtn.clicked.connect(self.startTask)
        self.ui.startbtn_2.clicked.connect(self.closeTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\oie_oie_overlay.gif")
        self.ui.mironman.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\initial.gif")
        self.ui.initiatingsystem.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\Jarvis_Gui (2).gif")
        self.ui.corner1.setMovie(self.ui.movie)
        self.ui.movie.start()
        # self.ui.movie = QtGui.QMovie("project/gui files/jarvis_jj.gif")
        # self.ui.rightjarvis.setMovie(self.ui.movie)
        # self.ui.movie.start()
        # self.ui.movie = QtGui.QMovie("project/gui files/Siri_1.gif")
        # self.ui.siri.setMovie(self.ui.movie)
        # self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\oct12.gif")
        self.ui.trigif.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\actual.gif")
        self.ui.corner2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\listeningGIF.gif")
        self.ui.liestening.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.liestening.setVisible(False)
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\Aqua.gif")
        self.ui.downeye.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"E:\project\gui files\Earth.gif")
        self.ui.earthlbl.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        timetext1 = now.toString(Qt.ISODate)
        m = "am" if datetime.now().hour < 12 else "pm"
        h = (datetime.now().hour % 12)
        mi = datetime.now().minute
        if h == 0:
            h = 12
        datetext1 = f"{str(h)}:{str(mi)} {m}"
        self.ui.datetext.setText(datetext1)
        self.ui.yousaidtxt.setText("you said:" + testt)
        self.ui.timetext.setText(timetext1)

    def closeTask(self):
        exit(0)


app = QApplication(sys.argv)

jarvis = Main()
jarvis.show()
# anima.state='walking'
# uapp.run()
exit(app.exec_())
# while True:
#     Main()
