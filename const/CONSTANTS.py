from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal

lineEditStyle = 'position: absolute;' \
                'border: 2px solid transparent;' \
                'border-bottom: 3px ridge #000000;' \
                'background: transparent;' \
                'font-family: "Inter";' \
                'font-style: normal;' \
                'font-weight: 400;' \
                'font-size: 32px;' \
                'line-height: 39px;' \
                'text-align: center;' \
                'color: #000000;'

dark_lineEditStyle = 'position: absolute;' \
                     'border: 2px solid transparent;' \
                     'border-bottom: 3px ridge #F3F3F3;' \
                     'background: transparent;' \
                     'font-family: "Inter";' \
                     'font-style: normal;' \
                     'font-weight: 400;' \
                     'font-size: 32px;' \
                     'line-height: 39px;' \
                     'text-align: center;' \
                     'color: #F3F3F3;'

corr_style = 'position: absolute;' \
             'border: 2px solid transparent;' \
             'border-bottom: 2px ridge #52FF00;' \
             'background: transparent;' \
             'font-family: "Inter";' \
             'font-style: normal;' \
             'font-weight: 400;' \
             'font-size: 32px;' \
             'line-height: 39px;' \
             'text-align: center;' \
             'color: #52FF00;'

incorr_style = 'position: absolute;' \
               'border: 2px solid transparent;' \
               'border-bottom: 2px ridge #CA0D2F;' \
               'background: transparent;' \
               'font-family: "Inter";' \
               'font-style: normal;' \
               'font-weight: 400;' \
               'font-size: 32px;' \
               'line-height: 39px;' \
               'text-align: center;' \
               'color: #CA0D2F;'

small_line_style = 'position: absolute;' \
                   'border: 2px solid transparent;' \
                   'border-bottom: 2px ridge #000000;' \
                   'background: transparent;' \
                   'font-family: "Inter";' \
                   'font-style: normal;' \
                   'font-weight: 400;' \
                   'font-size: 32px;' \
                   'line-height: 39px;' \
                   'text-align: center;' \
                   'color: #000000;'

dark_small_line_style = 'position: absolute;' \
                        'border: 2px solid transparent;' \
                        'border-bottom: 2px ridge F3F3F3;' \
                        'background: transparent;' \
                        'font-family: "Inter";' \
                        'font-style: normal;' \
                        'font-weight: 400;' \
                        'font-size: 32px;' \
                        'line-height: 39px;' \
                        'text-align: center;' \
                        'color: #F3F3F3;'

'''LIGHT THEME STYLES'''

previewWindow_styles = 'QMainWindow#Form{background: #FAFAFA;}' \
                       "QLabel{" \
                       "position: absolute;" \
                       "background: #D9D9D9;" \
                       "border-radius: 25px;" \
                       "font-family: 'Inter';" \
                       "font-style: normal;\n" \
                       "font-weight: 400;\n" \
                       "font-size: 32px;\n" \
                       "line-height: 39px;\n" \
                       "text-align: center;\n" \
                       "color: #000000;" \
                       "}" \
                       "QPushButton{" \
                       "position: absolute;\n" \
                       "background: #9E9E9E;\n" \
                       "border-radius: 25px;\n" \
                       "font-family: \'Inter\';\n" \
                       "font-style: normal;\n" \
                       "font-weight: 400;\n" \
                       "font-size: 32px;\n" \
                       "line-height: 39px;\n" \
                       "text-align: center;\n" \
                       "color: #000000;\n" \
                       "}" \
                       "QPushButton:hover{" \
                       "position: absolute;\n" \
                       "background: #686868;\n" \
                       "border-radius: 25px;\n" \
                       "font-family: \'Inter\';\n" \
                       "font-style: normal;\n" \
                       "font-weight: 400;\n" \
                       "font-size: 32px;\n" \
                       "line-height: 39px;\n" \
                       "text-align: center;\n" \
                       "color: #000000;\n" \
                       "}"
