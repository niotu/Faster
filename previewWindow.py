from PyQt5.QtWidgets import QMainWindow

from const.previewWindow_UI import PreviewWindow


class PreviewPage(QMainWindow, PreviewWindow):
    def __init__(self):
        super(PreviewPage, self).__init__()

        self.kitten = None
        self.setupUi(self)
        self.load('name')

    def load(self, name):
        self.welcome_label.setText('Добро пожаловать в Faster, ' + name)
