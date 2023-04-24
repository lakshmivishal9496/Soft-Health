import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi, loadUiType
import mysql.connector as connector
import sqlite3
#To install mysql-connector-python, open a terminal and type the following command:
# pip install mysql-connector-python

import os

class LoginApp(QDialog):
    # Deals with login screen for the app

# load the UI file using an relative path
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi(r"login.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_register)

    def login(self):
        # tb1 is the name of LineEdit component from desinger UI login.ui
        # tb2 is the name of LineEdit component from desinger UI login.ui
        print("Login")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Login Successfully")
        msgBox.setWindowTitle("User login")
        msgBox.setStandardButtons(QMessageBox.Ok)
        
# show the message box and wait for a button to be clicked
        buttonClicked = msgBox.exec()
        if buttonClicked == QMessageBox.Ok:
            print("OK button clicked")
        un = self.tb1.text()
        pw = self.tb2.text()
    
        # db =  connector.connect(host="DESKTOP-0LS9HQI\MSSQLSERVER01", user="root", password="", db ="SoftHealth")
        # cursor = db.cursor()
        # cursor.execute("select * from Login where username = '" +  un  +"'  and password = '" + pw +"'")
        # excute the sql query
        result = cursor.fetchone()
        self.tb1.setText("")
        self.tb2.setText("")
        if result:
            QMessageBox.information(self, "Login Output", "Congrats login successful")
            print("Connect")
            QApplication.processEvents()
        else:
            # If username and password are not in database, then
            QMessageBox.information(self, "Login Output", "Invalid User.. Register for New Account")
            print("not Connect")
            QApplication.processEvents()
            

    def show_register(self):
        widget.setCurrentIndex(1)


class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"register.ui", self)
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)

    def reg(self):
        msgBox1 = QMessageBox()
        msgBox1.setIcon(QMessageBox.Information)
        msgBox1.setWindowTitle("User Account Creation")
        msgBox1.setText("Registration Information")
        msgBox1.setStandardButtons(QMessageBox.Ok)
        buttonClicked1 = msgBox1.exec()
        if buttonClicked1 == QMessageBox.Ok:
            print("OK button clicked")
        un = self.tb3.text()
        pw = self.tb4.text()
        em = self.tb5.text()
        print(un)
        print(pw)
        print(em)
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS login (
                           'username' TEXT,
                           'password' TEXT,
                           'email' TEXT,
                       ''')
        cursor.execute('''
                       INSERT INTO login (username, password, email)
                       VALUES ( '" +  un  + "'  , '" + pw +"' , '" + em+ "' ")
                       ''')
        
        db.commit()
        db.close()
        # cursor.execute("select * from Login where username = '" +  un  +"'  and password = '" + pw + "'")
        # db = connector.connect(host="DESKTOP-0LS9HQI\MSSQLSERVER01", user="root", password="", db ="SoftHealth")
        # cursor = db.cursor()
        # cursor.execute("select * from Login where username = '" +  un  +"'  and password = '" + pw +"' ")
        # excute the sql query
        result = cursor.fetchone()
        if result:
            QMessageBox.information(self, "Login Output", "User already registered")
            print("Connect")
            QApplication.processEvents()
        else:
            # If username and password are not in database, then
            cursor.execute("insert into Login values( '" +  un  + "'  , '" + pw +"' , '" + em+ "' ")
            db.commit()
            QMessageBox.information(self, "Login Output", "User registered successfully login now>>")
            QApplication.processEvents()
            self.tb3.setText("")
            self.tb4.setText("")
            self.tb5.setText("")
            
    def show_login(self):
        widget.setCurrentIndex(0)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
# Connects both login and register widgets together
loginform = LoginApp()
registrationform = RegApp()
widget.addWidget(loginform)
widget.addWidget(registrationform)
widget.setCurrentIndex(0)
widget.setFixedWidth(400)
widget.setFixedHeight(500)

widget.show()
sys.exit(app.exec_())








# neccessary packages to be installed after activating venv
# pip install PyQt5
# pip install PyQt5-tools
# pip install PyQt5Designer
#activate venv
# inside venv/ Scripts paste the following
# login. ui and register.ui
# paste all the images used in the qt designer into the Scripts folder
# What does this command does? pyuic5 register.ui -o reg.py
# convert the register.ui in pyqt designer into code and create reg.py
# What does this command does?  pyuic5 login.ui -o res.py
# convert the login.ui in pyqt designer into code and create res.py
# after all these steps are done ,  there will be no errors such as 
# pyuic5 not recognized as internal and external commands
# login.ui file not found error


# pip install mysql-connector-python
# By default mysql wil be installed in venv/Lib 
# CTRL  X  mysql directory from the lib directory and paste it into the Script folder
# That will help to overcome the error 
#  File "c:\Users\laksh\pyqt\.venv\Scripts\main.py", line 5, in <module>
# import mysql.connector as connector
# ModuleNotFoundError: No module named 'mysql'