menuWindow_styles = ('QMainWindow#Form{background: #FAFAFA;}'
                     "QListWidget{"
                     "position: absolute;\n"
                     "border: None;\n"
                     "background: #D9D9D9;\n"
                     "padding-left: 69px;\n"
                     "padding-right: 69px;\n"
                     "padding-top: 130px;\n"
                     "}"
                     "QListWidget:item {"
                     "padding-top: 28px;\n"
                     "padding-bottom: 28px;\n"
                     "background: #696969;\n"
                     "border-radius: 25px;\n"
                     "font-family: \'Inter\';\n"
                     "font-style: normal;\n"
                     "font-weight: 400;\n"
                     "font-size: 32px;\n"
                     "line-height: 39px;\n"
                     "text-align: center;\n"
                     "color: #000000;"
                     "}"
                     "QListWidget:item:!hover{\n"
                     "padding-top: 28px;\n"
                     "padding-bottom: 28px;\n"
                     "background: #9E9E9E;\n"
                     "border-radius: 25px;\n"
                     "font-family: \'Inter\';\n"
                     "font-style: normal;\n"
                     "font-weight: 400;\n"
                     "font-size: 32px;\n"
                     "line-height: 39px;\n"
                     "text-align: center;\n"
                     "color: #000000;"
                     "}"
                     "QListWidget:item:selected{\n"
                     "padding-top: 28px;\n"
                     "padding-bottom: 28px;\n"
                     "border: 2px ridge #000000;\n"
                     "background: #696969;\n"
                     "border-radius: 25px;\n"
                     "font-family: \'Inter\';\n"
                     "font-style: normal;\n"
                     "font-weight: 400;\n"
                     "font-size: 32px;\n"
                     "line-height: 39px;\n"
                     "text-align: center;\n"
                     "color: #000000;"
                     "}"
                     "QLabel{position: absolute;\n"
                     "background: #D9D9D9;\n"
                     "font-family: \'Inter\';\n"
                     "font-style: normal;\n"
                     "font-weight: 400;\n"
                     "font-size: 32px;\n"
                     "line-height: 39px;\n"
                     "text-align: center;\n"
                     "color: #000000;"
                     "}"
                     'QPushButton{'
                     'background: #D9D9D9;'
                     ' border-radius: 25px;'
                     'font-family: "Inter";'
                     'font-style: normal;'
                     'font-weight: 400;'
                     'font-size: 32px;'
                     'line-height: 39px;'
                     'text-align: center;'
                     'color: #000000;'
                     '}'
                     'QPushButton:hover{'
                     'background: #9E9E9E;'
                     'border-radius: 25px;'
                     'position: absolute;'
                     'font-family: "Inter";'
                     'font-style: normal;'
                     'font-weight: 400;'
                     'font-size: 32px;'
                     'line-height: 39px;'
                     'text-align: center;'
                     'color: #000000;'
                     '}')
writingWindow_styles = ('QMainWindow#Form{background: #FAFAFA;}'
                        'QPushButton{'
                        'background: #D9D9D9;'
                        ' border-radius: 25px;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'text-align: center;'
                        'color: #000000;'
                        '}'
                        'QPushButton:hover{'
                        'background: #9E9E9E;'
                        'border-radius: 25px;'
                        'position: absolute;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'text-align: center;'
                        'color: #000000;'
                        '}'
                        'QPushButton#startButton{'
                        'background: #3A3A3A;'
                        'border-radius: 25px;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'text-align: center;'
                        'color: #FFFFFF;'
                        '}'
                        'QPushButton#startButton:hover{'
                        'background: #202020;'
                        'border-radius: 25px;'
                        'position: absolute;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'text-align: center;'
                        'color: #FFFFFF;'
                        '}'
                        'QLabel{'
                        'position: absolute;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'color: #9E9E9E;'
                        '}'
                        'QLabel#currentLineView{'
                        'position: absolute;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'color: #000000;'
                        '}'
                        'QLabel#timerView{'
                        'position: absolute;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'color: #000000;}'
                        'QLineEdit{'
                        'position: absolute;'
                        'border: 2px solid transparent;'
                        'border-bottom: 3px ridge #000000;'
                        'background-color: transparent;'
                        'font-family: "Inter";'
                        'font-style: normal;'
                        'font-weight: 400;'
                        'font-size: 32px;'
                        'line-height: 39px;'
                        'color: #000000;}')
loginWindow_styles = ('QMainWindow#Form{background: #FAFAFA;}'
                      'QLabel{'
                      'position: absolute;'
                      'background: #D9D9D9;'
                      'border-radius: 25px;'
                      'font-family: \'Inter\';'
                      "font-style: normal;"
                      "font-weight: 400;"
                      "font-size: 32px;"
                      "line-height: 39px;"
                      "text-align: center;"
                      'color: #000000;}'
                      'QPushButton{'
                      "position: absolute;\n"
                      "background: #9E9E9E;\n"
                      "border-radius: 25px;\n"
                      "font-family: \'Inter\';\n"
                      "font-style: normal;\n"
                      "font-weight: 400;\n"
                      "font-size: 32px;\n"
                      "line-height: 39px;\n"
                      "text-align: center;\n"
                      "color: #000000;\n"
                      "}"
                      "QPushButton:hover{"
                      "position: absolute;\n"
                      "background: #686868;\n"
                      "border-radius: 25px;\n"
                      "font-family: \'Inter\';\n"
                      "font-style: normal;\n"
                      "font-weight: 400;\n"
                      "font-size: 32px;\n"
                      "line-height: 39px;\n"
                      "text-align: center;\n"
                      "color: #000000;\n"
                      '}'
                      'QLineEdit{position: absolute;'
                      'border: 2px solid transparent;'
                      'border-bottom: 2px ridge #000000;'
                      'background: #D9D9D9;'
                      'font-family: "Inter";'
                      'font-style: normal;'
                      'font-weight: 400;'
                      'font-size: 32px;'
                      'line-height: 39px;'
                      'text-align: center;'
                      'color: #000000;}')
