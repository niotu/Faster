import json

from PyQt5.QtWidgets import QMainWindow

from dist.CONSTANTS import incorr_style
from dist.loginWindow_UI import LoginWindow


class LoginPage(QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.name = ''
        self.password = ''

        self.setupUi(self)
        self.createAccount.clicked.connect(self.login)

    def login(self):
        name = self.nameEdit.text()
        password = self.passwordEdit.text()
        if len(name) > 1 and len(password) > 7:
            self.name = name
            self.password = password
            self.create_account()
            return True
        else:
            return False

    def create_account(self):
        data = {"is_logined": True, "name": self.name, "password": self.password}
        with open('data/account.json', 'w') as account:
            json.dump(data, account)

    def incorr_reqs(self):
        self.nameEdit.setStyleSheet(incorr_style)
        self.nameEdit.setToolTip("Имя должно быть длиннее 2 символов")
        self.passwordEdit.setStyleSheet(incorr_style)
        self.passwordEdit.setToolTip("Пароль должен быть длиннее 7 символов")

    def reset(self):
        self.nameEdit.setStyleSheet('position: absolute;'
                                    'border: 2px solid transparent;'
                                    'border-bottom: 2px ridge #000000;'
                                    'background: #D9D9D9;'
                                    'font-family: "Inter";'
                                    'font-style: normal;'
                                    'font-weight: 400;'
                                    'font-size: 32px;'
                                    'line-height: 39px;'
                                    'display: flex;'
                                    'align-items: center;'
                                    'text-align: center;'
                                    'color: #000000;')
        self.nameEdit.setText('')
        self.passwordEdit.setStyleSheet('position: absolute;'
                                        'border: 2px solid transparent;'
                                        'border-bottom: 2px ridge #000000;'
                                        'background: #D9D9D9;'
                                        'font-family: "Inter";'
                                        'font-style: normal;'
                                        'font-weight: 400;'
                                        'font-size: 32px;'
                                        'line-height: 39px;'
                                        'display: flex;'
                                        'align-items: center;'
                                        'text-align: center;'
                                        'color: #000000;')
        self.passwordEdit.setText('')
