import sqlite3
import unittest
from src.main import RegApp
class TestRegApp(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database and set up the login table
        self.db = sqlite3.connect(':memory:')
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS login (
                username TEXT,
                password TEXT,
                email TEXT
            )
        ''')
        self.db.commit()

    def test_reg_success(self):
        # Create a new RegApp instance and register a new user
        reg = RegApp()
        reg.tb3.setText('testuser')
        reg.tb4.setText('testpassword')
        reg.tb5.setText('testemail')
        reg.reg()

        # Check that the new user is in the database
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM login WHERE username='testuser'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'testpassword')
        self.assertEqual(result[2], 'testemail')

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()
