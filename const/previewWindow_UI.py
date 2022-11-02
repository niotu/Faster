# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'previewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from const.CONSTANTS import previewWindow_styles


class PreviewWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1395, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(456, 132, 1007, 168))
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(456, 331, 1007, 515))
        self.bgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bgLabel.setObjectName("bgLabel")
        self.goNext = QtWidgets.QPushButton(self.centralwidget)
        self.goNext.setGeometry(QtCore.QRect(779, 877, 352, 70))
        self.goNext.setObjectName("goNext")
        self.bgLabel.raise_()
        self.welcome_label.raise_()
        self.goNext.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_label.setText(_translate("MainWindow", "Добро пожаловать в Faster"))
        self.bgLabel.setText(_translate("MainWindow", "Faster - программа для тренировки слепой печати на\n"
                                                      "клавиатуре компьютера.\n"
                                                      "\n"
                                                      "Faster поможет вам, если вы хотите научиться быстро\n"
                                                      "печатать различные тексты, в том числе ваши \n"
                                                      "собственные. \n"
                                                      "\n"
                                                      "Например: “Привет, как дела?”\n"
                                                      "\n"
                                                      "Готовы к первой тренировке?"))
        self.goNext.setText(_translate("MainWindow", "Начать тренировку"))
