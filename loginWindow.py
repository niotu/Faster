import json

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from const.CONSTANTS import incorr_style, small_line_style, dark_small_line_style
from const.loginWindow_UI import LoginWindow


class LoginPage(QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.name = ''
        self.password = ''
        self.is_dark_theme = None

        self.moon = QPixmap('icons/moon.png')
        self.sun = QPixmap('icons/sun.png')

        self.setupUi(self)

        self.darkThemeView.setText('light')
        self.darkThemeView.setPixmap(self.moon)
        self.createAccount.clicked.connect(self.login)

    def set_dark_theme(self, is_dark_theme):
        self.is_dark_theme = is_dark_theme

    def login(self):
        name = self.nameEdit.text()
        password = self.passwordEdit.text()
        if len(name) <= 1 and len(password) <= 7:
            self.incorr_reqs('namepassword')
            return False
        elif len(name) <= 1:
            self.incorr_reqs('name')
            return False
        elif len(password) <= 7:
            self.incorr_reqs('password')
            return False
        else:
            self.name = name
            self.password = password
            self.create_account()
            return True

    def create_account(self):
        data = {"is_logined": True, "name": self.name, "password": self.password}
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
        elif widget == 'password':
            self.passwordEdit.setStyleSheet(incorr_style)
            self.passwordEdit.setToolTip("Пароль должен быть длиннее 7 символов")
            QTimer(self).singleShot(1500, lambda: self.passwordEdit.setStyleSheet(normal_line))
        elif widget == 'namepassword':
            self.nameEdit.setStyleSheet(incorr_style)
            self.nameEdit.setToolTip("Имя должно быть длиннее 2 символов")
            self.passwordEdit.setStyleSheet(incorr_style)
            self.passwordEdit.setToolTip("Пароль должен быть длиннее 7 символов")
            QTimer(self).singleShot(1500, lambda: self.clear(normal_line))

    def clear(self, normal_line):
        self.nameEdit.setStyleSheet(normal_line)
        self.passwordEdit.setStyleSheet(normal_line)

    def reset(self):
        self.nameEdit.setText('')
        self.passwordEdit.setText('')
        self.clear(small_line_style)
