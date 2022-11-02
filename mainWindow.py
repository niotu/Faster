import json

from PyQt5.QtWidgets import QStackedWidget

from const.CONSTANTS import default_settings, default_account, writingWindow_styles, loginWindow_styles, \
    settingsWindow_styles, menuWindow_styles, previewWindow_styles, dark_loginWindow_styles, dark_previewWindow_styles, \
    dark_menuWindow_styles, dark_settingsWindow_styles, dark_writingWindow_styles
from const.main_UI import Ui_StackedWidget
from loginWindow import LoginPage
from menuWindow import MenuPage
from previewWindow import PreviewPage
from settingsWindow import SettingsPage
from writingWindow import WritingSession


class MainWindow(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loginWindow = LoginPage()
        self.writingWindow = WritingSession()
        self.previewWindow = PreviewPage()
        self.menuWindow = MenuPage()
        self.settingsWindow = SettingsPage()

        self.is_logined = None
        self.is_dark_theme = None
        self.name = ''

        self.account = {}

        self.setupUi(self)

        self.addWidget(self.loginWindow)
        self.addWidget(self.previewWindow)
        self.addWidget(self.menuWindow)
        self.addWidget(self.writingWindow)
        self.addWidget(self.settingsWindow)

        self.loginWindow.createAccount.clicked.connect(lambda: self.jump_from_login_window(self.previewWindow))
        self.loginWindow.darkThemeView.click.connect(self.set_dark_theme)
        self.previewWindow.goNext.clicked.connect(self.jump_menu_window)
        self.menuWindow.trainsView.itemDoubleClicked.connect(lambda: self.jump_writing_window(self.writingWindow))
        self.menuWindow.settingsButton.clicked.connect(lambda: self.jump_settings_window(self.menuWindow))
        self.writingWindow.menuButton.clicked.connect(self.jump_menu_window)
        self.writingWindow.settingsButton.clicked.connect(lambda: self.jump_settings_window(self.writingWindow))
        self.settingsWindow.quit.click.connect(lambda: self.jump_from_settings_window())
        self.settingsWindow.signOut.clicked.connect(self.sign_out)
        self.settingsWindow.resetFiles.clicked.connect(self.menuWindow.load)

        self.load()

    def jump_from_login_window(self, window):
        if self.loginWindow.login():
            self.settingsWindow.write_settings({'darkTheme': self.is_dark_theme, 'letterIgnore': False})
            self.load()
            self.settingsWindow.load_settings()
            self.set_theme(self.is_dark_theme)
            self.previewWindow.load(self.name)

            self.setCurrentWidget(window)

    def jump_menu_window(self):
        if not self.writingWindow.is_running:
            self.set_theme(self.settingsWindow.is_dark_theme)
            self.menuWindow.load()
            self.setCurrentWidget(self.menuWindow)

    def jump_writing_window(self, window):
        self.set_theme(self.settingsWindow.is_dark_theme)
        id = self.menuWindow.selected_id
        self.writingWindow.set_letter_ignore(self.settingsWindow.is_letter_ignore)
        self.load_writing_window(id)
        self.setCurrentWidget(window)

    def load_writing_window(self, id):
        self.set_theme(self.settingsWindow.is_dark_theme)
        self.writingWindow.load(id)

    def jump_settings_window(self, window):
        self.set_theme(self.settingsWindow.is_dark_theme)
        self.settingsWindow.load_settings()
        self.settingsWindow.setPreviousWindow(window)
        self.setCurrentWidget(self.settingsWindow)

    def jump_from_settings_window(self):
        self.set_theme(self.settingsWindow.is_dark_theme)
        self.setCurrentWidget(self.settingsWindow.previousWindow)

    def load(self):
        with open('data/settings.json', 'r') as settings:
            settings = json.load(settings)
        is_dark_theme = settings['darkTheme']
        self.is_dark_theme = is_dark_theme
        self.set_theme(self.is_dark_theme)

        with open('data/account.json', 'r') as account_data:
            self.account = json.load(account_data)
        self.is_logined = self.account['is_logined']
        self.name = self.account['name']
        if self.is_logined:
            self.previewWindow.load(self.name)
            self.setCurrentWidget(self.previewWindow)
        else:
            self.setCurrentWidget(self.loginWindow)

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
        self.loginWindow.reset()
        self.setCurrentWidget(self.loginWindow)

    def set_theme(self, is_dark_theme):
        if is_dark_theme:
            self.menuWindow.setStyleSheet(dark_menuWindow_styles)
            self.previewWindow.setStyleSheet(dark_previewWindow_styles)
            self.writingWindow.setStyleSheet(dark_writingWindow_styles)
            self.settingsWindow.setStyleSheet(dark_settingsWindow_styles)
            self.settingsWindow.quit.setPixmap(self.settingsWindow.dpix)
            self.loginWindow.setStyleSheet(dark_loginWindow_styles)
        else:
            self.menuWindow.setStyleSheet(menuWindow_styles)
            self.previewWindow.setStyleSheet(previewWindow_styles)
            self.writingWindow.setStyleSheet(writingWindow_styles)
            self.settingsWindow.setStyleSheet(settingsWindow_styles)
            self.settingsWindow.quit.setPixmap(self.settingsWindow.pix)
            self.loginWindow.setStyleSheet(loginWindow_styles)

    def set_dark_theme(self):
        if not self.is_dark_theme:
            self.is_dark_theme = True
            self.loginWindow.darkThemeView.setPixmap(self.loginWindow.sun)
            self.loginWindow.set_dark_theme(self.is_dark_theme)
            self.settingsWindow.darkTheme.setChecked(self.is_dark_theme)
            self.loginWindow.setStyleSheet(dark_loginWindow_styles)
        else:
            self.is_dark_theme = False
            self.loginWindow.darkThemeView.setPixmap(self.loginWindow.moon)
            self.loginWindow.set_dark_theme(self.is_dark_theme)
            self.settingsWindow.darkTheme.setChecked(self.is_dark_theme)
            self.loginWindow.setStyleSheet(loginWindow_styles)