settingsWindow_styles = ('QMainWindow#Form{background: #FAFAFA;}'
                         "QLabel#label_2 {"
                         "position: absolute;\n"
                         "background: #9E9E9E;\n"
                         "border-radius: 25px;\n"
                         "padding-left: 40px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #000000;"
                         "}"
                         "QLabel#label_2:hover{"
                         "position: absolute;\n"
                         "background: #696969;\n"
                         "border-radius: 25px;\n"
                         "padding-left: 40px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #000000;"
                         "}"
                         "QLabel#label_3 {"
                         "position: absolute;\n"
                         "background: #9E9E9E;\n"
                         "border-radius: 25px;\n"
                         "padding-left: 40px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #000000;"
                         "}"
                         "QLabel#label_3:hover{"
                         "position: absolute;\n"
                         "background: #696969;\n"
                         "border-radius: 25px;\n"
                         "padding-left: 40px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #000000;"
                         "}"
                         "QLabel#averageTimeView{position: absolute;"
                         'font-family: "Inter";'
                         'font-style: normal;'
                         'font-weight: 400;'
                         'font-size: 32px;'
                         'line-height: 39px;'
                         'text-align: center;'
                         'color: #000000;'
                         '}'
                         'QLabel#label{'
                         'position: absolute;'
                         "background: #D9D9D9;\n"
                         "padding-bottom: 880px;"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         'color: #000000;'
                         '}'
                         "QPushButton {"
                         "position: absolute;\n"
                         "background: #9E9E9E;\n"
                         "border-radius: 25px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #000000;"
                         "}"
                         "QPushButton:hover {"
                         "position: absolute;\n"
                         "background: #696969;\n"
                         "border-radius: 25px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #000000;"
                         "}"
                         "QPushButton#signOut {\n"
                         "position: absolute;\n"
                         "background: #FFFFFF;\n"
                         "border-radius: 25px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #FF0000;\n"
                         "}\n"
                         "QPushButton#signOut:hover{\n"
                         "position: absolute;\n"
                         "background: #FFFFFF;\n"
                         "border: 2px ridge #FF0000;\n"
                         "border-radius: 25px;\n"
                         "font-family: \'Inter\';\n"
                         "font-style: normal;\n"
                         "font-weight: 400;\n"
                         "font-size: 32px;\n"
                         "line-height: 39px;\n"
                         "text-align: center;\n"
                         "color: #FF0000;\n"
                         "}")

'''DARK THEME STYLES'''

dark_previewWindow_styles = 'QMainWindow#Form{background: #232323;}' \
                            "QLabel{" \
                            "position: absolute;" \
                            "background: #444444;" \
                            "border-radius: 25px;" \
                            "font-family: 'Inter';" \
                            "font-style: normal;\n" \
                            "font-weight: 400;\n" \
                            "font-size: 32px;\n" \
                            "line-height: 39px;\n" \
                            "text-align: center;\n" \
                            "color: #F3F3F3;" \
                            "}" \
                            "QPushButton{" \
                            "position: absolute;\n" \
                            "background: #F3F3F3;\n" \
                            "border-radius: 25px;\n" \
                            "font-family: \'Inter\';\n" \
                            "font-style: normal;\n" \
                            "font-weight: 400;\n" \
                            "font-size: 32px;\n" \
                            "line-height: 39px;\n" \
                            "text-align: center;\n" \
                            "color: #232323;\n" \
                            "}" \
                            "QPushButton:hover{" \
                            "position: absolute;\n" \
                            "background: #686868;\n" \
                            "border-radius: 25px;\n" \
                            "font-family: \'Inter\';\n" \
                            "font-style: normal;\n" \
                            "font-weight: 400;\n" \
                            "font-size: 32px;\n" \
                            "line-height: 39px;\n" \
                            "text-align: center;\n" \
                            "color: #FAFAFA;\n" \
                            "}"
