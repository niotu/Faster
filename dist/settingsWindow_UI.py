# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from qtwidgets import AnimatedToggle


class SettingsWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1392, 905)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(340, 0, 1200, 1020))
        self.label.setStyleSheet("position: absolute;\n"
                                 "background: #D9D9D9;"
                                 "padding-bottom: 880px;\n"
                                 "font-family: \'Inter\';\n"
                                 "font-style: normal;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 32px;\n"
                                 "line-height: 39px;\n"
                                 "display: flex;\n"
                                 "align-items: center;\n"
                                 "text-align: center;\n"
                                 "\n"
                                 "color: #000000;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 150, 1000, 70))
        self.label_2.setStyleSheet("QLabel {"
                                   "position: absolute;\n"
                                   "background: #9E9E9E;\n"
                                   "border-radius: 25px;\n"
                                   "padding-left: 40px;\n"
                                   "font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 32px;\n"
                                   "line-height: 39px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "color: #000000;"
                                   "}"
                                   "QLabel:hover{"
                                   "position: absolute;\n"
                                   "background: #696969;\n"
                                   "border-radius: 25px;\n"
                                   "padding-left: 40px;\n"
                                   "font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 32px;\n"
                                   "line-height: 39px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "color: #000000;}")
        self.label_2.setObjectName("label_2")
        self.darkTheme = QtWidgets.QPushButton(Form)
        self.darkTheme.setGeometry(QtCore.QRect(1260, 170, 60, 30))
        self.darkTheme.setCheckable(True)
        self.darkTheme.setStyleSheet('background: transparent;')
        self.darkTheme.setIconSize(QtCore.QSize(60, 30))
        self.label_2.setToolTip('В разработке...')
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 250, 1000, 70))
        self.label_3.setStyleSheet("QLabel {"
                                   "position: absolute;\n"
                                   "background: #9E9E9E;\n"
                                   "border-radius: 25px;\n"
                                   "padding-left: 40px;\n"
                                   "font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 32px;\n"
                                   "line-height: 39px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "color: #000000;"
                                   "}"
                                   "QLabel:hover{"
                                   "position: absolute;\n"
                                   "background: #696969;\n"
                                   "border-radius: 25px;\n"
                                   "padding-left: 40px;\n"
                                   "font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 32px;\n"
                                   "line-height: 39px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "color: #000000;}")
        self.label_3.setObjectName("label_3")
        self.letterIgnore = QtWidgets.QPushButton(Form)
        self.letterIgnore.setGeometry(QtCore.QRect(1260, 270, 60, 30))
        self.letterIgnore.setCheckable(True)
        self.letterIgnore.setStyleSheet('background: transparent;')
        self.letterIgnore.setIconSize(QtCore.QSize(60, 30))
        self.signOut = QtWidgets.QPushButton(Form)
        self.signOut.setGeometry(QtCore.QRect(778, 900, 364, 71))
        self.signOut.setStyleSheet("QPushButton {\n"
                                   "position: absolute;\n"
                                   "background: #FFFFFF;\n"
                                   "border-radius: 25px;\n"
                                   "font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 32px;\n"
                                   "line-height: 39px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "color: #FF0000;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "position: absolute;\n"
                                   "background: #FFFFFF;\n"
                                   "border: 2px ridge #FF0000;\n"
                                   "border-radius: 25px;\n"
                                   "font-family: \'Inter\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 32px;\n"
                                   "line-height: 39px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "color: #FF0000;\n"
                                   "}\n"
                                   "")
        self.signOut.setObjectName("signOut")
        self.addFiles = QtWidgets.QPushButton(Form)
        self.addFiles.setGeometry(QtCore.QRect(460, 350, 1000, 70))
        self.addFiles.setStyleSheet("QPushButton {"
                                    "position: absolute;\n"
                                    "background: #9E9E9E;\n"
                                    "border-radius: 25px;\n"
                                    "padding-right: 660px;\n"
                                    "font-family: \'Inter\';\n"
                                    "font-style: normal;\n"
                                    "font-weight: 400;\n"
                                    "font-size: 32px;\n"
                                    "line-height: 39px;\n"
                                    "display: flex;\n"
                                    "align-items: center;\n"
                                    "text-align: center;\n"
                                    "color: #000000;"
                                    "}"
                                    "QPushButton:hover {"
                                    "position: absolute;\n"
                                    "background: #696969;\n"
                                    "border-radius: 25px;\n"
                                    "padding-right: 660px;\n"
                                    "font-family: \'Inter\';\n"
                                    "font-style: normal;\n"
                                    "font-weight: 400;\n"
                                    "font-size: 32px;\n"
                                    "line-height: 39px;\n"
                                    "display: flex;\n"
                                    "align-items: center;\n"
                                    "text-align: center;\n"
                                    "color: #000000;"
                                    "}")
        self.addFiles.setCheckable(False)
        self.addFiles.setFlat(False)
        self.addFiles.setObjectName("addFiles")
        self.addFiles.setToolTip('В разработке...')
        self.resetFiles = QtWidgets.QPushButton(Form)
        self.resetFiles.setGeometry(QtCore.QRect(460, 450, 1000, 70))
        self.resetFiles.setStyleSheet("QPushButton {"
                                      "position: absolute;\n"
                                      "background: #9E9E9E;\n"
                                      "border-radius: 25px;\n"
                                      "padding-right: 590px;\n"
                                      "font-family: \'Inter\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 32px;\n"
                                      "line-height: 39px;\n"
                                      "display: flex;\n"
                                      "align-items: center;\n"
                                      "text-align: center;\n"
                                      "color: #000000;"
                                      "}"
                                      "QPushButton:hover {"
                                      "position: absolute;\n"
                                      "background: #696969;\n"
                                      "border-radius: 25px;\n"
                                      "padding-right: 590px;\n"
                                      "font-family: \'Inter\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 32px;\n"
                                      "line-height: 39px;\n"
                                      "display: flex;\n"
                                      "align-items: center;\n"
                                      "text-align: center;\n"
                                      "color: #000000;"
                                      "}")
        self.quit = Pic(Form)
        self.quit.setGeometry(QtCore.QRect(460, 40, 80, 75))
        self.quit.setText('aaaa')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Настройки"))
        self.label_2.setText(_translate("Form", "Темная тема"))
        self.label_3.setText(_translate("Form", "Буква \"ё\" (буква \"ё\" = буква \"е\")"))
        self.signOut.setText(_translate("Form", "Выйти из аккаунта"))
        self.addFiles.setText(_translate("Form", "Добавить файлы"))
        self.resetFiles.setText(_translate("Form", "Перезагрузить файлы"))


class Pic(QtWidgets.QLabel):
    click = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(ev)
        self.click.emit()
