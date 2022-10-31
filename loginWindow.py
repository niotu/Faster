from PyQt5.QtWidgets import QMainWindow

from dist.loginWindow_UI import LoginWindow
from writingWindow import WritingSession

from dist.CONSTANTS import incorr_style


class LoginPage(QMainWindow, LoginWindow):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.setupUi(self)

        self.createAccount.clicked.connect(self.login)

    def login(self):
        name = self.nameEdit.text()
        password = self.passwordEdit.text()
        if len(name) > 1 and len(password) > 7:
            return True
        else:
            return False

    def create_account(self):
        print('account')

    def incorr_reqs(self):
        self.nameEdit.setStyleSheet(incorr_style)
        self.nameEdit.setToolTip("Имя должно быть длиннее 2 символов")
        self.passwordEdit.setStyleSheet(incorr_style)
        self.passwordEdit.setToolTip("Пароль должен быть длиннее 7 символов")

