# test_auth.py
import unittest
from auth import check_login

class TestLogin(unittest.TestCase):
    def test_valid_credentials(self):
        """Перевіряє, що правильні логін і пароль повертають True."""
        self.assertTrue(check_login("admin", "1234"))

    def test_invalid_credentials(self):
        """Перевіряє, що неправильний пароль повертає False."""
        self.assertFalse(check_login("admin", "wrongpass"))

if __name__ == "__main__":
    unittest.main()
