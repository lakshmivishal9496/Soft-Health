import pytest
import sys
import os
from PyQt5.QtCore import Qt
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from src.exercises import Ui_Form




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


def test_next_button(ui_form):
    '''Test Next button'''

    font = ui_form.next_btn.font()
    assert font.family() == "Sura"  # check that the button has the correct font family
   
    assert ui_form.next_btn.objectName() == "next_btn"  # check that the button has the correct object name
    QTest.mouseClick(ui_form.next_btn, Qt.LeftButton)  # simulate a left mouse click on the button


def test_back_button(ui_form):
    '''Test Back button'''
    font = ui_form.next_btn.font()
    assert font.family() == "Sura" 
    assert ui_form.back_btn.objectName() == "back_btn"  # check that the button has the correct object name
    QTest.mouseClick(ui_form.back_btn, Qt.LeftButton)  # simulate a left mouse click on the button

def test_logoutButton(ui_form):
    '''Test Logout'''
    assert ui_form.logout.text() == "Logout"
    QTest.mouseClick(ui_form.logout, Qt.LeftButton)

def test_mainButton( ui_form):
    '''Test Main Button'''
    assert ui_form.main_btn.text() == "Main Menu"
    QTest.mouseClick(ui_form.main_btn, Qt.LeftButton)
    # Add any additional assertions or behavior that you expect from the main button






