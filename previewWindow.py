from PyQt5.QtWidgets import QMainWindow

from const.CONSTANTS import previewWindow_styles
from const.previewWindow_UI import PreviewWindow


class PreviewPage(QMainWindow, PreviewWindow):
    def __init__(self):
        super(PreviewPage, self).__init__()

        self.setupUi(self)
        self.load('name')

    def load(self, name):
        self.setStyleSheet(previewWindow_styles)
        self.welcome_label.setText(name + ', добро пожаловать в Faster')
