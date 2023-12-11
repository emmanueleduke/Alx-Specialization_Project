import unittest
from flask import Flask
import sys
sys.path.append("/home/emmyduke/Alx-Specialization_Project")

from app import app

class YourAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        response = self.app.get('/')
        content = response.get_data(as_text=True)  # Convert response data to a string

        # Assert that the expected strings are present in the HTML content
        self.assertIn('<h1>System Monitoring</h1>', content)
        self.assertIn('<div id="cpu-gauge"></div>', content)
        self.assertIn('<div id="mem-gauge"></div>', content)
        self.assertIn('CPU Utilization', content)
        self.assertIn('Memory Utilization', content)

if __name__ == '__main__':
    unittest.main()

