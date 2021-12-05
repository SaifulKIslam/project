from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_hatchback(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('shape'))
            self.assertIn(b'Hatchback', response.data)

    def test_saloon(self):
        with patch('random.randrange') as r:
            r.return_value = 1
            response = self.client.get(url_for('shape'))
            self.assertIn(b'Saloon', response.data)

    def test_suv(self):
        with patch('random.randrange') as r:
            r.return_value = 2
            response = self.client.get(url_for('shape'))
            self.assertIn(b'SUV', response.data)