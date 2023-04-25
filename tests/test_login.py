import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from unittest.mock import patch
import sqlite3

from src.main import LoginApp

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.login = LoginApp()
    
    def tearDown(self):
        self.login.close()
    
    @patch('login.sqlite3.connect')
    def test_login_with_valid_credentials(self, mock_connect):
        # Set up mock database connection
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = ('username', 'password', 'email')
        
        # Set up GUI inputs
        self.login.tb1.setText('username')
        self.login.tb2.setText('password')
        
        # Simulate button click
        with patch.object(QMessageBox, 'exec', return_value=QMessageBox.Ok):
            self.login.b1.click()
        
        # Check that message box was displayed
        self.assertTrue(QMessageBox.exec.called)
        self.assertEqual(QMessageBox.exec.call_args[0][0], 'Welcome username\nDo you want to take personality assessment')
        
        # Check that database was queried with correct credentials
        mock_cursor.execute.assert_called_once_with('SELECT * FROM login WHERE username = ? AND password = ?', ('username', 'password'))
        
        # Check that text boxes were cleared
        self.assertEqual(self.login.tb1.text(), '')
        self.assertEqual(self.login.tb2.text(), '')
    
    def test_login_with_missing_credentials(self):
        # Set up GUI inputs
        self.login.tb1.setText('')
        self.login.tb2.setText('password')
        
        # Simulate button click
        with patch.object(QMessageBox, 'warning') as mock_warning:
            self.login.b1.click()
        
        # Check that warning message box was displayed
        self.assertTrue(mock_warning.called)
        self.assertEqual(mock_warning.call_args[0][0], self.login)
        self.assertEqual(mock_warning.call_args[0][1], 'Login Error')
        self.assertEqual(mock_warning.call_args[0][2], 'Username and password are required')
        
        # Check that database was not queried
        mock_connect.assert_not_called()
        
        # Check that text boxes were not cleared
        self.assertEqual(self.login.tb1.text(), '')
        self.assertEqual(self.login.tb2.text(), '')
