from PyQt5.QtWidgets import QApplication
import sys

from PyQt5 import QtCore

from mainWindow import Application


def main():
    app = QApplication(sys.argv)
    application = Application()
    application.setWindowTitle('Faster')
    application.showMaximized()
    print("Started")
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Starting...")
    main()
