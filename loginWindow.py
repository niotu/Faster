import json

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

from const.CONSTANTS import incorr_style, loginWindow_styles, small_line_style
from const.loginWindow_UI import LoginWindow


class LoginPage(QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.name = ''
        self.password = ''

        self.setupUi(self)

        self.createAccount.clicked.connect(self.login)

    def load(self):
        self.setStyleSheet(loginWindow_styles)

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
        if widget == 'name':
            self.nameEdit.setStyleSheet(incorr_style)
            self.nameEdit.setToolTip("Имя должно быть длиннее 2 символов")
            QTimer(self).singleShot(1500, lambda: self.nameEdit.setStyleSheet(small_line_style))
        elif widget == 'password':
            self.passwordEdit.setStyleSheet(incorr_style)
            self.passwordEdit.setToolTip("Пароль должен быть длиннее 7 символов")
            QTimer(self).singleShot(1500, lambda: self.passwordEdit.setStyleSheet(small_line_style))
        elif widget == 'namepassword':
            self.nameEdit.setStyleSheet(incorr_style)
            self.nameEdit.setToolTip("Имя должно быть длиннее 2 символов")
            self.passwordEdit.setStyleSheet(incorr_style)
            self.passwordEdit.setToolTip("Пароль должен быть длиннее 7 символов")
            QTimer(self).singleShot(1500, lambda: self.clear())

    def clear(self):
        self.nameEdit.setStyleSheet(small_line_style)
        self.passwordEdit.setStyleSheet(small_line_style)

    def reset(self):
        self.nameEdit.setText('')
        self.passwordEdit.setText('')
        self.clear()
