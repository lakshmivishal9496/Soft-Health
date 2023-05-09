import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
import pytest
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from login import Ui_Form

@pytest.fixture
def ui_form():
    '''Test the form'''
    app = QApplication(sys.argv)
    ui = QtWidgets.QWidget()
    form = Ui_Form()
    form.setupUi(ui)
    ui.show()
    yield form
    app.quit()

class TestLoginUI:
    '''Test Login UI class'''
    def test_loginButton(self, ui_form):
        '''Test Login'''
        assert ui_form.b1.text() == "Login"
        QTest.mouseClick(ui_form.b1, Qt.LeftButton)
    
    def test_signUpButton(self, ui_form):
        assert ui_form.b2.text() == "Sign Up"
        QTest.mouseClick(ui_form.b2, Qt.LeftButton)
    
    def test_guestButton(self, ui_form):
        ''' Test that the guest button'''
        assert ui_form.b5.text() == "Continue as a Guest"
        QTest.mouseClick(ui_form.b5, Qt.LeftButton)

    def test_textBox(self, ui_form):
        '''Test that the text box is correctly displayed'''
        ui_form.tb1.setText("Username")
        ui_form.lineEdit.setText("Password")
        assert ui_form.tb1.text() == "Username"
        assert ui_form.lineEdit.text() == "Password"
