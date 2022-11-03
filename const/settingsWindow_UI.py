# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from const.CONSTANTS import Pic


class SettingsWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1392, 905)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(340, 0, 1200, 1020))
        # self.label.setStyleSheet(bg_wall_style + 'padding-bottom: 880px;')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 150, 1000, 70))
        # self.label_2.setStyleSheet(active_qlabel_style)
        self.label_2.setObjectName("label_2")
        self.darkTheme = QtWidgets.QPushButton(Form)
        self.darkTheme.setGeometry(QtCore.QRect(1260, 170, 60, 30))
        self.darkTheme.setCheckable(True)
        self.darkTheme.setStyleSheet('background: transparent;')
        self.darkTheme.setIconSize(QtCore.QSize(60, 30))
        self.label_2.setToolTip('В разработке...')
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 250, 1000, 70))
        # self.label_3.setStyleSheet(active_qlabel_style)
        self.label_3.setObjectName("label_3")
        self.letterIgnore = QtWidgets.QPushButton(Form)
        self.letterIgnore.setGeometry(QtCore.QRect(1260, 270, 60, 30))
        self.letterIgnore.setCheckable(True)
        self.letterIgnore.setStyleSheet('background: transparent;')
        self.letterIgnore.setIconSize(QtCore.QSize(60, 30))
        self.signOut = QtWidgets.QPushButton(Form)
        self.signOut.setGeometry(QtCore.QRect(778, 900, 364, 71))
        # self.signOut.setStyleSheet(signOutButtonStyle)
        self.signOut.setObjectName("signOut")
        self.addFiles = QtWidgets.QPushButton(Form)
        self.addFiles.setGeometry(QtCore.QRect(460, 350, 1000, 70))
        # self.addFiles.setStyleSheet(item_button_style)
        self.addFiles.setCheckable(False)
        self.addFiles.setFlat(False)
        self.addFiles.setObjectName("addFiles")
        self.addFiles.setToolTip('В разработке...')
        self.resetFiles = QtWidgets.QPushButton(Form)
        self.resetFiles.setGeometry(QtCore.QRect(460, 450, 1000, 70))
        # self.resetFiles.setStyleSheet(item_button_style)
        self.quit = Pic(Form)
        self.quit.setGeometry(QtCore.QRect(460, 40, 80, 75))
        self.quit.setObjectName("quit")
        self.averageTimeView = QtWidgets.QLabel(Form)
        # self.averageTimeView.setStyleSheet(textStyle)
        self.averageTimeView.setAlignment(QtCore.Qt.AlignCenter)
        self.averageTimeView.setGeometry(QtCore.QRect((1920 - 600) // 2, 600, 600, 71))
        self.averageTimeView.setObjectName('averageTimeView')
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
