# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'original.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Jarvis(object):
    def setupUi(self, Jarvis):
        Jarvis.setObjectName("Jarvis")
        Jarvis.resize(1257, 830)
        Jarvis.setFixedSize(1257, 830)
        self.centralwidget = QtWidgets.QWidget(Jarvis)
        self.centralwidget.setObjectName("centralwidget")
        self.blackbg = QtWidgets.QLabel(self.centralwidget)
        self.blackbg.setGeometry(QtCore.QRect(-50, -180, 1701, 1181))
        self.blackbg.setStyleSheet("background-color:black\n"
                                   "\n"
                                   "\n"
                                   "")
        self.blackbg.setScaledContents(True)
        self.blackbg.setObjectName("blackbg")
        self.mironman = QtWidgets.QLabel(self.centralwidget)
        self.mironman.setGeometry(QtCore.QRect(270, 50, 661, 431))
        self.mironman.setText("")
        self.mironman.setPixmap(QtGui.QPixmap(
            r"E:\project\gui files\oie_oie_overlay.gif"))  # "gui files/oie_oie_overlay.gif"))
        self.mironman.setScaledContents(True)
        self.mironman.setObjectName("mironman")
        self.initiatingsystem = QtWidgets.QLabel(self.centralwidget)
        self.initiatingsystem.setGeometry(QtCore.QRect(0, -10, 381, 191))
        self.initiatingsystem.setText("")
        self.initiatingsystem.setPixmap(QtGui.QPixmap(r"E:\project\gui files\initial.gif"))
        self.initiatingsystem.setScaledContents(True)
        self.initiatingsystem.setObjectName("initiatingsystem")
        self.datebackground = QtWidgets.QLabel(self.centralwidget)
        self.datebackground.setGeometry(QtCore.QRect(60, 460, 221, 71))
        self.datebackground.setStyleSheet("background-color:white")
        self.datebackground.setText("")
        self.datebackground.setPixmap(QtGui.QPixmap(r"E:\project\gui files\gggf.jpg"))
        self.datebackground.setScaledContents(True)
        self.datebackground.setObjectName("datebackground")
        self.timebg = QtWidgets.QLabel(self.centralwidget)
        self.timebg.setGeometry(QtCore.QRect(110, 560, 231, 71))
        self.timebg.setText("")
        self.timebg.setPixmap(QtGui.QPixmap(r"E:\project\gui files\gggf.jpg"))
        self.timebg.setScaledContents(True)
        self.timebg.setObjectName("timebg")
        self.corner2 = QtWidgets.QLabel(self.centralwidget)
        self.corner2.setGeometry(QtCore.QRect(1020, 40, 201, 141))
        self.corner2.setText("")
        self.corner2.setPixmap(QtGui.QPixmap(r"E:\project\gui files\actual.gif"))
        self.corner2.setScaledContents(True)
        self.corner2.setObjectName("corner2")
        self.corner1 = QtWidgets.QLabel(self.centralwidget)
        self.corner1.setGeometry(QtCore.QRect(780, 40, 201, 141))
        self.corner1.setText("")
        self.corner1.setPixmap(QtGui.QPixmap(r"E:\project\gui files\Jarvis_Gui (2).gif"))
        self.corner1.setScaledContents(True)
        self.corner1.setObjectName("corner1")
        self.startlbl = QtWidgets.QLabel(self.centralwidget)
        self.startlbl.setGeometry(QtCore.QRect(930, 420, 231, 81))
        self.startlbl.setText("")
        self.startlbl.setPixmap(QtGui.QPixmap(r"E:\project\gui files\Start.png"))
        self.startlbl.setScaledContents(True)
        self.startlbl.setObjectName("startlbl")
        self.quitlbl = QtWidgets.QLabel(self.centralwidget)
        self.quitlbl.setGeometry(QtCore.QRect(900, 530, 231, 71))
        self.quitlbl.setText("")
        self.quitlbl.setPixmap(QtGui.QPixmap(r"E:\project\gui files\Quit.png"))
        self.quitlbl.setScaledContents(True)
        self.quitlbl.setObjectName("quitlbl")
        self.datetext = QtWidgets.QTextBrowser(self.centralwidget)
        self.datetext.setGeometry(QtCore.QRect(80, 470, 181, 51))
        self.datetext.setStyleSheet("background:transparent;\n"
                                    "border:1;\n"
                                    "border:1;\n"
                                    "font-size:30px;\n"
                                    "color:#50ecde;")
        self.datetext.setObjectName("datetext")
        self.timetext = QtWidgets.QTextBrowser(self.centralwidget)
        self.timetext.setGeometry(QtCore.QRect(130, 570, 191, 51))
        self.timetext.setStyleSheet("background:transparent;\n"
                                    "border:none;\n"
                                    "font-size:30px;\n"
                                    "color:#50ecde;")
        self.timetext.setObjectName("timetext")
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn.setGeometry(QtCore.QRect(940, 440, 211, 51))
        self.startbtn.setStyleSheet("background:transparent;\n"
                                    "border:none;")
        self.startbtn.setText("")
        self.startbtn.setObjectName("startbtn")
        self.startbtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn_2.setGeometry(QtCore.QRect(910, 540, 211, 51))
        self.startbtn_2.setStyleSheet("background:transparent;\n"
                                      "border:none;")
        self.startbtn_2.setText("")
        self.startbtn_2.setObjectName("startbtn_2")
        self.downeye = QtWidgets.QLabel(self.centralwidget)
        self.downeye.setGeometry(QtCore.QRect(440, 450, 341, 181))
        self.downeye.setText("")
        self.downeye.setTextFormat(QtCore.Qt.MarkdownText)
        self.downeye.setPixmap(QtGui.QPixmap(r"E:\project\gui files\Aqua.gif"))
        self.downeye.setScaledContents(True)
        self.downeye.setObjectName("downeye")
        self.earthlbl = QtWidgets.QLabel(self.centralwidget)
        self.earthlbl.setGeometry(QtCore.QRect(30, 280, 281, 171))
        self.earthlbl.setText("")
        self.earthlbl.setPixmap(QtGui.QPixmap(r"E:\project\gui files\Earth.gif"))
        self.earthlbl.setScaledContents(True)
        self.earthlbl.setObjectName("earthlbl")
        self.trigif = QtWidgets.QLabel(self.centralwidget)
        self.trigif.setGeometry(QtCore.QRect(870, 240, 281, 171))
        self.trigif.setText("")
        self.trigif.setPixmap(QtGui.QPixmap(r"E:\project\gui files\program_load.gif"))
        self.trigif.setScaledContents(True)
        self.trigif.setObjectName("trigif")
        self.liestening = QtWidgets.QLabel(self.centralwidget)
        self.liestening.setEnabled(True)
        self.liestening.setGeometry(QtCore.QRect(470, 460, 281, 191))
        self.liestening.setText("")
        self.liestening.setPixmap(QtGui.QPixmap(r"E:\project\gui files\listeningGIF.gif"))
        self.liestening.setScaledContents(True)
        self.liestening.setObjectName("liestening")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 140, 201, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"E:\project\gui files\Code_Template.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.yousaidbg = QtWidgets.QLabel(self.centralwidget)
        self.yousaidbg.setGeometry(QtCore.QRect(290, 670, 691, 81))
        self.yousaidbg.setText("")
        self.yousaidbg.setPixmap(QtGui.QPixmap(r"E:\project\gui files\gggf.jpg"))
        self.yousaidbg.setScaledContents(True)
        self.yousaidbg.setObjectName("yousaidbg")
        self.yousaidtxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.yousaidtxt.setGeometry(QtCore.QRect(330, 690, 591, 51))
        self.yousaidtxt.setStyleSheet("background:transparent;\n"
                                      "border:none;\n"
                                      "border:1;\n"
                                      "font-size:30px;\n"
                                      "color:#50ecde;")
        self.yousaidtxt.setObjectName("yousaidtxt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 290, 1061, 361))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"E:\project\gui files\loading_1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.blackbg.raise_()
        self.corner2.raise_()
        self.initiatingsystem.raise_()
        self.datebackground.raise_()
        self.downeye.raise_()
        self.timebg.raise_()
        self.timetext.raise_()
        self.datetext.raise_()
        self.startlbl.raise_()
        self.quitlbl.raise_()
        self.earthlbl.raise_()
        self.trigif.raise_()
        self.liestening.raise_()
        self.mironman.raise_()
        self.startbtn.raise_()
        self.startbtn_2.raise_()
        self.corner1.raise_()
        self.label.raise_()
        self.yousaidbg.raise_()
        self.yousaidtxt.raise_()
        Jarvis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Jarvis)
        self.statusbar.setObjectName("statusbar")
        Jarvis.setStatusBar(self.statusbar)

        self.retranslateUi(Jarvis)
        QtCore.QMetaObject.connectSlotsByName(Jarvis)

    def retranslateUi(self, Jarvis):
        _translate = QtCore.QCoreApplication.translate
        Jarvis.setWindowTitle(_translate("Jarvis", "MainWindow"))
        self.blackbg.setText(_translate("Jarvis", "TextLabel"))
        self.datetext.setHtml(_translate("Jarvis",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#409491;\">DATE</span></p></body></html>"))
        self.timetext.setHtml(_translate("Jarvis",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#409491;\">TIME</span></p></body></html>"))
        self.yousaidtxt.setHtml(_translate("Jarvis",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#409491;\">QUERY</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Jarvis = QtWidgets.QMainWindow()
    ui = Ui_Jarvis()
    ui.setupUi(Jarvis)
    Jarvis.show()
    sys.exit(app.exec_())
