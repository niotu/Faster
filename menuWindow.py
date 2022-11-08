import sqlite3
import os.path
import requests
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QListWidgetItem, QMainWindow

from const.menuWindow_UI import MenuWindow


class MenuPage(QMainWindow, MenuWindow):
    def __init__(self):
        super(MenuPage, self).__init__()
        self.selected_id = None
        self.texts = []
        self.titles = []

        self.db_path = None

        self.setupUi(self)

        self.load()

        self.trainsView.itemClicked.connect(self.Clicked)

    def load(self):
        self.trainsView.clear()
        texts = self.load_from_db()  # load text list from database
        titles = []

        self.texts = texts

        '''generate titles'''

        for text in texts:
            mas = text
            title = ' '.join(mas.replace('\\n', '\n').rstrip().split()[:2]).capitalize()
            titles.append(title if title[-1] not in ',./-_;:' else title[:-1])

        self.titles = titles

        '''put titles on listWidget'''

        for i, title in enumerate(titles):  # put titles on items
            item = QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont('Inter')
            font.setKerning(True)
            font.setPixelSize(32)
            item.setFont(font)
            item.setText(title)
            self.trainsView.addItem(item)

        '''lastItem will be used for a random text'''

        if self.internet_on():
            lastItem = QListWidgetItem()
            lastItem.setTextAlignment(QtCore.Qt.AlignCenter)
            lastItem.setBackground(QColor(191, 215, 124))
            font = QtGui.QFont('Inter')
            font.setKerning(True)
            font.setPixelSize(32)
            lastItem.setFont(font)
            lastItem.setText('Случайный стих')
            self.trainsView.addItem(lastItem)

    def load_from_db(self):
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        res = []
        try:
            for item in cur.execute("""SELECT text FROM texts""").fetchall():
                res.append(item[0])
            con.close()
        except Exception:
            with open('data/create_db.sql', 'r', encoding='utf-8') as sql_file:
                sql = sql_file.read()
            result = cur.executescript(sql)
            for item in cur.execute("""SELECT text FROM texts""").fetchall():
                res.append(item[0])
            con.close()
        return res

    def Clicked(self, item):
        train = item.text()
        if train == 'Случайный стих' or train == 'Загрузка...':
            self.selected_id = 'random'
            # item.setText('Загрузка...')
        else:
            self.selected_id = self.titles.index(train) + 1

    def internet_on(self):
        try:
            r = requests.session().get('https://stihi.ru', timeout=(3.05, 7.05))
            return True
        except Exception as e:
            return False

    def update_texts(self):
        self.load()
