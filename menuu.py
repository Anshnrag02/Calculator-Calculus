from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuwin(object):
    def setupUi(self, menuwin):
        menuwin.setObjectName("menuwin")
        menuwin.resize(1143, 768)
        menuwin.setStyleSheet("background-image: url(:/newPrefix/test9.png);")
        self.menu = QtWidgets.QWidget(menuwin)
        self.menu.setStyleSheet("")
        self.menu.setObjectName("menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menubtn_dni_2 = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubtn_dni_2.sizePolicy().hasHeightForWidth())
        self.menubtn_dni_2.setSizePolicy(sizePolicy)
        self.menubtn_dni_2.setStyleSheet("QPushButton{\n"
"   background: transparent;\n"
"   font: 87 40pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   \n"
"   \n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background: transparent;\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.menubtn_dni_2.setObjectName("menubtn_dni_2")
        self.verticalLayout.addWidget(self.menubtn_dni_2)
        self.menubtn_dni_3 = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubtn_dni_3.sizePolicy().hasHeightForWidth())
        self.menubtn_dni_3.setSizePolicy(sizePolicy)
        self.menubtn_dni_3.setStyleSheet("QPushButton{\n"
"   background: transparent;\n"
"   font: 87 40pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   \n"
"   \n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background: transparent;\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.menubtn_dni_3.setObjectName("menubtn_dni_3")
        self.verticalLayout.addWidget(self.menubtn_dni_3)
        self.menubtn_dni_4 = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubtn_dni_4.sizePolicy().hasHeightForWidth())
        self.menubtn_dni_4.setSizePolicy(sizePolicy)
        self.menubtn_dni_4.setStyleSheet("QPushButton{\n"
"   background: transparent;\n"
"   font: 87 40pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   \n"
"   \n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background: transparent;\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.menubtn_dni_4.setObjectName("menubtn_dni_4")
        self.verticalLayout.addWidget(self.menubtn_dni_4)
        self.menubtn_dni = QtWidgets.QPushButton(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubtn_dni.sizePolicy().hasHeightForWidth())
        self.menubtn_dni.setSizePolicy(sizePolicy)
        self.menubtn_dni.setStyleSheet("QPushButton{\n"
"   background: transparent;\n"
"   font: 87 40pt \"Arial Black\";\n"
"   color: rgb(255, 255, 255);\n"
"   \n"
"   \n"
"   border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"    border: 5px solid white\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background: transparent;\n"
"    color: rgb(255,255,255);\n"
"border: 0px solid white\n"
"}\n"
"\n"
"")
        self.menubtn_dni.setObjectName("menubtn_dni")
        self.verticalLayout.addWidget(self.menubtn_dni)
        menuwin.setCentralWidget(self.menu)

        self.retranslateUi(menuwin)
        QtCore.QMetaObject.connectSlotsByName(menuwin)

    def retranslateUi(self, menuwin):
        _translate = QtCore.QCoreApplication.translate
        menuwin.setWindowTitle(_translate("menuwin", "MainWindow"))
        self.menubtn_dni_2.setText(_translate("menuwin", "Differentiation and Integration"))
        self.menubtn_dni_3.setText(_translate("menuwin", "Limits"))
        self.menubtn_dni_4.setText(_translate("menuwin", "Root Finder"))
        self.menubtn_dni.setText(_translate("menuwin", "History"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuwin = QtWidgets.QMainWindow()
    ui = Ui_menuwin()
    ui.setupUi(menuwin)
    menuwin.show()
    sys.exit(app.exec_())
