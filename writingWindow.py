import sqlite3
from random import randint

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QUrl, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QMessageBox

from const.CONSTANTS import corr_style, incorr_style, good_words, textStyle, lineEditStyle, buttonStyle
from const.writingWindow_UI import WritingWindow


class WritingSession(QMainWindow, WritingWindow):
    def __init__(self):
        super(WritingSession, self).__init__()
        self.icon = QIcon('icons/logo.png')
        self.id = None
        self.lines = []
        self.current_line_num = 0

        self.is_letter_ignore = None

        self.lockedPix = QPixmap('icons/lock.png')
        self.unlockedPix = QPixmap('icons/unlock.png')
        self.unlockedMov = QMovie('icons/unlock.gif')
        self.lockedMov = QMovie('icons/lock.gif')

        self.is_running = False
        self.secs = 0
        self.is_completed = False

        self.setupUi(self)

        self.sound_player = QMediaPlayer()
        url = QUrl('sounds/correct-answer.mp3')
        self.content = QMediaContent(url)

        self.setWindowIcon(self.icon)
        '''connects'''

        self.startButton.clicked.connect(lambda: self.start(self.startButton))
        self.stopButton.clicked.connect(lambda: self.stop(self.stopButton))
        '''set timer'''

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Enter, Qt.Key_Return) and self.is_running:
            self.check_lines()

    def set_letter_ignore(self, param):
        self.is_letter_ignore = param

    def load(self, id):
        self.id = id
        self.secs = 0
        self.mainLine.setEnabled(False)
        self.showData.setPixmap(self.lockedPix)

        self.lines = self.load_text(self.id)  # load lines from database using 'SELECT'

        self.timerView.setText('0:00:00')
        text1 = ''
        text2 = ''.join(self.lines[self.current_line_num])
        if len(self.lines) > 1:
            text3 = ''.join(self.lines[self.current_line_num + 1])
        else:
            text3 = ''
        self.previousLineView.setText(text1)
        self.currentLineView.setText(text2)
        self.nextLineView.setText(text3)

    def load_text(self, id):
        con = sqlite3.connect("data/data.db")
        cur = con.cursor()
        result = cur.execute(f"""SELECT text FROM texts WHERE id={id}""").fetchone()[0].split('\\n')
        return result

    def check_lines(self):
        line = self.mainLine.text()
        curr_line = self.lines[self.current_line_num].rstrip()
        if self.is_letter_ignore:
            line = line.replace("ё", 'е').replace('Ё', 'Е')
            curr_line = curr_line.replace("ё", 'е').replace('Ё', 'Е')
        if curr_line == line:
            self.show_correct(True)
            self.current_line_num += 1
            self.mainLine.setText('')
            if len(self.lines) == self.current_line_num:
                self.win()
            else:
                text1, text2, text3 = '', '', ''
                if 0 < self.current_line_num < len(self.lines) - 1:
                    text1 = ''.join(self.lines[self.current_line_num - 1])
                    text2 = ''.join(self.lines[self.current_line_num])
                    text3 = ''.join(self.lines[self.current_line_num + 1])
                elif self.current_line_num == len(self.lines) - 1:
                    text1 = ''.join(self.lines[self.current_line_num - 1])
                    text2 = ''.join(self.lines[self.current_line_num])
                self.previousLineView.setText(text1)
                self.currentLineView.setText(text2)
                self.nextLineView.setText(text3)
        else:
            self.show_correct(False)

    def start(self, button):
        self.is_running = True
        self.mainLine.setEnabled(True)
        if self.is_completed:
            self.secs = 0
        self.showData.setMovie(self.unlockedMov)
        self.unlockedMov.start()
        self.mainLine.setFocus()

    def stop(self, button):
        self.is_running = False
        self.mainLine.setEnabled(False)
        self.showData.setMovie(self.lockedMov)
        self.lockedMov.start()

    '''other functions'''

    def win(self):
        self.stop(button=None)
        self.is_completed = True
        self.current_line_num = 0

        msgbox = QMessageBox(self)
        msgbox.setText(good_words[randint(0, len(good_words) - 1)])
        msgbox.setStyleSheet(textStyle)
        msgbox.setGeometry(QRect(810, 490, 300, 100))
        msgbox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        buttonY = msgbox.button(QMessageBox.Yes)
        buttonY.setText("Сохранить результат")
        buttonY.clicked.connect(lambda: self.export_to_db(self.secs, self.is_completed))
        buttonY.setStyleSheet(buttonStyle)

        buttonN = msgbox.button(QMessageBox.No)
        buttonN.setText("Начать заново")
        buttonN.clicked.connect(lambda: self.load(self.filename))
        buttonN.setStyleSheet(buttonStyle)

        msgbox.setWindowTitle('Урааа')
        msgbox.show()

    def show_correct(self, is_correct):
        if is_correct:
            sound_player = QMediaPlayer()
            url = QUrl('sounds/correct-answer.mp3')
            content = QMediaContent(url)
            sound_player.setMedia(content)
            sound_player.play()

            self.mainLine.setStyleSheet(corr_style)
            QTimer(self).singleShot(500, lambda: self.mainLine.setStyleSheet(lineEditStyle))

        else:
            sound_player = QMediaPlayer()
            url = QUrl('sounds/bad-answer.mp3')
            content = QMediaContent(url)
            sound_player.setMedia(content)
            sound_player.play()

            self.mainLine.setStyleSheet(incorr_style)
            QTimer(self).singleShot(500, lambda: self.mainLine.setStyleSheet(lineEditStyle))

    def format_time(self, time):
        minutes = time // 6000
        seconds = (time - minutes * 6000) // 100
        mscesonds = time - seconds * 100 - minutes * 6000
        return f'{minutes}:{seconds}:{mscesonds}'

    def showTime(self):
        # checking if flag is true
        if self.is_running:
            # incrementing the counter
            self.secs += 1

        self.check_animation()

        # getting text from count
        text = str(self.format_time(self.secs // 10))

        self.timerView.setText(text)

    def check_animation(self):
        if self.unlockedMov.currentFrameNumber() >= 14:
            self.unlockedMov.stop()
        if self.lockedMov.currentFrameNumber() >= 14:
            self.lockedMov.stop()

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def export_to_db(self, time, is_completed):
        if is_completed:
            with open('data/times.txt', 'a') as f:
                f.write(str(time))
