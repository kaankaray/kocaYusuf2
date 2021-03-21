from sources import globals
from sources.imports import *
from kocaYusuf import Worker

class Ui_MainWindow(object):

    def isCSGORunningCheck(self, flag):
        _translate = QCoreApplication.translate
        if flag:
            self.label.setText(_translate("MainWindow", "Bam bam"))
            self.label.setStyleSheet("QLabel {  color : green; }")
        else:
            self.label.setText(_translate("MainWindow", "CS:GO is not running"))
            self.label.setStyleSheet("QLabel {  color : red; }")

    def ultraInstinctCheck(self):
        if (globals.pause_flag1 and globals.pause_flag2 and globals.pause_flag3 and globals.pause_flag4 and globals.pause_flag5):
            print("ULTRA INSTINCT")
            #QWidget#centralwidget{image: url(:/newPrefix/beeg.jpg);}\n
            MainWindow.setStyleSheet("QWidget#centralwidget{image: url(:/newPrefix/ultrabeeg.jpeg);}")
        else:
            MainWindow.setStyleSheet("QWidget#centralwidget{image: url(:/newPrefix/beeg.jpg);}")

    def returnString(self, flag):
        if flag:
            return "background-image: url(:/newPrefix/flagGreenturkey.png);" # Green
        else:
            return "background-image: url(:/newPrefix/flag.png);" #Red

    def updateButtons(self):
        self.pushButton_1.setStyleSheet(self.returnString(globals.pause_flag1))
        self.pushButton_2.setStyleSheet(self.returnString(globals.pause_flag2))
        self.pushButton_3.setStyleSheet(self.returnString(globals.pause_flag3))
        self.pushButton_4.setStyleSheet(self.returnString(globals.pause_flag4))
        self.pushButton_5.setStyleSheet(self.returnString(globals.pause_flag5))
        self.ultraInstinctCheck()

    def addButtonActions(self):
        self.pushButton_1.clicked.connect(self.wallhack)
        self.pushButton_2.clicked.connect(self.noflash)
        self.pushButton_3.clicked.connect(self.radar)
        self.pushButton_4.clicked.connect(self.bhop)
        self.pushButton_5.clicked.connect(self.trigger)

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
        MainWindow.resize(750, 422)
        MainWindow.setMinimumSize(QSize(750, 422))
        MainWindow.setMaximumSize(QSize(750, 422))
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget#centralwidget{image: url(:/newPrefix/beeg.jpg);}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QRect(620, 20, 90, 60))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-image: url(:/newPrefix/flag.png);")
        self.pushButton_1.setCheckable(False)
        self.pushButton_1.setChecked(False)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(620, 100, 90, 60))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/flag.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(620, 180, 90, 60))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/flag.png);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(620, 260, 90, 60))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/flag.png);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(620, 340, 90, 60))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-image: url(:/newPrefix/flag.png);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(10, 10, 371, 51))
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.label.setPalette(palette)
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel {  color : red; }")
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(0, 400, 401, 21))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.label_2.setPalette(palette)
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("QLabel {  color : white; }")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.addButtonActions()
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Koca yusuf2 (weak version)"))
        self.pushButton_1.setToolTip(_translate("MainWindow", "Shortcut: " + str(globals.wall_key)))
        self.pushButton_1.setText(_translate("MainWindow", "Wallhack"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Shortcut: " + str(globals.flash_key)))
        self.pushButton_2.setText(_translate("MainWindow", "NoFlash"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Shortcut: " + str(globals.radar_key)))
        self.pushButton_3.setText(_translate("MainWindow", "RadarHack"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Shortcut: " + str(globals.bhop_key)))
        self.pushButton_4.setText(_translate("MainWindow", "BHOP"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "Shortcut: " + str(globals.trigger_key)))
        self.pushButton_5.setText(_translate("MainWindow", "Trigger"))
        self.label.setText(_translate("MainWindow", "CS:GO is not running"))
        self.label_2.setText(_translate("MainWindow", "Updated:"))

    def _startUpdateTimer(self, secs):
        print("Starting update timer for %d seconds" % secs)
        try:
            self._updateTimer.stop()
        except:
            pass
        self._updateTimer = QTimer()
        self._updateTimer.timeout.connect(self.updateButtons)
        self._updateTimer.start(secs * 1000)

    def __init__(self, *args, **kwargs):
        print("Window started")
        worker = Worker()
        self._startUpdateTimer(1)
        self.threadpool = QThreadPool()
        self.threadpool.start(worker)
from ui_qtdesigner import resources_rc

def myExitHandler():
    sys.exit("User quit the app.")

app = QApplication(sys.argv)
app.aboutToQuit.connect(myExitHandler)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
