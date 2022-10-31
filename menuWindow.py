from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox

from dist.menuWindow_UI import MenuWindow
from dist.CONSTANTS import encoding


class MenuPage(QMainWindow, MenuWindow):
    def __init__(self):
        super(MenuPage, self).__init__()
        self.selected_train_path = None
        self.texts = []
        self.titles = []

        self.setupUi(self)

        self.load()

        self.trainsView.itemClicked.connect(self.Clicked)

    def load(self):
        with open('texts/all_texts.txt', 'r', encoding=encoding) as f:
            texts = f.readlines()
        titles = []

        texts = list(map(str.rstrip, texts))
        self.texts = texts

        for text in texts:
            with open(f'texts/{text.rstrip()}', 'r', encoding=encoding) as f:
                mas = f.read()

                title = ' '.join(mas.rstrip().split()[:2]).capitalize()
            titles.append(title if title[-1] not in ',./-_;:' else title[:-1])

        self.titles = titles

        for i, title in enumerate(titles):
            item = QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont('Inter')
            font.setKerning(True)
            font.setPixelSize(32)
            item.setFont(font)
            item.setText(title)
            self.trainsView.addItem(item)

    def Clicked(self, item):
        train = item.text()
        self.selected_train_path = 'texts/' + self.texts[self.titles.index(train)]

    def update_texts(self):
        pass
