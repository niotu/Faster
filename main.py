import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from const.CONSTANTS import ENCODING
from loginWindow import LoginPage
from mainWindow import MainWindow
from writingWindow import WritingSession


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    with open('data/current_text', 'w', encoding=ENCODING) as f:
        f.write('')
    app = QApplication(sys.argv)
    application = MainWindow()
    application.addWidget(LoginPage())
    application.addWidget(WritingSession())
    application.setWindowTitle('Faster')
    application.setWindowIcon(QIcon('icons/logo.png'))
    application.showMaximized()
    sys.excepthook = except_hook
    print("Started")
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Starting...")
    main()
    os.remove('data/current_text')
