from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox

from dist.settingsWindow_UI import SettingsWindow
from dist.CONSTANTS import encoding


class SettingsPage(QMainWindow, SettingsWindow):
    def __init__(self):
        super(SettingsPage, self).__init__()
        self.previousWindow = None
        self.pix = QPixmap('icons/arrow.png')

        self.setupUi(self)

        self.quit.setPixmap(self.pix)

    def setPreviousWindow(self, window):
        self.previousWindow = window