dark_menuWindow_styles = ('QMainWindow#Form{background: #232323;}'
                          "QListWidget{"
                          "position: absolute;\n"
                          "border: None;\n"
                          "background: #444444;\n"
                          "padding-left: 69px;\n"
                          "padding-right: 69px;\n"
                          "padding-top: 130px;\n"
                          "}"
                          "QListWidget:item {"
                          "padding-top: 28px;\n"
                          "padding-bottom: 28px;\n"
                          "background: #1F1F1F;\n"
                          "border-radius: 25px;\n"
                          "font-family: \'Inter\';\n"
                          "font-style: normal;\n"
                          "font-weight: 400;\n"
                          "font-size: 32px;\n"
                          "line-height: 39px;\n"
                          "text-align: center;\n"
                          "color: #F3F3F3;"
                          "}"
                          "QListWidget:item:hover{\n"
                          "padding-top: 28px;\n"
                          "padding-bottom: 28px;\n"
                          "background: #AFAFAF;\n"
                          "border-radius: 25px;\n"
                          "font-family: \'Inter\';\n"
                          "font-style: normal;\n"
                          "font-weight: 400;\n"
                          "font-size: 32px;\n"
                          "line-height: 39px;\n"
                          "text-align: center;\n"
                          "color: #000000;"
                          "}"
                          "QListWidget:item:selected{\n"
                          "padding-top: 28px;\n"
                          "padding-bottom: 28px;\n"
                          "border: 2px ridge #000000;\n"
                          "background: #FAFAFA;\n"
                          "border-radius: 25px;\n"
                          "font-family: \'Inter\';\n"
                          "font-style: normal;\n"
                          "font-weight: 400;\n"
                          "font-size: 32px;\n"
                          "line-height: 39px;\n"
                          "text-align: center;\n"
                          "color: #000000;"
                          "}"
                          "QLabel{position: absolute;\n"
                          "background: transparent;\n"
                          "font-family: \'Inter\';\n"
                          "font-style: normal;\n"
                          "font-weight: 400;\n"
                          "font-size: 32px;\n"
                          "line-height: 39px;\n"
                          "text-align: center;\n"
                          "color: #FAFAFA;"
                          "}"
                          'QPushButton{'
                          'background: #9E9E9E;'
                          ' border-radius: 25px;'
                          'font-family: "Inter";'
                          'font-style: normal;'
                          'font-weight: 400;'
                          'font-size: 32px;'
                          'line-height: 39px;'
                          'text-align: center;'
                          'color: #000000;'
                          '}'
                          'QPushButton:hover{'
                          'background: #F1F1F1;'
                          'border-radius: 25px;'
                          'position: absolute;'
                          'font-family: "Inter";'
                          'font-style: normal;'
                          'font-weight: 400;'
                          'font-size: 32px;'
                          'line-height: 39px;'
                          'text-align: center;'
                          'color: #000000;'
                          '}')
dark_writingWindow_styles = ('QMainWindow#Form{background: #232323;}'
                             'QPushButton{'
                             'background: #444444;'
                             ' border-radius: 25px;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'text-align: center;'
                             'color: #F1F1F1;'
                             '}'
                             'QPushButton:hover{'
                             'background: #9E9E9E;'
                             'border-radius: 25px;'
                             'position: absolute;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'text-align: center;'
                             'color: #000000;'
                             '}'
                             'QPushButton#startButton{'
                             'background: #F1F1F1;'
                             'border-radius: 25px;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'text-align: center;'
                             'color: #232323;'
                             '}'
                             'QPushButton#startButton:hover{'
                             'background: #9E9E9E;'
                             'border-radius: 25px;'
                             'position: absolute;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'text-align: center;'
                             'color: #202020;'
                             '}'
                             'QLabel{'
                             'position: absolute;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'color: #9E9E9E;'
                             '}'
                             'QLabel#currentLineView{'
                             'position: absolute;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'color: #FFFFFF;'
                             '}'
                             'QLabel#timerView{'
                             'position: absolute;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'color: #F3F3F3;}'
                             'QLineEdit{'
                             'position: absolute;'
                             'border: 2px solid transparent;'
                             'border-bottom: 3px ridge #F3F3F3;'
                             'background-color: transparent;'
                             'font-family: "Inter";'
                             'font-style: normal;'
                             'font-weight: 400;'
                             'font-size: 32px;'
                             'line-height: 39px;'
                             'color: #F3F3F3;}')
