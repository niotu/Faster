from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from writingWindow import Ui_MainWindow

from CONSTANTS import buttonStyle, textStyle, fadeStyle, maxTime


class Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.icon = QIcon('icons/logo.png')
        self.filename = 'texts/text1'
        self.lines = []

        self.is_running = False
        self.secs = 0

        self.setupUi(self)

        self.setWindowIcon(self.icon)
        self.load(self.filename)

        '''connects'''

        self.startButton.clicked.connect(lambda: self.start(self.startButton))
        self.settingsButton.clicked.connect(lambda: self.jumpWindow(self.settingsButton, None))
        self.menuButton.clicked.connect(lambda: self.jumpWindow(self.menuButton, None))
        self.stopButton.clicked.connect(lambda: self.stop(self.stopButton))
        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(100)

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            file = f.readlines()
        self.lines = file
        self.timerView.setText('0:00:00')
        self.mainText.setText(''.join(self.lines))

    def start(self, button):
        self.fade(button)
        self.is_running = True

    def jumpWindow(self, button, window):
        self.fade(button)

    def stop(self, button):
        self.fade(button)
        self.is_running = False

    '''other functions'''

    def showTime(self):
        # checking if flag is true
        if self.is_running:
            # incrementing the counter
            self.secs += 1

        # getting text from count
        text = str(self.secs / 10)

        # showing text
        self.timerView.setText(text)

    def fade(self, button):
        button.setStyleSheet(fadeStyle)
        print('pressed')
        QTimer.singleShot(150, lambda: self.unfade(button))

    def unfade(self, button):
        button.setStyleSheet(buttonStyle)
