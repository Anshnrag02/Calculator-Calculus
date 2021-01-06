from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_limwin(object):
    def setupUi(self, limwin):
        limwin.setObjectName("limwin")
        limwin.resize(900, 768)
        limwin.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.limwidget = QtWidgets.QWidget(limwin)
        self.limwidget.setObjectName("limwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.limwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.limframe_main = QtWidgets.QFrame(self.limwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limframe_main.sizePolicy().hasHeightForWidth())
        self.limframe_main.setSizePolicy(sizePolicy)
        self.limframe_main.setStyleSheet("background-color: rgb(26,26,26);")
        self.limframe_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.limframe_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.limframe_main.setObjectName("limframe_main")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.limframe_main)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(0, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        self.limfram_cal = QtWidgets.QFrame(self.limframe_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limfram_cal.sizePolicy().hasHeightForWidth())
        self.limfram_cal.setSizePolicy(sizePolicy)
        self.limfram_cal.setMinimumSize(QtCore.QSize(0, 300))
        self.limfram_cal.setStyleSheet("color: rgb(0, 0, 0);")
        self.limfram_cal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.limfram_cal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.limfram_cal.setObjectName("limfram_cal")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.limfram_cal)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.limgrid = QtWidgets.QGridLayout()
        self.limgrid.setObjectName("limgrid")
        self.limbtn_pow = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_pow.sizePolicy().hasHeightForWidth())
        self.limbtn_pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_pow.setFont(font)
        self.limbtn_pow.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_pow.setObjectName("limbtn_pow")
        self.limgrid.addWidget(self.limbtn_pow, 3, 2, 1, 1)
        self.limbtn_7 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_7.sizePolicy().hasHeightForWidth())
        self.limbtn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_7.setFont(font)
        self.limbtn_7.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_7.setObjectName("limbtn_7")
        self.limgrid.addWidget(self.limbtn_7, 3, 3, 1, 1)
        self.limbtn_8 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_8.sizePolicy().hasHeightForWidth())
        self.limbtn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_8.setFont(font)
        self.limbtn_8.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_8.setObjectName("limbtn_8")
        self.limgrid.addWidget(self.limbtn_8, 3, 4, 1, 1)
        self.limbtn_C = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_C.sizePolicy().hasHeightForWidth())
        self.limbtn_C.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_C.setFont(font)
        self.limbtn_C.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_C.setObjectName("limbtn_C")
        self.limgrid.addWidget(self.limbtn_C, 4, 3, 1, 1)
        self.limbtn_back = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_back.sizePolicy().hasHeightForWidth())
        self.limbtn_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_back.setFont(font)
        self.limbtn_back.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_back.setObjectName("limbtn_back")
        self.limgrid.addWidget(self.limbtn_back, 4, 5, 1, 1)
        self.limbtn_9 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_9.sizePolicy().hasHeightForWidth())
        self.limbtn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_9.setFont(font)
        self.limbtn_9.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_9.setObjectName("limbtn_9")
        self.limgrid.addWidget(self.limbtn_9, 3, 5, 1, 1)
        self.limbtn_exit = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_exit.sizePolicy().hasHeightForWidth())
        self.limbtn_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_exit.setFont(font)
        self.limbtn_exit.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_exit.setObjectName("limbtn_exit")
        self.limgrid.addWidget(self.limbtn_exit, 4, 0, 1, 1)
        self.limbtn_rc = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_rc.sizePolicy().hasHeightForWidth())
        self.limbtn_rc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_rc.setFont(font)
        self.limbtn_rc.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_rc.setObjectName("limbtn_rc")
        self.limgrid.addWidget(self.limbtn_rc, 4, 2, 1, 1)
        self.limbtn_0 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_0.sizePolicy().hasHeightForWidth())
        self.limbtn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_0.setFont(font)
        self.limbtn_0.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_0.setObjectName("limbtn_0")
        self.limgrid.addWidget(self.limbtn_0, 4, 4, 1, 1)
        self.limbtn_3 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_3.sizePolicy().hasHeightForWidth())
        self.limbtn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_3.setFont(font)
        self.limbtn_3.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_3.setShortcut("")
        self.limbtn_3.setObjectName("limbtn_3")
        self.limgrid.addWidget(self.limbtn_3, 1, 5, 1, 1)
        self.limbtn_icos = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_icos.sizePolicy().hasHeightForWidth())
        self.limbtn_icos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_icos.setFont(font)
        self.limbtn_icos.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_icos.setObjectName("limbtn_icos")
        self.limgrid.addWidget(self.limbtn_icos, 2, 1, 1, 1)
        self.limbtn_mul = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_mul.sizePolicy().hasHeightForWidth())
        self.limbtn_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_mul.setFont(font)
        self.limbtn_mul.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_mul.setObjectName("limbtn_mul")
        self.limgrid.addWidget(self.limbtn_mul, 3, 6, 1, 1)
        self.limbtn_x = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_x.sizePolicy().hasHeightForWidth())
        self.limbtn_x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_x.setFont(font)
        self.limbtn_x.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_x.setObjectName("limbtn_x")
        self.limgrid.addWidget(self.limbtn_x, 0, 6, 1, 1)
        self.limbtn_div = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_div.sizePolicy().hasHeightForWidth())
        self.limbtn_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_div.setFont(font)
        self.limbtn_div.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_div.setObjectName("limbtn_div")
        self.limgrid.addWidget(self.limbtn_div, 4, 6, 1, 1)
        self.limbtn_sin = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_sin.sizePolicy().hasHeightForWidth())
        self.limbtn_sin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_sin.setFont(font)
        self.limbtn_sin.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_sin.setObjectName("limbtn_sin")
        self.limgrid.addWidget(self.limbtn_sin, 1, 0, 1, 1)
        self.limbtn_2 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_2.sizePolicy().hasHeightForWidth())
        self.limbtn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_2.setFont(font)
        self.limbtn_2.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_2.setShortcut("")
        self.limbtn_2.setObjectName("limbtn_2")
        self.limgrid.addWidget(self.limbtn_2, 1, 4, 1, 1)
        self.limbtn_tan = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_tan.sizePolicy().hasHeightForWidth())
        self.limbtn_tan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_tan.setFont(font)
        self.limbtn_tan.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_tan.setObjectName("limbtn_tan")
        self.limgrid.addWidget(self.limbtn_tan, 1, 2, 1, 1)
        self.limbtn_isin = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_isin.sizePolicy().hasHeightForWidth())
        self.limbtn_isin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_isin.setFont(font)
        self.limbtn_isin.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_isin.setObjectName("limbtn_isin")
        self.limgrid.addWidget(self.limbtn_isin, 2, 0, 1, 1)
        self.limbtn_lc = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_lc.sizePolicy().hasHeightForWidth())
        self.limbtn_lc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_lc.setFont(font)
        self.limbtn_lc.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_lc.setObjectName("limbtn_lc")
        self.limgrid.addWidget(self.limbtn_lc, 4, 1, 1, 1)
        self.limbtn_log = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_log.sizePolicy().hasHeightForWidth())
        self.limbtn_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_log.setFont(font)
        self.limbtn_log.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_log.setObjectName("limbtn_log")
        self.limgrid.addWidget(self.limbtn_log, 3, 1, 1, 1)
        self.limbtn_itan = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_itan.sizePolicy().hasHeightForWidth())
        self.limbtn_itan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_itan.setFont(font)
        self.limbtn_itan.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_itan.setObjectName("limbtn_itan")
        self.limgrid.addWidget(self.limbtn_itan, 2, 2, 1, 1)
        self.limbtn_6 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_6.sizePolicy().hasHeightForWidth())
        self.limbtn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_6.setFont(font)
        self.limbtn_6.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_6.setShortcut("")
        self.limbtn_6.setObjectName("limbtn_6")
        self.limgrid.addWidget(self.limbtn_6, 2, 5, 1, 1)
        self.limbtn_e = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_e.sizePolicy().hasHeightForWidth())
        self.limbtn_e.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_e.setFont(font)
        self.limbtn_e.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_e.setObjectName("limbtn_e")
        self.limgrid.addWidget(self.limbtn_e, 3, 0, 1, 1)
        self.limbtn_4 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_4.sizePolicy().hasHeightForWidth())
        self.limbtn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_4.setFont(font)
        self.limbtn_4.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_4.setShortcut("")
        self.limbtn_4.setObjectName("limbtn_4")
        self.limgrid.addWidget(self.limbtn_4, 2, 3, 1, 1)
        self.limbtn_1 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_1.sizePolicy().hasHeightForWidth())
        self.limbtn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_1.setFont(font)
        self.limbtn_1.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_1.setObjectName("limbtn_1")
        self.limgrid.addWidget(self.limbtn_1, 1, 3, 1, 1)
        self.limbtn_cos = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_cos.sizePolicy().hasHeightForWidth())
        self.limbtn_cos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_cos.setFont(font)
        self.limbtn_cos.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_cos.setObjectName("limbtn_cos")
        self.limgrid.addWidget(self.limbtn_cos, 1, 1, 1, 1)
        self.limbtn_5 = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_5.sizePolicy().hasHeightForWidth())
        self.limbtn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_5.setFont(font)
        self.limbtn_5.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_5.setShortcut("")
        self.limbtn_5.setObjectName("limbtn_5")
        self.limgrid.addWidget(self.limbtn_5, 2, 4, 1, 1)
        self.limbtn_add = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_add.sizePolicy().hasHeightForWidth())
        self.limbtn_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_add.setFont(font)
        self.limbtn_add.setStyleSheet("QPushButton{\n"
"   font: 87 24pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_add.setObjectName("limbtn_add")
        self.limgrid.addWidget(self.limbtn_add, 1, 6, 1, 1)
        self.limbtn_subt = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_subt.sizePolicy().hasHeightForWidth())
        self.limbtn_subt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_subt.setFont(font)
        self.limbtn_subt.setStyleSheet("QPushButton{\n"
"   font: 87 28pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_subt.setObjectName("limbtn_subt")
        self.limgrid.addWidget(self.limbtn_subt, 2, 6, 1, 1)
        self.limbtn_lim = QtWidgets.QPushButton(self.limfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limbtn_lim.sizePolicy().hasHeightForWidth())
        self.limbtn_lim.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.limbtn_lim.setFont(font)
        self.limbtn_lim.setStyleSheet("QPushButton{\n"
"   font: 87 32pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(0, 0, 0);\n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(26, 26, 26);\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.limbtn_lim.setObjectName("limbtn_lim")
        self.limgrid.addWidget(self.limbtn_lim, 0, 0, 1, 6)
        self.gridLayout_3.addLayout(self.limgrid, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.limfram_cal, 2, 0, 1, 1)
        self.limframe_input = QtWidgets.QFrame(self.limframe_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limframe_input.sizePolicy().hasHeightForWidth())
        self.limframe_input.setSizePolicy(sizePolicy)
        self.limframe_input.setMinimumSize(QtCore.QSize(0, 250))
        self.limframe_input.setStyleSheet("color: rgb(0, 0, 0);")
        self.limframe_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.limframe_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.limframe_input.setObjectName("limframe_input")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.limframe_input)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.liminput = QtWidgets.QLineEdit(self.limframe_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liminput.sizePolicy().hasHeightForWidth())
        self.liminput.setSizePolicy(sizePolicy)
        self.liminput.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.liminput.setFont(font)
        self.liminput.setStyleSheet("color: rgb(255, 255, 255);")
        self.liminput.setText("")
        self.liminput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.liminput.setObjectName("liminput")
        self.gridLayout_4.addWidget(self.liminput, 0, 1, 1, 1)
        self.liminput_2 = QtWidgets.QLineEdit(self.limframe_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liminput_2.sizePolicy().hasHeightForWidth())
        self.liminput_2.setSizePolicy(sizePolicy)
        self.liminput_2.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.liminput_2.setFont(font)
        self.liminput_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.liminput_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.liminput_2.setObjectName("liminput_2")
        self.gridLayout_4.addWidget(self.liminput_2, 1, 1, 1, 1)
        self.limfn = QtWidgets.QLabel(self.limframe_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limfn.sizePolicy().hasHeightForWidth())
        self.limfn.setSizePolicy(sizePolicy)
        self.limfn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 24pt \"Arial Black\";")
        self.limfn.setObjectName("limfn")
        self.gridLayout_4.addWidget(self.limfn, 0, 0, 1, 1)
        self.limatpt = QtWidgets.QLabel(self.limframe_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limatpt.sizePolicy().hasHeightForWidth())
        self.limatpt.setSizePolicy(sizePolicy)
        self.limatpt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 24pt \"Arial Black\";")
        self.limatpt.setObjectName("limatpt")
        self.gridLayout_4.addWidget(self.limatpt, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.limframe_input, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.limframe_main, 0, 0, 1, 1)
        limwin.setCentralWidget(self.limwidget)
        self.statusbar = QtWidgets.QStatusBar(limwin)
        self.statusbar.setObjectName("statusbar")
        limwin.setStatusBar(self.statusbar)

        self.retranslateUi(limwin)
        QtCore.QMetaObject.connectSlotsByName(limwin)

    def retranslateUi(self, limwin):
        _translate = QtCore.QCoreApplication.translate
        limwin.setWindowTitle(_translate("limwin", "MainWindow"))
        self.limbtn_pow.setText(_translate("limwin", "x^y"))
        self.limbtn_pow.setShortcut(_translate("limwin", "^"))
        self.limbtn_7.setText(_translate("limwin", "7"))
        self.limbtn_8.setText(_translate("limwin", "8"))
        self.limbtn_8.setShortcut(_translate("limwin", "8"))
        self.limbtn_C.setText(_translate("limwin", "C"))
        self.limbtn_back.setText(_translate("limwin", "⌫"))
        self.limbtn_back.setShortcut(_translate("limwin", "Backspace"))
        self.limbtn_9.setText(_translate("limwin", "9"))
        self.limbtn_exit.setText(_translate("limwin", "Exit"))
        self.limbtn_rc.setText(_translate("limwin", ")"))
        self.limbtn_rc.setShortcut(_translate("limwin", ")"))
        self.limbtn_0.setText(_translate("limwin", "0"))
        self.limbtn_0.setShortcut(_translate("limwin", "0"))
        self.limbtn_3.setText(_translate("limwin", "3"))
        self.limbtn_icos.setText(_translate("limwin", "acos( )"))
        self.limbtn_mul.setText(_translate("limwin", "×"))
        self.limbtn_mul.setShortcut(_translate("limwin", "*"))
        self.limbtn_x.setText(_translate("limwin", "X"))
        self.limbtn_x.setShortcut(_translate("limwin", "X"))
        self.limbtn_div.setText(_translate("limwin", "÷"))
        self.limbtn_div.setShortcut(_translate("limwin", "/"))
        self.limbtn_sin.setText(_translate("limwin", "sin( )"))
        self.limbtn_2.setText(_translate("limwin", "2"))
        self.limbtn_tan.setText(_translate("limwin", "tan( )"))
        self.limbtn_isin.setText(_translate("limwin", "asin( )"))
        self.limbtn_lc.setText(_translate("limwin", "("))
        self.limbtn_lc.setShortcut(_translate("limwin", "("))
        self.limbtn_log.setText(_translate("limwin", "log()"))
        self.limbtn_itan.setText(_translate("limwin", "atan( )"))
        self.limbtn_6.setText(_translate("limwin", "6"))
        self.limbtn_e.setText(_translate("limwin", "e"))
        self.limbtn_e.setShortcut(_translate("limwin", "E"))
        self.limbtn_4.setText(_translate("limwin", "4"))
        self.limbtn_1.setText(_translate("limwin", "1"))
        self.limbtn_1.setShortcut(_translate("limwin", "1"))
        self.limbtn_cos.setText(_translate("limwin", "cos( )"))
        self.limbtn_5.setText(_translate("limwin", "5"))
        self.limbtn_add.setText(_translate("limwin", "+"))
        self.limbtn_add.setShortcut(_translate("limwin", "+"))
        self.limbtn_subt.setText(_translate("limwin", "-"))
        self.limbtn_subt.setShortcut(_translate("limwin", "-"))
        self.limbtn_lim.setText(_translate("limwin", "Limits"))
        self.limfn.setText(_translate("limwin", "FUNCTION"))
        self.limatpt.setText(_translate("limwin", "AT POINT "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    limwin = QtWidgets.QMainWindow()
    ui = Ui_limwin()
    ui.setupUi(limwin)
    limwin.show()
    sys.exit(app.exec_())
