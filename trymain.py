from diffcal3 import Ui_dniwindow
from menuu import Ui_menuwin
from limcal import Ui_limwin
from solvecal import Ui_solvecal
from history import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

import sys

import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')


##################################### Menu Functions ##########################



def open_diffcal():
    MainWindow.show()
    menutry.hide()

def open_limcal():
    limcal.show()
    menutry.hide()

def open_solvecal():
    solvecal.show()
    menutry.hide()

def open_history():
    history.show()
    menutry.hide

################################### History Functions #########################

def loadData():
    con = sqlite3.connect('Project1.db')
    c =  con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS 'history' ('type1'	TEXT,'old'	TEXT,'new'	TEXT)")
    
    result = c.execute("SELECT * FROM history")
    con.commit()
    ui4.tableWidget.setRowCount(0)
    #ui4.tableWidget.setColumnCount(3)
    for row_number,row_data in enumerate(result):
        ui4.tableWidget.insertRow(row_number)
        for colum_number, data in enumerate(row_data):
            ui4.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
def delete():
    con = sqlite3.connect('Project1.db')
    c =  con.cursor()
    c.execute("DELETE FROM history")
    con.commit()


    
   





    
##################################### Diffcal Functions #######################

def open_menu():

    menutry.show()
    MainWindow.hide()

def diff_clicked():
    con = sqlite3.connect('Project1.db')
    c =  con.cursor()

    data = ui.dinput.text()
    old = ui.dinput.text()
    ans=str(sym.diff(data, x))
    new = str(sym.diff(data, x))
    ui.dinput.setText(ans)
    type1 = 'diff'
    c.execute("insert into history values('" + type1 +"','" + old +"','" + new +"')")
    con.commit()

def insert_ddata():
    return
    

def sin_clicked():

    data = ui.dinput.text()
    ui.dinput.setText(data+'sin(x)')

def int_clicked():
    

    data = ui.dinput.text()
    old = ui.dinput.text()
    ans=str(sym.integrate(data, x))
    new = str(sym.integrate(data, x))
    ui.dinput.setText(ans)
    con = sqlite3.connect('Project1.db')
    c =  con.cursor()
    type1 = 'int'
    c.execute("insert into history values('" + type1 +"','" + old +"','" + new +"')")
    con.commit()

def cos_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'cos(x)')

def tan_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'tan()')

def asin_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'asin()')

def acos_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'acos()')

def atan_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'atan()')

def e_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'e')

def log_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'log()')

def x_y_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'**')

def leftbrac_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'(')

def rightbrac_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+')')

def num1_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'1')

def num2_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'2')

def num3_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'3')

def num4_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'4')

def num5_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'5')

def num6_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'6')
    
def num7_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'7')

def num8_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'8')

def num9_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'9')

def num0_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'0')

def x_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'x')

def plus_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'+')

def minus_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'-')

def multiply_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'*')

def divide_clicked():
    data = ui.dinput.text()
    ui.dinput.setText(data+'/')

def back_clicked():
    data = ui.dinput.text()
    data = data[:-1]
    ui.dinput.setText(data)

def clear_clicked():
    data = ""
    ui.dinput.setText(data)

def try123():
    data = ui.dinput.text()
    ui.dinput.setText(data+'tan()')
    len1 = len(data)
    
    ui.dinput.setCursorPosition(len1-1)






################################# Limcal Functions ###########################

def lopen_menu():

    menutry.show()
    limcal.hide()

def limit_clicked():

    data = ui2.liminput.text()
    old = data
    data2 = ui2.liminput_2.text()
    ans=str(sym.limit(data, x, data2))
    new = ans
    ui2.liminput.setText(ans)
    con = sqlite3.connect('Project1.db')
    c =  con.cursor()
    type1 = 'lim'
    c.execute("insert into history values('" + type1 +"','" + old +"','" + new +"')")
    con.commit()


def lsin_clicked():

    data = ui2.liminput.text()
    ui2.liminput.setText(data+'sin(x)')


def lcos_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'cos(x)')

def ltan_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'tan()')

def lasin_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'asin()')

def lacos_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'acos()')

def latan_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'atan()')

def le_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'e')

def llog_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'log()')

def lx_y_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'**')

def lleftbrac_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'(')

def lrightbrac_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+')')

def lnum1_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'1')

def lnum2_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'2')

def lnum3_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'3')

def lnum4_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'4')

def lnum5_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'5')

def lnum6_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'6')
    
def lnum7_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'7')

def lnum8_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'8')

def lnum9_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'9')

def lnum0_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'0')

def lx_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'x')

def lplus_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'+')

def lminus_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'-')

def lmultiply_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'*')

def ldivide_clicked():
    data = ui2.liminput.text()
    ui2.liminput.setText(data+'/')

def lback_clicked():
    data = ui2.liminput.text()
    data = data[:-1]
    ui2.liminput.setText(data)

def lclear_clicked():
    data = ""
    ui2.liminput.setText(data)





################################# Solvecal Functions #########################
    

def sopen_menu():

    menutry.show()
    solvecal.hide()

def solve_clicked():

    data = ui3.lineEdit.text()
    old = data
    ans=str(sym.solveset(data,x))
    new = ans
    ui3.lineEdit.setText(ans)

    con = sqlite3.connect('Project1.db')
    c =  con.cursor()
    type1 = 'root'
    c.execute("insert into history values('" + type1 +"','" + old +"','" + new +"')")
    con.commit()



    
    


