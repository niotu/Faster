from PyQt5.QtWidgets import QMainWindow

from dist.previewWindow_UI import PreviewWindow


class PreviewPage(QMainWindow, PreviewWindow):
    def __init__(self):
        super(PreviewPage, self).__init__()

        self.setupUi(self)
