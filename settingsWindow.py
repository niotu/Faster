import json

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow

from dist.settingsWindow_UI import SettingsWindow


class SettingsPage(QMainWindow, SettingsWindow):
    def __init__(self):
        super(SettingsPage, self).__init__()
        self.previousWindow = None
        self.pix = QPixmap('icons/arrow.png')

        self.is_dark_theme = None
        self.is_letter_ignore = None
        self.settings = {}

        self.setupUi(self)
        self.load_settings()

        self.quit.setPixmap(self.pix)

        self.darkTheme.clicked.connect(self.set_dark_theme)
        self.letterIgnore.clicked.connect(self.set_letter_ignore)

    def setPreviousWindow(self, window):
        self.previousWindow = window

    def set_dark_theme(self):
        if self.darkTheme.isChecked():
            self.darkTheme.setIcon(QIcon('icons/toggle_on.png'))
            self.is_dark_theme = True
        else:
            self.darkTheme.setIcon(QtGui.QIcon('icons/toggle_off.png'))
            self.is_dark_theme = False
        self.settings = {'darkTheme': self.is_dark_theme, 'letterIgnore': self.is_letter_ignore}
        self.write_settings(self.settings)

    def set_letter_ignore(self):
        if self.letterIgnore.isChecked():
            self.letterIgnore.setIcon(QIcon('icons/toggle_on.png'))
            self.is_letter_ignore = True
        else:
            self.letterIgnore.setIcon(QtGui.QIcon('icons/toggle_off.png'))
            self.is_letter_ignore = False
        self.settings = {'darkTheme': self.is_dark_theme, 'letterIgnore': self.is_letter_ignore}
        self.write_settings(self.settings)

    def load_settings(self):
        with open('data/settings.json', 'r') as fileobject:
            settings = json.load(fileobject)
        self.is_dark_theme = settings['darkTheme']
        self.is_letter_ignore = settings['letterIgnore']

        self.settings = settings

        if self.is_dark_theme:
            self.darkTheme.setChecked(True)
        if self.is_letter_ignore:
            self.letterIgnore.setChecked(True)
        self.set_dark_theme()
        self.set_letter_ignore()

    def write_settings(self, settings):
        with open('data/settings.json', 'w') as fileobject:
            json.dump(settings, fileobject)
