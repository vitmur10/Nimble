import unittest
from app import app


class FullTextSearchTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_search_with_no_text(self):
        # Тестуємо пошук без тексту, має повернути порожній список контактів
        response = self.app.get('/search')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)

    def test_search_with_valid_text(self):
        # Тестуємо пошук з дійсним текстом, має повернути збіги контактів
        response = self.app.get('/search?text=John')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        # Перевіряємо, чи кожен контакт містить хоча б одну зі співпадаючих слів (прізвище, ім'я, електронна пошта)
        for contact in data:
            self.assertTrue(
                'John' in contact['first_name'] or 'John' in contact['last_name'] or 'John' in contact['email'])

    def test_search_with_invalid_text(self):
        # Тестуємо пошук з недійсним текстом, має повернути порожній список контактів
        response = self.app.get('/search?text=InvalidText')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)

    def test_search_with_special_characters(self):
        # Тестуємо пошук з текстом, що містить спеціальні символи, має повернути збіги контактів
        response = self.app.get('/search?text=@gmail.com')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        # Перевіряємо, чи кожен контакт містить хоча б одну зі співпадаючих слів (прізвище, ім'я, електронна пошта)
        for contact in data:
            self.assertTrue(
                '@gmail.com' in contact['first_name'] or '@gmail.com' in contact['last_name'] or '@gmail.com' in
                contact['email'])


if __name__ == '__main__':
    unittest.main()
