import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)

from PyQt5.QtCore import Qt
import pytest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from login import Ui_Form



def Ui_test():
    app = QApplication(sys.argv)
    Ui_test = Ui_Form()
    Ui_test.setupUi(Ui_test)
    yield Ui_test
    app.quit()
    
    
def test_login_button(Ui_test):
    assert Ui_test.b1.text() == "Login"
    QTest.mouseClick(Ui_test.b1, Qt.LeftButton)
    
def test_signUp_button(Ui_test):
    assert Ui_test.b2.text() == "Sign up"
    QTest.mouseClick(Ui_test.b2, Qt.LeftButton)
    
def test_guest_button(Ui_test):
    assert Ui_test.b5.text() == "Continue as a Guest"
    QTest.mouseClick(Ui_test.b5, Qt.LeftButton)

 
def text_box_test(Ui_test):
    Ui_test.tb1.setText("Username")
    Ui_test.lineEdit.setText("Password")
    assert Ui_test.tb1.text() == "Username"
    assert Ui_test.lineEdit.text() == "Password"

    
    
