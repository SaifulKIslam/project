from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_Audi(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('make'))
            self.assertIn(b'Audi', response.data)
    
    def test_BMW(self):
        with patch('random.randrange') as r:
            r.return_value = 1
            response = self.client.get(url_for('make'))
            self.assertIn(b'BMW', response.data)
    
    def test_Mercedes(self):
        with patch('random.randrange') as r:
            r.return_value = 2
            response = self.client.get(url_for('make'))
            self.assertIn(b'Mercedes', response.data)