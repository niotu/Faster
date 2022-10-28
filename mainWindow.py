from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from writingWindow import Ui_MainWindow

from CONSTANTS import buttonStyle, textStyle, fadeStyle


class Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.icon = QIcon('icons/logo.png')
        self.filename = 'texts/text1'
        self.lines = []
        self.__fading_button = None

        self.setupUi(self)
        self.setWindowIcon(self.icon)
        self.load(self.filename)
        self.startButton.clicked.connect(lambda: self.start(self.startButton))
        # self.line.changeEvent(QEvent.KeyPress)

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            file = f.readlines()
        self.lines = file
        self.mainText.setText(''.join(self.lines))

    def fade(self, button):
        button.setStyleSheet(fadeStyle)
        print('pressed')
        QTimer.singleShot(150, lambda: self.unfade(button))

    def unfade(self, button):
        button.setStyleSheet(buttonStyle)

    def start(self, button):
        print('pressed')
        self.fade(button)
