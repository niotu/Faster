import json

from PyQt5.QtCore import QTimer, QRect, QUrl
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow

from const.CONSTANTS import incorr_style, small_line_style, dark_small_line_style, Pic
from const.loginWindow_UI import LoginWindow


class LoginPage(QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.kitten = None
        self.name = ''
        self.is_dark_theme = None

        self.moon = QPixmap('icons/moon.png')
        self.sun = QPixmap('icons/sun.png')

        self.setupUi(self)

        self.add_kitten()

        self.sound_player = QMediaPlayer()
        meow = QUrl('sounds/kitten.mp3')
        self.meow = QMediaContent(meow)
        self.sound_player.setMedia(self.meow)

        self.darkThemeView.setText('light')
        self.darkThemeView.setPixmap(self.moon)
        self.createAccount.clicked.connect(self.login)
        self.kitten_view.click.connect(lambda: self.play())

    def play(self):
        print(1)
        self.sound_player.play()

    def set_dark_theme(self, is_dark_theme):
        self.is_dark_theme = is_dark_theme

    def login(self):
        name = self.nameEdit.text()
        if len(name) <= 1:
            self.incorr_reqs('namepassword')
            return False
        elif len(name) <= 1:
            self.incorr_reqs('name')
            return False

        else:
            self.name = name
            self.create_account()
            return True

    def create_account(self):
        data = {"is_logined": True, "name": self.name}
        with open('data/account.json', 'w') as account:
            json.dump(data, account)

    def incorr_reqs(self, widget):
        if self.is_dark_theme:
            normal_line = dark_small_line_style
        else:
            normal_line = small_line_style

        if widget == 'name':
            self.nameEdit.setStyleSheet(incorr_style)
            self.nameEdit.setToolTip("Имя должно быть длиннее 2 символов")
            QTimer(self).singleShot(1500, lambda: self.nameEdit.setStyleSheet(normal_line))

            QTimer(self).singleShot(1500, lambda: self.clear(normal_line))

    def clear(self, normal_line):
        self.nameEdit.setStyleSheet(normal_line)

    def reset(self):
        self.nameEdit.setText('')
        self.clear(small_line_style)

    def add_kitten(self):
        self.kitten = QMovie('icons/kittens.gif')
        self.kitten_view = Pic(self)
        self.kitten_view.setGeometry(QRect(100, 550, 250, 250))
        self.kitten_view.setMovie(self.kitten)
        self.kitten_view.setStyleSheet('background:transparent;')
        self.kitten.start()
