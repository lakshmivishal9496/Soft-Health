import unittest
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
from login import Ui_Form

class TestUiForm(unittest.TestCase):
    '''Test the UI form'''
    def setUp(self):
        '''Set up the UI form'''
        self.app = QApplication([])
        self.form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)

    def tearDown(self):
        '''Shut the application'''
        self.form.close()

    def test_window_title(self):
        '''Test window title'''
        self.assertEqual(self.form.windowTitle(), "Form")

    def test_button_text(self):
        '''Test button text'''
        self.assertEqual(self.ui.b1.text(), "Login")
        self.assertEqual(self.ui.b2.text(), "Sign Up")
        self.assertEqual(self.ui.b5.text(), "Continue as a Guest")

    def test_placeholder_text(self):
        '''Test placeholder'''
        self.assertEqual(self.ui.tb1.placeholderText(), "Enter username....")
        self.assertEqual(self.ui.lineEdit.placeholderText(), "Enter password.....")

    def test_widget_geometry(self):
        '''Test widget geometry'''
        self.assertEqual(self.form.width(), 363)
        self.assertEqual(self.form.height(), 487)


if __name__ == "__main__":
    unittest.main()


