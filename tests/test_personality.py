import unittest
from PyQt5.QtWidgets import QApplication, QPushButton, QRadioButton, QLineEdit

from personality import Ui_PersonalityTest


class TestUiPersonalityTest(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.ui = Ui_PersonalityTest()
        self.PersonalityTest = QWidget()

    def tearDown(self):
        self.app.quit()

    def test_setupUi(self):
        self.ui.setupUi(self.PersonalityTest)

        self.assertEqual(self.PersonalityTest.objectName(), "PersonalityTest")
        self.assertEqual(self.PersonalityTest.size().width(), 1024)
        self.assertEqual(self.PersonalityTest.size().height(), 768)

        self.assertIsInstance(self.ui.logout, QPushButton)
        self.assertEqual(self.ui.logout.text(), "Logout")
        self.assertEqual(self.ui.logout.geometry().x(), 800)
        self.assertEqual(self.ui.logout.geometry().y(), 50)
        self.assertEqual(self.ui.logout.geometry().width(), 175)
        self.assertEqual(self.ui.logout.geometry().height(), 40)

        # Continue testing the remaining UI elements...

    def test_retranslateUi(self):
        self.ui.retranslateUi(self.PersonalityTest)

        self.assertEqual(self.PersonalityTest.windowTitle(), "Form")
        self.assertEqual(self.ui.logout.text(), "Logout")
        self.assertEqual(self.ui.next_btn.text(), "Next")
        self.assertEqual(self.ui.back_btn.text(), "Back")
        self.assertEqual(self.ui.main_btn.text(), "Main Menu")
        self.assertEqual(self.ui.Question_No.text(), "Question 1")
        self.assertEqual(self.ui.Question_area.text(), "You feel more energetic when:")
        self.assertEqual(self.ui.radioButton1.text(), "Socializing with others")
        self.assertEqual(self.ui.radioButton2.text(), "Spending time alone")

if __name__ == "__main__":
    unittest.main()
