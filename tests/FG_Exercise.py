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
from src.guestexercises import Ui_Form




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


def test_nextButton(ui_form):
    '''Test Next Button'''
    # Ensure button text is correct
    assert ui_form.next_btn.text() == "Next"
    QTest.mouseClick(ui_form.next_btn, Qt.LeftButton)

def test_back_button(ui_form):
    '''Test Back Button'''
    # Verify the button text
    assert ui_form.back_btn.text() == "Back"
    QTest.mouseClick(ui_form.back_btn, Qt.LeftButton)

def test_guestMenu_btn(ui_form):
    assert ui_form.guestMenu_btn is not None
    QTest.mouseClick(ui_form.guestMenu_btn, Qt.LeftButton)
  
def test_ui_form_formatting(ui_form):
    assert ui_form.Exercise is not None

