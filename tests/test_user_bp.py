import unittest
from app import create_app 


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Налаштування клієнта тестування перед кожним тестом."""
        self.app = create_app()     # 👈 створюємо додаток
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_greetings_page(self):
        """Тест маршруту /hi/<name>."""
        response = self.client.get("/users/hi/John?age=30")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"John", response.data)
        self.assertIn(b"30", response.data)

    def test_admin_page(self):
        """Тест маршруту /admin, який перенаправляє."""
        response = self.client.get("/admin", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Administrator", response.data)
        self.assertIn(b"45", response.data)

    def test_product_page(self):
        """Тест маршруту /products."""
        response = self.client.get("/products/salt")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"salt", response.data)

if __name__ == "__main__":
    unittest.main()