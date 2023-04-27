import unittest
from PyQt5.QtWidgets import QApplication, QWidget
from src.login import Ui_Form

class TestUiForm(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)

    def tearDown(self):
        self.form.close()

    def test_window_title(self):
        self.assertEqual(self.form.windowTitle(), "Form")

    def test_button_text(self):
        self.assertEqual(self.ui.b1.text(), "Login")
        self.assertEqual(self.ui.b2.text(), "Sign Up")
        self.assertEqual(self.ui.b5.text(), "Continue as a Guest")

    def test_placeholder_text(self):
        self.assertEqual(self.ui.tb1.placeholderText(), "Enter username....")
        self.assertEqual(self.ui.lineEdit.placeholderText(), "Enter password.....")

    def test_widget_geometry(self):
        self.assertEqual(self.form.width(), 363)
        self.assertEqual(self.form.height(), 487)

    # Add more test methods for other UI elements and functionality

if __name__ == '__main__':
    unittest.main()