################################## Main Window ################################

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_dniwindow()
ui.setupUi(MainWindow)
#MainWindow.show()
menutry = QtWidgets.QMainWindow()
ui1 = Ui_menuwin()
ui1.setupUi(menutry)

limcal = QtWidgets.QMainWindow()
ui2 = Ui_limwin()
ui2.setupUi(limcal)

solvecal = QtWidgets.QMainWindow()
ui3 = Ui_solvecal()
ui3.setupUi(solvecal)
menutry.show()

history = QtWidgets.QMainWindow()
ui4 = Ui_MainWindow()
ui4.setupUi(history)




################################# Menu Buttons ###################################
def his_close():
    menutry.show()
    history.hide()

ui1.menubtn_dni_2.clicked.connect(open_diffcal)
ui1.menubtn_dni_3.clicked.connect(open_limcal)
ui1.menubtn_dni_4.clicked.connect(open_solvecal)
ui1.menubtn_dni.clicked.connect(open_history)
ui1.menubtn_dni.clicked.connect(loadData)
ui4.btn_clear.clicked.connect(delete)
ui4.btn_exit.clicked.connect(his_close)


################################  Diffcal Buttons #################################


ui.dbtn_exit.clicked.connect(open_menu)
ui.dbtn_diff.clicked.connect(diff_clicked)
ui.dbtn_diff.clicked.connect(insert_ddata)

ui.dbtn_sin.clicked.connect(sin_clicked)
ui.dbtn_int.clicked.connect(int_clicked)
ui.dbtn_cos.clicked.connect(cos_clicked)
ui.dbtn_tan.clicked.connect(try123)
ui.dbtn_itan.clicked.connect(atan_clicked)
ui.dbtn_icos.clicked.connect(acos_clicked)
ui.dbtn_isin.clicked.connect(asin_clicked)
ui.dbtn_e.clicked.connect(e_clicked)
ui.dbtn_log.clicked.connect(log_clicked)
ui.dbtn_pow.clicked.connect(x_y_clicked)
ui.dbtn_lc.clicked.connect(leftbrac_clicked)
ui.dbtn_rc.clicked.connect(rightbrac_clicked)
ui.dbtn_1.clicked.connect(num1_clicked)
ui.dbtn_2.clicked.connect(num2_clicked)
ui.dbtn_3.clicked.connect(num3_clicked)
ui.dbtn_4.clicked.connect(num4_clicked)
ui.dbtn_5.clicked.connect(num5_clicked)
ui.dbtn_6.clicked.connect(num6_clicked)
ui.dbtn_7.clicked.connect(num7_clicked)
ui.dbtn_8.clicked.connect(num8_clicked)
ui.dbtn_9.clicked.connect(num9_clicked)
ui.dbtn_0.clicked.connect(num0_clicked)
ui.dbtn_C.clicked.connect(clear_clicked)
ui.dbtn_back.clicked.connect(back_clicked)
ui.dbtn_add.clicked.connect(plus_clicked)
ui.dbtn_subt.clicked.connect(minus_clicked)
ui.dbtn_mul.clicked.connect(multiply_clicked)
ui.dbtn_div.clicked.connect(divide_clicked)
ui.dbtn_x.clicked.connect(x_clicked)


################################ Solvecal Buttons #################################

ui3.pushButton.clicked.connect(sopen_menu)
ui3.pushButton_2.clicked.connect(solve_clicked)


################################ Limcal Buttons ###################################

ui2.limbtn_exit.clicked.connect(lopen_menu)
ui2.limbtn_lim.clicked.connect(limit_clicked)
ui2.limbtn_sin.clicked.connect(lsin_clicked)

ui2.limbtn_cos.clicked.connect(lcos_clicked)
ui2.limbtn_itan.clicked.connect(latan_clicked)
ui2.limbtn_icos.clicked.connect(lacos_clicked)
ui2.limbtn_isin.clicked.connect(lasin_clicked)
ui2.limbtn_e.clicked.connect(le_clicked)
ui2.limbtn_log.clicked.connect(llog_clicked)
ui2.limbtn_pow.clicked.connect(lx_y_clicked)
ui2.limbtn_lc.clicked.connect(lleftbrac_clicked)
ui2.limbtn_rc.clicked.connect(lrightbrac_clicked)
ui2.limbtn_1.clicked.connect(lnum1_clicked)
ui2.limbtn_2.clicked.connect(lnum2_clicked)
ui2.limbtn_3.clicked.connect(lnum3_clicked)
ui2.limbtn_4.clicked.connect(lnum4_clicked)
ui2.limbtn_5.clicked.connect(lnum5_clicked)
ui2.limbtn_6.clicked.connect(lnum6_clicked)
ui2.limbtn_7.clicked.connect(lnum7_clicked)
ui2.limbtn_8.clicked.connect(lnum8_clicked)
ui2.limbtn_9.clicked.connect(lnum9_clicked)
ui2.limbtn_0.clicked.connect(lnum0_clicked)
ui2.limbtn_C.clicked.connect(lclear_clicked)
ui2.limbtn_back.clicked.connect(lback_clicked)
ui2.limbtn_add.clicked.connect(lplus_clicked)
ui2.limbtn_subt.clicked.connect(lminus_clicked)
ui2.limbtn_mul.clicked.connect(lmultiply_clicked)
ui2.limbtn_div.clicked.connect(ldivide_clicked)
ui2.limbtn_x.clicked.connect(lx_clicked)





################################# Do not replace ##################################

sys.exit(app.exec_())