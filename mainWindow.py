import json

from PyQt5.QtWidgets import QStackedWidget

from const.CONSTANTS import default_settings, default_account
from const.main_UI import Ui_StackedWidget
from loginWindow import LoginPage
from menuWindow import MenuPage
from previewWindow import PreviewPage
from settingsWindow import SettingsPage
from writingWindow import WritingSession


class MainWindow(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loginPage = LoginPage()
        self.writingWindow = WritingSession()
        self.previewWindow = PreviewPage()
        self.menuWindow = MenuPage()
        self.settingsWindow = SettingsPage()

        self.is_logined = None
        self.name = ''

        self.account = {}

        self.setupUi(self)

        self.addWidget(self.loginPage)
        self.addWidget(self.previewWindow)
        self.addWidget(self.menuWindow)
        self.addWidget(self.writingWindow)
        self.addWidget(self.settingsWindow)

        self.loginPage.createAccount.clicked.connect(lambda: self.jump_login_window(self.previewWindow))
        self.previewWindow.goNext.clicked.connect(self.jump_menu_window)
        self.menuWindow.trainsView.itemDoubleClicked.connect(lambda: self.jump_writing_window(self.writingWindow))
        self.menuWindow.settingsButton.clicked.connect(lambda: self.jump_settings_window(self.menuWindow))
        self.writingWindow.menuButton.clicked.connect(self.jump_menu_window)
        self.writingWindow.settingsButton.clicked.connect(lambda: self.jump_settings_window(self.writingWindow))
        self.settingsWindow.quit.click.connect(lambda: self.jump_from_settings_window())
        self.settingsWindow.signOut.clicked.connect(self.sign_out)
        self.settingsWindow.resetFiles.clicked.connect(self.menuWindow.load)

        self.load()

    def jump_login_window(self, window):
        if self.loginPage.login():
            self.load()
            self.previewWindow.load(self.name)
            self.setCurrentWidget(window)

    def jump_menu_window(self):
        if not self.writingWindow.is_running:
            self.menuWindow.load()
            self.setCurrentWidget(self.menuWindow)

    def jump_writing_window(self, window):
        id = self.menuWindow.selected_id
        self.writingWindow.set_letter_ignore(self.settingsWindow.is_letter_ignore)
        self.load_writing_window(id)
        self.setCurrentWidget(window)

    def load_writing_window(self, id):
        self.writingWindow.load(id)

    def jump_settings_window(self, window):
        self.settingsWindow.load_settings()
        self.settingsWindow.setPreviousWindow(window)
        self.setCurrentWidget(self.settingsWindow)

    def jump_from_settings_window(self):
        # self.set_theme(self.settingsWindow.is_dark_theme)
        self.setCurrentWidget(self.settingsWindow.previousWindow)

    def load(self):
        with open('data/settings.json', 'r') as settings:
            settings = json.load(settings)
        is_dark_theme = settings['darkTheme']
        # self.set_theme(is_dark_theme=is_dark_theme)

        with open('data/account.json', 'r') as account_data:
            self.account = json.load(account_data)
        self.is_logined = self.account['is_logined']
        self.name = self.account['name']
        if self.is_logined:
            self.previewWindow.load(self.name)
            self.setCurrentWidget(self.previewWindow)
        else:
            self.loginPage.load()
            self.setCurrentWidget(self.loginPage)

    def sign_out(self):
        with open('data/account.json', 'w') as account:
            json.dump(default_account, account)

        with open('data/settings.json', 'w') as settings:
            json.dump(default_settings, settings)

        with open('data/times.txt', 'w') as times:
            times.write('')

        self.load()

        self.settingsWindow.darkTheme.setChecked(False)
        self.settingsWindow.letterIgnore.setChecked(False)
        self.settingsWindow.load_settings()

        self.menuWindow.load()
        self.loginPage.reset()
        self.setCurrentWidget(self.loginPage)
    #
    # def set_theme(self, is_dark_theme):
    #     if is_dark_theme:
    #         self.menuWindow.setStyleSheet(dark_background)
    #         self.previewWindow.setStyleSheet(dark_background)
    #         self.writingWindow.setStyleSheet(dark_background)
    #         # self.
