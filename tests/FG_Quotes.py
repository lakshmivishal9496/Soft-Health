import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
import pytest
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from src.guestquotes import Ui_Form

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

def test_QGroupBox(ui_form):
    '''Test that the QGroupBox is correctly displayed'''
    assert ui_form.groupBox.styleSheet() == "background-color:rgba(4, 255, 4, 50);"
    assert ui_form.groupBox.title() == ""
    assert ui_form.groupBox.objectName() == "groupBox"


def test_next_btn(ui_form):
    '''Test the properties of the next_btn button'''
    assert ui_form.next_btn.text() == "Next"
    assert ui_form.next_btn.font().family() == "Sura"
    assert ui_form.next_btn.objectName() == "next_btn" 
    QTest.mouseClick(ui_form.next_btn, Qt.LeftButton) 

def test_back_btn(ui_form):
    '''Test the back button'''
    assert ui_form.back_btn.text() == "Back"
    assert ui_form.back_btn.objectName() == "back_btn" 
    QTest.mouseClick(ui_form.back_btn, Qt.LeftButton) 

def test_quote_label(ui_form):
    assert ui_form.label_2 is not None
    assert ui_form.quote_area is not None
    assert ui_form.Question_No is not None

def test_guestMenu_btn(ui_form):
    '''Test that the guest menu button is correctly displayed'''
    assert ui_form.guestMenu_btn.text() == "Guest Menu"
