import sys
import os
import unittest
from PyQt5.QtWidgets import QApplication, QWidget
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
from registration import Ui_Form

class TestUiForm(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
    
    def tearDown(self):
        self.form.close()
    
    def test_tb3_placeholder_text(self):
        expected_text = "Enter username here........."
        actual_text = self.ui.tb3.placeholderText()
        self.assertEqual(actual_text, expected_text)

    def test_tb4_placeholder_text(self):
        expected_text = "Enter password  here........."
        actual_text = self.ui.tb4.placeholderText()
        self.assertEqual(actual_text, expected_text)

    def test_b3_text(self):
        expected_text = "Submit"
        actual_text = self.ui.b3.text()
        self.assertEqual(actual_text, expected_text)


if __name__ == "__main__":
    unittest.main()
