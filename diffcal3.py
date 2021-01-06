from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dniwindow(object):
    def setupUi(self, dniwindow):
        dniwindow.setObjectName("dniwindow")
        dniwindow.resize(900, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dniwindow.sizePolicy().hasHeightForWidth())
        dniwindow.setSizePolicy(sizePolicy)
        dniwindow.setAutoFillBackground(False)
        dniwindow.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.diffandintcal = QtWidgets.QWidget(dniwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diffandintcal.sizePolicy().hasHeightForWidth())
        self.diffandintcal.setSizePolicy(sizePolicy)
        self.diffandintcal.setStyleSheet("\n"
"QMainWindow::centralWidget()->layout()->setContentsMargins(0,0,0,0);")
        self.diffandintcal.setObjectName("diffandintcal")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.diffandintcal)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.dframe_main = QtWidgets.QFrame(self.diffandintcal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dframe_main.sizePolicy().hasHeightForWidth())
        self.dframe_main.setSizePolicy(sizePolicy)
        self.dframe_main.setStyleSheet("background-color: rgb(26,26,26);")
        self.dframe_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dframe_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dframe_main.setObjectName("dframe_main")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dframe_main)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dfram_cal = QtWidgets.QFrame(self.dframe_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dfram_cal.sizePolicy().hasHeightForWidth())
        self.dfram_cal.setSizePolicy(sizePolicy)
        self.dfram_cal.setMinimumSize(QtCore.QSize(800, 400))
        self.dfram_cal.setStyleSheet("color: rgb(0, 0, 0);")
        self.dfram_cal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dfram_cal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dfram_cal.setObjectName("dfram_cal")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dfram_cal)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dgrid = QtWidgets.QGridLayout()
        self.dgrid.setObjectName("dgrid")
        self.dbtn_3 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_3.sizePolicy().hasHeightForWidth())
        self.dbtn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_3.setFont(font)
        self.dbtn_3.setStyleSheet("QPushButton{\n"
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
        self.dbtn_3.setShortcut("")
        self.dbtn_3.setObjectName("dbtn_3")
        self.dgrid.addWidget(self.dbtn_3, 1, 5, 1, 1)
        self.dbtn_icos = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_icos.sizePolicy().hasHeightForWidth())
        self.dbtn_icos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_icos.setFont(font)
        self.dbtn_icos.setStyleSheet("QPushButton{\n"
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
        self.dbtn_icos.setObjectName("dbtn_icos")
        self.dgrid.addWidget(self.dbtn_icos, 2, 1, 1, 1)
        self.dbtn_rc = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_rc.sizePolicy().hasHeightForWidth())
        self.dbtn_rc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_rc.setFont(font)
        self.dbtn_rc.setStyleSheet("QPushButton{\n"
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
        self.dbtn_rc.setObjectName("dbtn_rc")
        self.dgrid.addWidget(self.dbtn_rc, 4, 2, 1, 1)
        self.dbtn_0 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_0.sizePolicy().hasHeightForWidth())
        self.dbtn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_0.setFont(font)
        self.dbtn_0.setStyleSheet("QPushButton{\n"
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
        self.dbtn_0.setObjectName("dbtn_0")
        self.dgrid.addWidget(self.dbtn_0, 4, 4, 1, 1)
        self.dbtn_div = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_div.sizePolicy().hasHeightForWidth())
        self.dbtn_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_div.setFont(font)
        self.dbtn_div.setStyleSheet("QPushButton{\n"
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
        self.dbtn_div.setObjectName("dbtn_div")
        self.dgrid.addWidget(self.dbtn_div, 4, 6, 1, 1)
        self.dbtn_x = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_x.sizePolicy().hasHeightForWidth())
        self.dbtn_x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_x.setFont(font)
        self.dbtn_x.setStyleSheet("QPushButton{\n"
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
        self.dbtn_x.setObjectName("dbtn_x")
        self.dgrid.addWidget(self.dbtn_x, 0, 6, 1, 1)
        self.dbtn_1 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_1.sizePolicy().hasHeightForWidth())
        self.dbtn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_1.setFont(font)
        self.dbtn_1.setStyleSheet("QPushButton{\n"
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
        self.dbtn_1.setObjectName("dbtn_1")
        self.dgrid.addWidget(self.dbtn_1, 1, 3, 1, 1)
        self.dbtn_int = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_int.sizePolicy().hasHeightForWidth())
        self.dbtn_int.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_int.setFont(font)
        self.dbtn_int.setStyleSheet("QPushButton{\n"
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
        self.dbtn_int.setObjectName("dbtn_int")
        self.dgrid.addWidget(self.dbtn_int, 0, 3, 1, 3)
        self.dbtn_cos = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_cos.sizePolicy().hasHeightForWidth())
        self.dbtn_cos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_cos.setFont(font)
        self.dbtn_cos.setStyleSheet("QPushButton{\n"
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
        self.dbtn_cos.setObjectName("dbtn_cos")
        self.dgrid.addWidget(self.dbtn_cos, 1, 1, 1, 1)
        self.dbtn_add = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_add.sizePolicy().hasHeightForWidth())
        self.dbtn_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_add.setFont(font)
        self.dbtn_add.setStyleSheet("QPushButton{\n"
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
        self.dbtn_add.setObjectName("dbtn_add")
        self.dgrid.addWidget(self.dbtn_add, 1, 6, 1, 1)
        self.dbtn_subt = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_subt.sizePolicy().hasHeightForWidth())
        self.dbtn_subt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_subt.setFont(font)
        self.dbtn_subt.setStyleSheet("QPushButton{\n"
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
        self.dbtn_subt.setObjectName("dbtn_subt")
        self.dgrid.addWidget(self.dbtn_subt, 2, 6, 1, 1)
        self.dbtn_5 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_5.sizePolicy().hasHeightForWidth())
        self.dbtn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_5.setFont(font)
        self.dbtn_5.setStyleSheet("QPushButton{\n"
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
        self.dbtn_5.setShortcut("")
        self.dbtn_5.setObjectName("dbtn_5")
        self.dgrid.addWidget(self.dbtn_5, 2, 4, 1, 1)
        self.dbtn_mul = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_mul.sizePolicy().hasHeightForWidth())
        self.dbtn_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_mul.setFont(font)
        self.dbtn_mul.setStyleSheet("QPushButton{\n"
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
        self.dbtn_mul.setObjectName("dbtn_mul")
        self.dgrid.addWidget(self.dbtn_mul, 3, 6, 1, 1)
        self.dbtn_sin = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_sin.sizePolicy().hasHeightForWidth())
        self.dbtn_sin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_sin.setFont(font)
        self.dbtn_sin.setStyleSheet("QPushButton{\n"
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
        self.dbtn_sin.setObjectName("dbtn_sin")
        self.dgrid.addWidget(self.dbtn_sin, 1, 0, 1, 1)
        self.dbtn_tan = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_tan.sizePolicy().hasHeightForWidth())
        self.dbtn_tan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_tan.setFont(font)
        self.dbtn_tan.setStyleSheet("QPushButton{\n"
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
        self.dbtn_tan.setObjectName("dbtn_tan")
        self.dgrid.addWidget(self.dbtn_tan, 1, 2, 1, 1)
        self.dbtn_2 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_2.sizePolicy().hasHeightForWidth())
        self.dbtn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_2.setFont(font)
        self.dbtn_2.setStyleSheet("QPushButton{\n"
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
        self.dbtn_2.setShortcut("")
        self.dbtn_2.setObjectName("dbtn_2")
        self.dgrid.addWidget(self.dbtn_2, 1, 4, 1, 1)
        self.dbtn_isin = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_isin.sizePolicy().hasHeightForWidth())
        self.dbtn_isin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_isin.setFont(font)
        self.dbtn_isin.setStyleSheet("QPushButton{\n"
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
        self.dbtn_isin.setObjectName("dbtn_isin")
        self.dgrid.addWidget(self.dbtn_isin, 2, 0, 1, 1)
        self.dbtn_itan = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_itan.sizePolicy().hasHeightForWidth())
        self.dbtn_itan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_itan.setFont(font)
        self.dbtn_itan.setStyleSheet("QPushButton{\n"
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
        self.dbtn_itan.setObjectName("dbtn_itan")
        self.dgrid.addWidget(self.dbtn_itan, 2, 2, 1, 1)
        self.dbtn_lc = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_lc.sizePolicy().hasHeightForWidth())
        self.dbtn_lc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_lc.setFont(font)
        self.dbtn_lc.setStyleSheet("QPushButton{\n"
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
        self.dbtn_lc.setObjectName("dbtn_lc")
        self.dgrid.addWidget(self.dbtn_lc, 4, 1, 1, 1)
        self.dbtn_log = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_log.sizePolicy().hasHeightForWidth())
        self.dbtn_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_log.setFont(font)
        self.dbtn_log.setStyleSheet("QPushButton{\n"
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
        self.dbtn_log.setObjectName("dbtn_log")
        self.dgrid.addWidget(self.dbtn_log, 3, 1, 1, 1)
        self.dbtn_4 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_4.sizePolicy().hasHeightForWidth())
        self.dbtn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_4.setFont(font)
        self.dbtn_4.setStyleSheet("QPushButton{\n"
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
        self.dbtn_4.setShortcut("")
        self.dbtn_4.setObjectName("dbtn_4")
        self.dgrid.addWidget(self.dbtn_4, 2, 3, 1, 1)
        self.dbtn_e = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_e.sizePolicy().hasHeightForWidth())
        self.dbtn_e.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_e.setFont(font)
        self.dbtn_e.setStyleSheet("QPushButton{\n"
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
        self.dbtn_e.setObjectName("dbtn_e")
        self.dgrid.addWidget(self.dbtn_e, 3, 0, 1, 1)
        self.dbtn_6 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_6.sizePolicy().hasHeightForWidth())
        self.dbtn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_6.setFont(font)
        self.dbtn_6.setStyleSheet("QPushButton{\n"
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
        self.dbtn_6.setShortcut("")
        self.dbtn_6.setObjectName("dbtn_6")
        self.dgrid.addWidget(self.dbtn_6, 2, 5, 1, 1)
        self.dbtn_7 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_7.sizePolicy().hasHeightForWidth())
        self.dbtn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_7.setFont(font)
        self.dbtn_7.setStyleSheet("QPushButton{\n"
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
        self.dbtn_7.setObjectName("dbtn_7")
        self.dgrid.addWidget(self.dbtn_7, 3, 3, 1, 1)
        self.dbtn_pow = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_pow.sizePolicy().hasHeightForWidth())
        self.dbtn_pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_pow.setFont(font)
        self.dbtn_pow.setStyleSheet("QPushButton{\n"
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
        self.dbtn_pow.setObjectName("dbtn_pow")
        self.dgrid.addWidget(self.dbtn_pow, 3, 2, 1, 1)
        self.dbtn_diff = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_diff.sizePolicy().hasHeightForWidth())
        self.dbtn_diff.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_diff.setFont(font)
        self.dbtn_diff.setStyleSheet("QPushButton{\n"
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
        self.dbtn_diff.setObjectName("dbtn_diff")
        self.dgrid.addWidget(self.dbtn_diff, 0, 0, 1, 3)
        self.dbtn_8 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_8.sizePolicy().hasHeightForWidth())
        self.dbtn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_8.setFont(font)
        self.dbtn_8.setStyleSheet("QPushButton{\n"
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
        self.dbtn_8.setObjectName("dbtn_8")
        self.dgrid.addWidget(self.dbtn_8, 3, 4, 1, 1)
        self.dbtn_9 = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_9.sizePolicy().hasHeightForWidth())
        self.dbtn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_9.setFont(font)
        self.dbtn_9.setStyleSheet("QPushButton{\n"
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
        self.dbtn_9.setObjectName("dbtn_9")
        self.dgrid.addWidget(self.dbtn_9, 3, 5, 1, 1)
        self.dbtn_C = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_C.sizePolicy().hasHeightForWidth())
        self.dbtn_C.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_C.setFont(font)
        self.dbtn_C.setStyleSheet("QPushButton{\n"
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
        self.dbtn_C.setObjectName("dbtn_C")
        self.dgrid.addWidget(self.dbtn_C, 4, 3, 1, 1)
        self.dbtn_back = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_back.sizePolicy().hasHeightForWidth())
        self.dbtn_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_back.setFont(font)
        self.dbtn_back.setStyleSheet("QPushButton{\n"
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
        self.dbtn_back.setObjectName("dbtn_back")
        self.dgrid.addWidget(self.dbtn_back, 4, 5, 1, 1)
        self.dbtn_exit = QtWidgets.QPushButton(self.dfram_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn_exit.sizePolicy().hasHeightForWidth())
        self.dbtn_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dbtn_exit.setFont(font)
        self.dbtn_exit.setStyleSheet("QPushButton{\n"
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
        self.dbtn_exit.setObjectName("dbtn_exit")
        self.dgrid.addWidget(self.dbtn_exit, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.dgrid, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.dfram_cal, 2, 0, 1, 1)
        self.dframe_input = QtWidgets.QFrame(self.dframe_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dframe_input.sizePolicy().hasHeightForWidth())
        self.dframe_input.setSizePolicy(sizePolicy)
        self.dframe_input.setStyleSheet("color: rgb(0, 0, 0);")
        self.dframe_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dframe_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dframe_input.setObjectName("dframe_input")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dframe_input)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dinput = QtWidgets.QLineEdit(self.dframe_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dinput.sizePolicy().hasHeightForWidth())
        self.dinput.setSizePolicy(sizePolicy)
        self.dinput.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.dinput.setFont(font)
        self.dinput.setStyleSheet("color: rgb(255, 255, 255);")
        self.dinput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dinput.setObjectName("dinput")
        self.gridLayout_4.addWidget(self.dinput, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.dframe_input, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.dframe_main, 0, 0, 1, 1)
        dniwindow.setCentralWidget(self.diffandintcal)
        self.statusbar = QtWidgets.QStatusBar(dniwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        dniwindow.setStatusBar(self.statusbar)

        self.retranslateUi(dniwindow)
        QtCore.QMetaObject.connectSlotsByName(dniwindow)

    def retranslateUi(self, dniwindow):
        _translate = QtCore.QCoreApplication.translate
        dniwindow.setWindowTitle(_translate("dniwindow", "Differentiaion and Integration"))
        self.dbtn_3.setText(_translate("dniwindow", "3"))
        self.dbtn_icos.setText(_translate("dniwindow", "acos( )"))
        self.dbtn_rc.setText(_translate("dniwindow", ")"))
        self.dbtn_rc.setShortcut(_translate("dniwindow", ")"))
        self.dbtn_0.setText(_translate("dniwindow", "0"))
        self.dbtn_0.setShortcut(_translate("dniwindow", "0"))
        self.dbtn_div.setText(_translate("dniwindow", "÷"))
        self.dbtn_div.setShortcut(_translate("dniwindow", "/"))
        self.dbtn_x.setText(_translate("dniwindow", "X"))
        self.dbtn_x.setShortcut(_translate("dniwindow", "X"))
        self.dbtn_1.setText(_translate("dniwindow", "1"))
        self.dbtn_1.setShortcut(_translate("dniwindow", "1"))
        self.dbtn_int.setText(_translate("dniwindow", "Integrate"))
        self.dbtn_cos.setText(_translate("dniwindow", "cos( )"))
        self.dbtn_add.setText(_translate("dniwindow", "+"))
        self.dbtn_add.setShortcut(_translate("dniwindow", "+"))
        self.dbtn_subt.setText(_translate("dniwindow", "-"))
        self.dbtn_subt.setShortcut(_translate("dniwindow", "-"))
        self.dbtn_5.setText(_translate("dniwindow", "5"))
        self.dbtn_mul.setText(_translate("dniwindow", "×"))
        self.dbtn_mul.setShortcut(_translate("dniwindow", "*"))
        self.dbtn_sin.setText(_translate("dniwindow", "sin( )"))
        self.dbtn_tan.setText(_translate("dniwindow", "tan( )"))
        self.dbtn_2.setText(_translate("dniwindow", "2"))
        self.dbtn_isin.setText(_translate("dniwindow", "asin( )"))
        self.dbtn_itan.setText(_translate("dniwindow", "atan( )"))
        self.dbtn_lc.setText(_translate("dniwindow", "("))
        self.dbtn_lc.setShortcut(_translate("dniwindow", "("))
        self.dbtn_log.setText(_translate("dniwindow", "log()"))
        self.dbtn_4.setText(_translate("dniwindow", "4"))
        self.dbtn_e.setText(_translate("dniwindow", "e"))
        self.dbtn_e.setShortcut(_translate("dniwindow", "E"))
        self.dbtn_6.setText(_translate("dniwindow", "6"))
        self.dbtn_7.setText(_translate("dniwindow", "7"))
        self.dbtn_pow.setText(_translate("dniwindow", "x^y"))
        self.dbtn_pow.setShortcut(_translate("dniwindow", "^"))
        self.dbtn_diff.setText(_translate("dniwindow", "Differentiate"))
        self.dbtn_8.setText(_translate("dniwindow", "8"))
        self.dbtn_8.setShortcut(_translate("dniwindow", "8"))
        self.dbtn_9.setText(_translate("dniwindow", "9"))
        self.dbtn_C.setText(_translate("dniwindow", "C"))
        self.dbtn_back.setText(_translate("dniwindow", "⌫"))
        self.dbtn_back.setShortcut(_translate("dniwindow", "Backspace"))
        self.dbtn_exit.setText(_translate("dniwindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dniwindow = QtWidgets.QMainWindow()
    ui = Ui_dniwindow()
    ui.setupUi(dniwindow)
    dniwindow.show()
    sys.exit(app.exec_())
