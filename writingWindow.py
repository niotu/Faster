import sqlite3
from random import randint

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QUrl, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QMessageBox, QMainWindow

from const.CONSTANTS import writingWindow_styles, corr_style, GOOD_WORDS, incorr_style, MAXSTRING, \
    dark_lineEditStyle, lineEditStyle
from const.writingWindow_UI import WritingWindow


class WritingSession(QMainWindow, WritingWindow):
    def __init__(self):
        super(WritingSession, self).__init__()
        self.icon = QIcon('icons/logo.png')
        self.id = None
        self.lines = []
        self.current_line_num = 0

        self.is_letter_ignore = None
        self.is_dark_theme = None

        self.lockedPix = QPixmap('icons/lock.png')
        self.unlockedPix = QPixmap('icons/unlock.png')
        self.unlockedMov = QMovie('icons/unlock.gif')
        self.lockedMov = QMovie('icons/lock.gif')

        self.is_running = False
        self.secs = 0
        self.is_completed = False
        self.is_on_training = False

        self.setupUi(self)

        self.sound_player = QMediaPlayer()
        correct = QUrl('sounds/correct-answer.mp3')
        self.correct = QMediaContent(correct)

        incorrect = QUrl('sounds/bad-answer.mp3')
        self.incorrect = QMediaContent(incorrect)

        self.setWindowIcon(self.icon)
        '''connects'''

        self.startButton.clicked.connect(lambda: self.start(self.startButton))
        self.stopButton.clicked.connect(lambda: self.stop(self.stopButton))
        '''set timer'''

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1)

    def set_dark_theme(self, is_dark_theme):
        self.is_dark_theme = is_dark_theme

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

        if self.id == 'random':
            self.lines = self.load_from_internet()
        else:
            self.lines = self.load_text_from_db(self.id)  # load lines from database using 'SELECT'

        self.show_correct(None)
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

    def load_text_from_db(self, id):
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        result = cur.execute(f"""SELECT text FROM texts WHERE id={id}""").fetchone()
        if '\\n' in result[0] or '\n' in result[0]:
            result = result[0].split('\\n')
        else:
            result = self.format_text(result[0])
        return result

    def format_text(self, text):
        lines = []
        line = []
        text = text.split()
        for word in text:
            if len(' '.join(line)) < MAXSTRING:
                line.append(word)
            else:
                incorrect = line.pop()
                lines.append(' '.join(line))
                line = [incorrect, word]
        lines.append(' '.join(line))
        return lines

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
        self.is_on_training = True
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
        self.is_on_training = False

        msgbox = QMessageBox(self)
        msgbox.setText(GOOD_WORDS[randint(0, len(GOOD_WORDS) - 1)])
        msgbox.setStyleSheet(writingWindow_styles)
        msgbox.setGeometry(QRect(810, 490, 300, 100))
        msgbox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        buttonY = msgbox.button(QMessageBox.Yes)
        buttonY.setText("Сохранить результат")
        buttonY.clicked.connect(lambda: self.export_to_db(self.secs, self.is_completed))
        buttonY.setStyleSheet(writingWindow_styles)

        buttonN = msgbox.button(QMessageBox.No)
        buttonN.setText("Начать заново")
        buttonN.clicked.connect(lambda: self.load(self.id))
        buttonN.setStyleSheet(writingWindow_styles)

        msgbox.setWindowTitle('Урааа')
        msgbox.show()

    def show_correct(self, is_correct):
        normal_style = dark_lineEditStyle if self.is_dark_theme else lineEditStyle
        if is_correct is None:
            self.mainLine.setStyleSheet(normal_style)
        elif is_correct:
            self.sound_player.setMedia(self.correct)
            self.sound_player.play()

            self.mainLine.setStyleSheet(corr_style)
            QTimer(self).singleShot(500, lambda: self.mainLine.setStyleSheet(normal_style))
        elif not is_correct:
            self.sound_player.setMedia(self.incorrect)
            self.sound_player.play()

            self.mainLine.setStyleSheet(incorr_style)
            QTimer(self).singleShot(500, lambda: self.mainLine.setStyleSheet(normal_style))

    def format_time(self, time):
        time = time // 10
        minutes = time // 6000
        seconds = (time - minutes * 6000) // 100
        mseconds = time - seconds * 100 - minutes * 6000
        minutes, seconds, mseconds = str(minutes), str(seconds), str(mseconds)
        return f'{minutes}:{seconds if len(seconds) > 1 else "0" + seconds}:{mseconds if len(mseconds) > 1 else "0" + mseconds}'

    def showTime(self):
        # checking if flag is true
        if self.is_running:
            # incrementing the counter
            self.secs += 1

        self.check_animation()

        # getting text from count
        text = str(self.format_time(self.secs))

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
                f.write(str(time) + '\n')

    def load_from_internet(self):
        from parsing_data.parser import Parser
        parser = Parser()
        parser.process()
        mas = parser.text
        mas = ''.join(mas).rstrip().split('\n')
        try:
            mas.remove('')
        except Exception:
            pass
        return mas

    def clear(self):
        self.is_on_training = False
        self.mainLine.setText('')
        self.currentLineView.setText('')
        self.nextLineView.setText('')
        self.previousLineView.setText('')
        self.lines = []
        self.secs = 0
        self.mainLine.setEnabled(False)
        self.showData.setPixmap(self.lockedPix)
