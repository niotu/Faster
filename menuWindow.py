import sqlite3

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem

from const.CONSTANTS import encoding
from const.menuWindow_UI import MenuWindow


class MenuPage(QMainWindow, MenuWindow):
    def __init__(self):
        super(MenuPage, self).__init__()
        self.selected_id = None
        self.texts = []
        self.titles = []

        self.setupUi(self)

        self.load()

        self.trainsView.itemClicked.connect(self.Clicked)

    def load(self):
        texts = self.load_from_db()  # load text list from database
        titles = []

        # texts = list(map(str.replace('\\n', '\n'), texts))
        self.texts = texts

        '''generate titles'''

        for text in texts:
            mas = text
            title = ' '.join(mas.replace('\\n', '\n').rstrip().split()[:2]).capitalize()
            titles.append(title if title[-1] not in ',./-_;:' else title[:-1])

        self.titles = titles

        '''put titles on listWidget'''

        for i, title in enumerate(titles):
            item = QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont('Inter')
            font.setKerning(True)
            font.setPixelSize(32)
            item.setFont(font)
            item.setText(title)
            self.trainsView.addItem(item)

    def load_from_db(self):
        con = sqlite3.connect("data/data.db")
        cur = con.cursor()
        res = []
        for item in cur.execute("""SELECT text FROM texts""").fetchall():
            res.append(item[0])
        con.close()
        return res

    def Clicked(self, item):
        train = item.text()
        self.selected_id = self.titles.index(train) + 1

    def update_texts(self):
        self.load()
