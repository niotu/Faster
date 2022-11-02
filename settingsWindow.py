import json
import sqlite3

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from const.CONSTANTS import ENCODING, settingsWindow_styles, dark_settingsWindow_styles
from const.settingsWindow_UI import SettingsWindow


class SettingsPage(QMainWindow, SettingsWindow):
    def __init__(self):
        super(SettingsPage, self).__init__()
        self.previousWindow = None
        self.pix = QPixmap('icons/arrow.png')
        self.dpix = QPixmap('icons/dark-arrow.png')

        self.is_dark_theme = None
        self.is_letter_ignore = None
        self.settings = {}
        self.average_time = 0

        self.setupUi(self)
        self.load_settings()

        self.quit.setPixmap(self.pix)

        self.darkTheme.clicked.connect(self.set_dark_theme)
        self.letterIgnore.clicked.connect(self.set_letter_ignore)
        self.addFiles.clicked.connect(self.add_new_file)

    def setPreviousWindow(self, window):
        self.previousWindow = window

    def set_dark_theme(self):
        if self.darkTheme.isChecked():
            self.darkTheme.setIcon(QIcon('icons/toggle_on.png'))
            self.setStyleSheet(dark_settingsWindow_styles)
            self.quit.setPixmap(self.dpix)

            self.is_dark_theme = True
        else:
            self.setStyleSheet(settingsWindow_styles)
            self.darkTheme.setIcon(QtGui.QIcon('icons/toggle_off.png'))
            self.quit.setPixmap(self.pix)

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

        self.average_time = self.load_time()
        self.averageTimeView.setText('Среднее время выполнения: ' + self.average_time)

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

    def load_time(self):
        with open('data/times.txt', 'r') as f:
            times = f.readlines()
        times = list(map(int, times))
        return self.format_time(sum(times) // len(times) if len(times) > 0 else 0)

    def format_time(self, time):
        time = time // 10
        minutes = time // 6000
        seconds = (time - minutes * 6000) // 100
        mseconds = time - seconds * 100 - minutes * 6000
        minutes, seconds, mseconds = str(minutes), str(seconds), str(mseconds)
        return f'{minutes}:{seconds if len(seconds) > 1 else "0" + seconds}:{mseconds if len(mseconds) > 1 else "0" + mseconds}'

    def add_new_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Choose file', '', 'Text files(*.txt)')[0]
        if filename != '':
            with open(filename, 'r', encoding=ENCODING) as f:
                text = f.read()
            self.load_file_to_db(text)

    def load_file_to_db(self, text):
        con = sqlite3.connect("data/data.db")
        cur = con.cursor()
        num = cur.execute(f"""SELECT id FROM texts """).fetchall()
        num = num[-1][0] + 1
        res = (num, text)
        cur.execute(
            f"""INSERT INTO texts ( id, text ) VALUES {res};""")
        cur.execute("""COMMIT TRANSACTION;""")
        con.close()
