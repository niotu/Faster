from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow

from dist.main_UI import Ui_StackedWidget
from loginWindow import LoginPage
from writingWindow import WritingSession
from previewWindow import PreviewPage
from menuWindow import MenuPage
from settingsWindow import SettingsPage

from dist.CONSTANTS import encoding


class MainWindow(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loginPage = LoginPage()
        self.writingWindow = WritingSession()
        self.previewWindow = PreviewPage()
        self.menuWindow = MenuPage()
        self.settingsWindow = SettingsPage()

        self.setupUi(self)

        self.addWidget(self.loginPage)
        self.addWidget(self.previewWindow)
        self.addWidget(self.menuWindow)
        self.addWidget(self.writingWindow)
        self.addWidget(self.settingsWindow)

        self.loginPage.createAccount.clicked.connect(lambda: self.jump_login_window(self.previewWindow))
        self.previewWindow.goNext.clicked.connect(lambda: self.jump_menu_window(self.menuWindow))
        self.menuWindow.trainsView.itemDoubleClicked.connect(lambda: self.jump_writing_window(self.writingWindow))
        self.menuWindow.settingsButton.clicked.connect(lambda: self.jump_settings_window(self.menuWindow))
        self.writingWindow.menuButton.clicked.connect(lambda: self.jump_menu_window(self.menuWindow))
        self.writingWindow.settingsButton.clicked.connect(lambda: self.jump_settings_window(self.writingWindow))
        self.settingsWindow.quit.click.connect(lambda: self.jump_from_settings_window())

    def jump_login_window(self, window):
        if self.loginPage.login():
            self.setCurrentWidget(window)
        else:
            self.loginPage.incorr_reqs()

    def jump_menu_window(self, window):
        if not self.writingWindow.is_running:
            self.setCurrentWidget(self.menuWindow)

    def jump_writing_window(self, window):
        filename = self.menuWindow.selected_train_path
        self.load_writing_window(filename)
        self.setCurrentWidget(window)

    def load_writing_window(self, file):
        with open(file, 'r', encoding=encoding) as f:
            mas = f.readlines()
        with open('texts/current_text', 'w', encoding=encoding) as f:
            f.write(''.join(mas))
        self.writingWindow.load(self.writingWindow.filename)

    def jump_settings_window(self, window):
        self.settingsWindow.setPreviousWindow(window)
        self.setCurrentWidget(self.settingsWindow)

    def jump_from_settings_window(self):
        self.setCurrentWidget(self.settingsWindow.previousWindow)
