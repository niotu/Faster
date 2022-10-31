from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow

from dist.main_UI import Ui_StackedWidget
from loginWindow import LoginPage
from writingWindow import WritingSession
from previewWindow import PreviewPage


class MainWindow(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loginPage = LoginPage()
        self.writingWindow = WritingSession()
        self.previewWindow = PreviewPage()

        self.setupUi(self)

        self.addWidget(self.loginPage)
        self.addWidget(self.previewWindow)
        self.addWidget(self.writingWindow)

        self.loginPage.createAccount.clicked.connect(lambda: self.jump_login_window(self.previewWindow))
        self.previewWindow.goNext.clicked.connect(lambda : self.jump_menu_window(self.writingWindow))

    def jump_login_window(self, window):
        if self.loginPage.login():
            self.setCurrentWidget(window)
        else:
            self.loginPage.incorr_reqs()

    def jump_menu_window(self, window):
        self.setCurrentWidget(window)
