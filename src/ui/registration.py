from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sqlite3


class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\register.ui", self)
        self.b3.clicked.connect(self.reg)

    def reg(self):
        un = self.tb3.text()
        pw = self.tb4.text()
        em = self.tb5.text()
        # print(un)
        # print(pw)
        # print(em)
        # check if username, password and email are provided
        if len(un) == 0 or len(pw) == 0 or len(em) == 0:
            QMessageBox.warning(self, "Sign up error",
                                "Please fill all the fields.")
        else:
            db = sqlite3.connect('softhealth.db')
            cursor = db.cursor()
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS login (
                    username TEXT,
                    password TEXT,
                    email TEXT)
                    ''')
            cursor.execute('''
                    INSERT INTO login (username, password, email)
                    VALUES (?,?,?)
            ''', (un, pw, em))
            db.commit()
            db.close()
            QMessageBox.information(self, "Login Output",
                                    "User registered successfully login now>>")
            QApplication.processEvents()
            self.tb3.setText("")
            self.tb4.setText("")
            self.tb5.setText("")
