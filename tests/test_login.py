import unittest
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from main import LoginApp
class TestLoginApp(unittest.TestCase):
    
    def setUp(self):
        self.app = LoginApp()
        self.app.tb1.setText("testuser")
        self.app.tb2.setText("testpass")

    def test_login_success(self):
        # create a test user in the database
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO login (username, password) VALUES ('testuser', 'testpass')")
        db.commit()

        # simulate a login attempt
        self.app.login()

        # check that the welcome message is displayed
        self.assertEqual(self.app.msgBox.text(), "Welcome testuser\nDo you want to take personality assessment")

        # click the OK button
        self.app.msgBox.buttonClicked.connect(lambda: self.app.msgBox.done(QMessageBox.Ok))
        self.app.msgBox.show()
        
        # check that the OK button was clicked
        self.assertEqual(self.app.buttonClicked, QMessageBox.Ok)

        # delete the test user from the database
        cursor.execute("DELETE FROM login WHERE username = 'testuser'")
        db.commit()
        db.close()

    def test_login_failure(self):
        # simulate a login attempt with an invalid username and password
        self.app.tb1.setText("invaliduser")
        self.app.tb2.setText("invalidpass")
        self.app.login()

        # check that an error message is displayed
        self.assertEqual(self.app.msgBox.text(), "Invalid username or password")

    def test_login_missing_fields(self):
        # simulate a login attempt with missing username and password fields
        self.app.tb1.setText("")
        self.app.tb2.setText("")
        self.app.login()

        # check that an error message is displayed
        self.assertEqual(self.app.msgBox.text(), "Username and password are required")

    def tearDown(self):
        self.app.close()

if __name__ == '__main__':
    unittest.main()
