import sys
from PyQt5.QtWidgets import QApplication
from writingWindow import Application
from PyQt5 import QtCore


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QApplication(sys.argv)
    application = Application()
    application.setWindowTitle('Faster')
    application.showMaximized()
    sys.excepthook = except_hook
    print("Started")
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Starting...")
    main()