dark_loginWindow_styles = ('QMainWindow#Form{background: #232323;}'
                           'QLabel{'
                           'position: absolute;'
                           'background: #444444;'
                           'border-radius: 25px;'
                           'font-family: \'Inter\';'
                           "font-style: normal;"
                           "font-weight: 400;"
                           "font-size: 32px;"
                           "line-height: 39px;"
                           "text-align: center;"
                           'color: #F1F1F1;}'
                           'QPushButton{'
                           "position: absolute;\n"
                           "background: #F1F1F1;\n"
                           "border-radius: 25px;\n"
                           "font-family: \'Inter\';\n"
                           "font-style: normal;\n"
                           "font-weight: 400;\n"
                           "font-size: 32px;\n"
                           "line-height: 39px;\n"
                           "text-align: center;\n"
                           "color: #232323;\n"
                           "}"
                           "QPushButton:hover{"
                           "position: absolute;\n"
                           "background: #9E9E9E;\n"
                           'border: 3px solid #444444;'
                           "border-radius: 25px;\n"
                           "font-family: \'Inter\';\n"
                           "font-style: normal;\n"
                           "font-weight: 400;\n"
                           "font-size: 32px;\n"
                           "line-height: 39px;\n"
                           "text-align: center;\n"
                           "color: #232323;\n"
                           '}'
                           'QLineEdit{position: absolute;'
                           'border: 2px solid transparent;'
                           'border-bottom: 2px ridge #F3F3F3;'
                           'background: transparent;'
                           'font-family: "Inter";'
                           'font-style: normal;'
                           'font-weight: 400;'
                           'font-size: 32px;'
                           'line-height: 39px;'
                           'text-align: center;'
                           'color: #F3F3F3;}')
dark_settingsWindow_styles = ('QMainWindow#Form{background: #232323;}'
                              "QLabel#label_2 {"
                              "position: absolute;\n"
                              "background: #9E9E9E;\n"
                              "border-radius: 25px;\n"
                              "padding-left: 40px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #000000;"
                              "}"
                              "QLabel#label_2:hover{"
                              "position: absolute;\n"
                              "background: #696969;\n"
                              "border-radius: 25px;\n"
                              "padding-left: 40px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #000000;"
                              "}"

                              "QLabel#label_3 {"
                              "position: absolute;\n"
                              "background: #9E9E9E;\n"
                              "border-radius: 25px;\n"
                              "padding-left: 40px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #000000;"
                              "}"
                              "QLabel#label_3:hover{"
                              "position: absolute;\n"
                              "background: #696969;\n"
                              "border-radius: 25px;\n"
                              "padding-left: 40px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #000000;"
                              "}"
                              "QLabel#averageTimeView{position: absolute;"
                              'font-family: "Inter";'
                              'font-style: normal;'
                              'font-weight: 400;'
                              'font-size: 32px;'
                              'line-height: 39px;'
                              'text-align: center;'
                              'color: #F3F3F3;'
                              '}'
                              'QLabel#label{'
                              'position: absolute;'
                              "background: #444444;\n"
                              "padding-bottom: 880px;"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              'color: #F3F3F3;'
                              '}'
                              "QPushButton {"
                              "position: absolute;\n"
                              "background: #232323;\n"
                              "border-radius: 25px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #DFDFDF;"
                              "}"
                              "QPushButton:hover {"
                              "position: absolute;\n"
                              "background: #9E9E9E;\n"
                              "border-radius: 25px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #202020"
                              "}"
                              "QPushButton#signOut {\n"
                              "position: absolute;\n"
                              "background: #232323;\n"
                              "border-radius: 25px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #FF3838;\n"
                              "}\n"
                              "QPushButton#signOut:hover{\n"
                              "position: absolute;\n"
                              "background: #232323;\n"
                              "border: 3px solid #FF3838;\n"
                              "border-radius: 25px;\n"
                              "font-family: \'Inter\';\n"
                              "font-style: normal;\n"
                              "font-weight: 400;\n"
                              "font-size: 32px;\n"
                              "line-height: 39px;\n"
                              "text-align: center;\n"
                              "color: #FF3838;\n"
                              "}"
                              'QLabel#quit{background-image: url(icons/dark-arrow.png};')

'''DARK THEME STYLES END'''

BASE_URL = 'https://stihi.ru'

maxTime = 3600000

MAXSTRING = 75

GOOD_WORDS = ['Отлично!', 'Очень хорошо!', 'Так держать!']

ENCODING = 'utf-8'

default_settings = {"darkTheme": False, "letterIgnore": False}
default_account = {"is_logined": False, "name": "name"}


class Pic(QtWidgets.QLabel):
    click = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(ev)
        self.click.emit()
