from sources import globals

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys



from kocaYusuf import Worker

class Ui_MainWindow(object):
    def ultraInstinctCheck(self):
        if (globals.pause_flag1 and globals.pause_flag2 and globals.pause_flag3 and globals.pause_flag4 and globals.pause_flag5):
            print("ULTRA INSTINCT")
            MainWindow.setStyleSheet("background-image: url(:/newPrefix/ultrabeeg.jpeg);")
        else:
            MainWindow.setStyleSheet("background-image: url(:/newPrefix/beeg.jpg);")

    def returnString(self, flag):
        if flag:
            return "image: url(:/newPrefix/flagGreenturkey.png);background-image: url(:/newPrefix/dark.jpg);" # Green
        else:
            return "image: url(:/newPrefix/220px-Flag_of_Turkey.jpg);background-image: url(:/newPrefix/dark.jpg);" #Red

    def updateButtons(self):
        self.pushButton_3.setStyleSheet(self.returnString(globals.pause_flag1))
        self.pushButton_4.setStyleSheet(self.returnString(globals.pause_flag2))
        self.pushButton_6.setStyleSheet(self.returnString(globals.pause_flag3))
        self.pushButton_7.setStyleSheet(self.returnString(globals.pause_flag4))
        self.pushButton_8.setStyleSheet(self.returnString(globals.pause_flag5))
        self.ultraInstinctCheck()

    def wallhack(self):
        print("wallhack")
        globals.pause_flag1 = not globals.pause_flag1
        self.updateButtons()

    def noflash(self):
        print("noflash")
        globals.pause_flag2 = not globals.pause_flag2
        self.updateButtons()

    def radar(self):
        print("radar")
        globals.pause_flag3 = not globals.pause_flag3
        self.updateButtons()

    def bhop(self):
        print("bhop")
        globals.pause_flag4 = not globals.pause_flag4
        self.updateButtons()

    def trigger(self):
        print("trigger")
        globals.pause_flag5 = not globals.pause_flag5
        self.updateButtons()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 429)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/beeg.jpg);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(530, 0, 141, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.wallhack)
        self.pushButton_3.setFont(font)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(530, 70, 141, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.noflash)
        self.pushButton_4.setFont(font)

        self.pushButton_6 =QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(530, 140, 141, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.radar)
        self.pushButton_6.setFont(font)

        self.pushButton_7 =QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QRect(530, 210, 141, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.bhop)
        self.pushButton_7.setFont(font)

        self.pushButton_8 =QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QRect(530, 280, 141, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.trigger)
        self.pushButton_8.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar =QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 736, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar =QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.updateButtons()
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Koca yusuf2 (weak version)"))
        self.pushButton_3.setText(_translate("MainWindow", "Wallhack"))
        self.pushButton_4.setText(_translate("MainWindow", "NoFlash"))
        self.pushButton_6.setText(_translate("MainWindow", "RadarHack"))
        self.pushButton_7.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_8.setText(_translate("MainWindow", "Trigger"))

    def __init__(self, *args, **kwargs):
        print("Window started")
        worker = Worker()
        self.threadpool = QThreadPool()
        self.threadpool.start(worker)

from GUI import ui_resource_rc

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())