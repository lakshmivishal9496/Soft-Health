import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi, loadUiType
import sqlite3
import re

class LoginApp(QDialog):
    # Deals with login screen for the app

    # load the UI file using an relative path
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi(r"static\login.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_register)
        self.b5.clicked.connect(self.guest_login)

    def login(self):
        print("Login")
        un = self.tb1.text()
        pw = self.tb2.text()
        print(un)
        print(pw)        
        # connect to the database and check if the username and password are valid
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM login WHERE username = ? AND password = ?', (un, pw))
        user = cursor.fetchone()
        print(user)
        # check if username and password are provided
        if not un or not pw:
            QMessageBox.warning(self, "Login Error", "Username and password are required")
            return

        # display an error message if the username and password are not valid
        if user is None:
            QMessageBox.warning(self, "Login Error", "Invalid username or password")
            return
        
        # display a message box asking the user if they want to take a personality assessment
        widget.setCurrentIndex(4)
        # msgBox = QMessageBox()
        # msgBox.setIcon(QMessageBox.Information)
        # msgBox.setText("Welcome " + un + '\n'
        #                "Do you want to take personality assessment")
        # msgBox.setWindowTitle("User login")
        # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        # # show the message box and wait for a button to be clicked
        # buttonClicked = msgBox.exec()
        # if buttonClicked == QMessageBox.Ok:
        #     print("OK button clicked")
        
        db.close()
        self.tb1.setText("")
        self.tb2.setText("")

    def show_register(self):
        widget.setCurrentIndex(1)
    def guest_login(self):
        widget.setCurrentIndex(3)
        msgBox = QMessageBox()
        # msgBox.setIcon(QMessageBox.Information)
        # msgBox.setText("Welcome " + 'guest user' + '\n'
        #                "Do you want to take personality assessment")
        # msgBox.setWindowTitle("Guest User login")
        # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        # # show the message box and wait for a button to be clicked
        # buttonClicked = msgBox.exec()
        # if buttonClicked == QMessageBox.Ok:
        #     print("OK button clicked")


class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\register.ui", self)
        
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)

    def verify_password(self, password):
        if len(password) < 8 and re.search('[0-9]', password) is None and re.search('[A-Z]', password) is None:
            return "Password must contain: \n " + "*minimum 8 characters,\n " +  "*a number \n " + "*a uppercase letter"
        else:
            return None

    def reg(self):
        un = self.tb3.text()
        pw = self.tb4.text()
        em = self.tb5.text()
        repw = self.tb6.text()
        # print(un)
        # print(pw)
        # print(em)
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS login (
                           username TEXT,
                           password TEXT,
                           email TEXT)
                       ''')
        
        error_message = self.verify_password(pw)
        if not un or not pw or not em:
            QMessageBox.warning(self, "Registration Error", "Please fill in all the fields")
        else:
            if error_message:
                QMessageBox.warning(self, "Registration Error", error_message)
            elif pw != repw:
                QMessageBox.warning(self, "Registration Error", "Passwords do not match.")
            else:
                cursor.execute('''
                    INSERT INTO login (username, password, email)
                    VALUES (?,?,?)
                    ''', (un, pw, em))
                db.commit()
                db.close()
                QMessageBox.information(self, "Login Output", "User registered successfully login now>>")
            QApplication.processEvents()
            self.tb3.setText("")
            self.tb4.setText("")
            self.tb5.setText("")
            self.tb6.setText("")

    def show_login(self):
        widget.setCurrentIndex(0)
        
class HomeApp(QDialog):
    def __init__(self):
        super(HomeApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\home.ui", self)

class mainMenuApp(QDialog):
    def __init__(self):
        super(mainMenuApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\mainmenu.ui", self)
        self.b9.clicked.connect(self.menu)
    
    def menu(self):
        widget.setCurrentIndex(2)

class GuestApp(QDialog):
    def __init__(self):
        super(GuestApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\guest.ui", self)

class Verify:
    def __init__(self, password):
        self.password = password

    def compare(self, other_password):
        return self.password == other_password



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
# Connects both login and register widgets together
loginform = LoginApp()
registrationform = RegApp()
Homeform = HomeApp()
guestform = GuestApp()
mainMenuform = mainMenuApp()
widget.addWidget(loginform)
widget.addWidget(registrationform)
widget.addWidget(Homeform)
widget.addWidget(guestform)
widget.addWidget(mainMenuform)
widget.setCurrentIndex(0)
widget.setFixedWidth(800)
widget.setFixedHeight(600)

widget.show()
sys.exit(app.exec_())
