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
        un = self.tb1.text()
        pw = self.tb2.text()
        # tb1 is the name of LineEdit component from desinger UI login.ui
        # tb2 is the name of LineEdit component from desinger UI login.ui
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Welcome " + self.tb1.text() + '\n'
                       "Do you want to take personality assessment")
        msgBox.setWindowTitle("User login")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
# show the message box and wait for a button to be clicked
        buttonClicked = msgBox.exec()
        un = self.tb1.text()
        pw = self.tb2.text()

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
        msgBox1.setText("User account has been created")
        msgBox1.setStandardButtons(QMessageBox.Ok)
        buttonClicked1 = msgBox1.exec()
        if buttonClicked1 == QMessageBox.Ok:
            print("OK button clicked")
        self.un = self.tb3.text()
        self.pw = self.tb4.text()
        self.em = self.tb5.text()
        print(self.un)
        print(self.pw)
        print(self.em)
        db = sqlite3.connect('softhealth1.db')
        print(db)
        cursor1 = db.cursor()
        print(cursor1)
        cursor1.execute('''
                       CREATE TABLE IF NOT EXISTS Login1 (
                           username VARCHAR(255) NOT NULL,
                           password VARCHAR(255),
                           email VARCHAR(255) NOT NULL,
                       ''')
        cursor1.execute('''
                       INSERT INTO Login1 (username, password, email)
                       VALUES (self.un, self.pw, self.em)
                       ''')
        user = cursor1.execute('''SELECT  * FROM  Login1 ''')
        print(user.fetchall())
        db.commit()
        db.close()
       
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
# inside root director have both the files:
# login. ui and register.ui
# paste all the images used in the qt designer into the Root folder
# What does this command does? pyuic5 register.ui -o reg.py
# convert the register.ui in pyqt designer into code and create reg.py
# What does this command does?  pyuic5 login.ui -o res.py
# convert the login.ui in pyqt designer into code and create res.py
