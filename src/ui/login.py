from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import sqlite3
from ui.guest import GuestApp


class LoginApp(QDialog):
    # Deals with login screen for the app

    # load the UI file using an relative path
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi(r"static\login.ui", self)
        self.guest_page = GuestApp()
        self.b5.clicked.connect(self.guest_page.guest_login)

    def login(self):
        print("Login")
        un = self.tb1.text()
        pw = self.tb2.text()
        # print(un)
        # print(pw)
        # connect to the database anD
        # check if the username and password are valid
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM login \
                    WHERE username = ? AND password = ?', (un, pw))
        user = cursor.fetchone()
        # print(user)
        # check if username and password are provided
        if not un or not pw:
            QMessageBox.warning(self, "Login Error",
                                "Username and password are required")
            return

        # display an error message if the username and password are not valid
        if user is None:
            QMessageBox.warning(self, "Login Error",
                                "Invalid username or password")
            return

        # display a message box asking the user
        # if they want to take a personality assessment
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Welcome " + un + '\n'
                       "Do you want to take personality assessment")
        msgBox.setWindowTitle("User login")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # show the message box and wait for a button to be clicked
        buttonClicked = msgBox.exec()
        if buttonClicked == QMessageBox.Ok:
            print("OK button clicked")

        db.close()
        self.tb1.setText("")
        self.tb2.setText("")
