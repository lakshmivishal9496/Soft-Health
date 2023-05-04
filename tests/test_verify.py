import unittest
from unittest.mock import patch
from main import RegApp
from main import Verify


class TestVerify(unittest.TestCase):
    # testing if the password contains uppercase and numbers.
    @patch('builtins.input', side_effect = lambda x: ['password', 'Psw1'].pop(0))
    
    def test_verification(self, mock_input):
        verify = RegApp.verify_password('Psw1')
        self.assertTrue(verify)

    def test_compare(self):
        verify = Verify('Psw1')
        self.assertTrue(verify.compare('Psw1'))

    def test_compare_false(self):
        verify = Verify('Psw1')
        self.assertFalse(verify.compare('psw2'))


if __name__ == '__main__':
    app = RegApp()
    app.get_password()
    verified = app.verify_password(app.password)
    if verified:
        print("Password verified.")
    else:
        print("Password not verified.")
    
    unittest.main()