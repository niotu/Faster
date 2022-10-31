from PyQt5.QtWidgets import QMainWindow

from dist.loginWindow_UI import LoginWindow
from writingWindow import WritingSession


class LoginPage(QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.setupUi(self)

        self.createAccount.clicked.connect(self.login)

    def login(self):
        name = self.nameEdit.text()
        # password = self.passwordEdit.text()
        # if len(name) > 1 and len(password) > 7:
        #     self.create_account()
        # else:
        #     self.welcome_label.setText("Имя должно быть длиннее 2 символов,\n а пароль длиннее 7.")

    def create_account(self):
        print('account')
