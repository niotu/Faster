import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5 import QtCore

from writingWindow import WritingSession
from loginWindow import LoginPage
from mainWindow import MainWindow




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.addWidget(LoginPage())
    application.addWidget(WritingSession())
    application.setWindowTitle('Faster')
    application.showMaximized()
    sys.excepthook = except_hook
    print("Started")
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Starting...")
    main()
