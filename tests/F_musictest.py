import sys
import os
import pytest
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
from src.music import Ui_Form


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


class TestMusicUI:
    '''Test the UI of the music page'''

    def test_ui_elements_exist(self, ui_form):
        '''Test that all the UI elements exist'''

        assert ui_form.next_btn is not None
        assert ui_form.back_btn is not None
        assert ui_form.main_btn is not None
        assert ui_form.mute is not None
        assert ui_form.play_btn is not None
        assert ui_form.pause_btn is not None
        assert ui_form.minus is not None
        assert ui_form.plus is not None
        assert ui_form.main_label is not None
        assert ui_form.volume_label is not None
        assert ui_form.logout is not None
    
    def test_logoutButton(self, ui_form):
        assert ui_form.logout.text() == "Logout"
        QTest.mouseClick(ui_form.logout, Qt.LeftButton)

    def test_nextButton(self, ui_form):
        assert ui_form.next_btn.text() == "Next"
        QTest.mouseClick(ui_form.next_btn, Qt.LeftButton)

    def test_backButton(self, ui_form):
        assert ui_form.back_btn.text() == "Back"
        QTest.mouseClick(ui_form.back_btn, Qt.LeftButton)

    def test_mainButton(self, ui_form):
        assert ui_form.main_btn.text() == "Main Menu"
        QTest.mouseClick(ui_form.main_btn, Qt.LeftButton)
    
    def test_playButton(self, ui_form):
        assert ui_form.play_btn.text() == "play"
        QTest.mouseClick(ui_form.play_btn, Qt.LeftButton)
  
    def test_pauseButton(self, ui_form):
        assert ui_form.pause_btn.text() == "pause"
        QTest.mouseClick(ui_form.pause_btn, Qt.LeftButton)
    
    def test_volumeLabel(self, ui_form):
        assert ui_form.volume_label.text() == "Volume"
        QTest.mouseClick(ui_form.volume_label, Qt.LeftButton)
    
    def test_muteButton(self, ui_form):
        assert ui_form.mute.text() == "mute"
        QTest.mouseClick(ui_form.mute, Qt.LeftButton)
    
    def test_minusButton(self, ui_form):
        assert ui_form.minus.text() == "-"
        QTest.mouseClick(ui_form.minus, Qt.LeftButton)
    
    def test_plusButton(self, ui_form):
        assert ui_form.plus.text() == "+"
        QTest.mouseClick(ui_form.plus, Qt.LeftButton)
    
    def test_main_label(self, ui_form):
        assert ui_form.main_label.text() == "Relaxing Music"
        QTest.mouseClick(ui_form.main_label, Qt.LeftButton)

