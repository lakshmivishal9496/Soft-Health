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
    ui_form = Ui_Form()
    ui_form.setupUi(ui_form)
    yield ui_form
    app.quit()
    
    
def test_loginButton(ui_form):
    assert ui_form.b1.text() == "Login"
    QTest.mouseClick(ui_form.b1, Qt.LeftButton)
    
def test_signUpButton(ui_form):
    assert ui_form.b2.text() == "Sign up"
    QTest.mouseClick(ui_form.b2, Qt.LeftButton)
    
def test_guestButton(ui_form):
    assert ui_form.b5.text() == "Continue as a Guest"
    QTest.mouseClick(ui_form.b5, Qt.LeftButton)


def test_textBox(ui_form):
    ui_form.tb1.setText("Username")
    ui_form.lineEdit.setText("Password")
    assert ui_form.tb1.text() == "Username"
    assert ui_form.lineEdit.text() == "Password"
