from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_audi_hatchback(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Audi'
            with patch('random.randrange') as r:
                    r.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Hatchback Audi')
                    self.assertIn(b'A3', response.data)
    
    def test_audi_Saloon(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Audi'
            with patch('random.randrange') as r:
                    r.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Saloon Audi')
                    self.assertIn(b'A6', response.data)
    
    def test_audi_suv(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Audi'
            with patch('random.randrange') as r:
                    r.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'SUV Audi')
                    self.assertIn(b'Q7', response.data)
    
    def test_bmw_hatchback(self):
        with patch('requests.get') as i:
            i.return_value.text = 'BMW'
            with patch('random.randrange') as r:
                    r.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Hatchback BMW')
                    self.assertIn(b'1-Series', response.data)
    
    def test_bmw_saloon(self)):
        with patch('requests.get') as i:
            i.return_value.text = 'BMW'
            with patch('random.randrange') as r:
                    r.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Saloon BMW')
                    self.assertIn(b'5-Series', response.data)
    
    def test_bmw_suv(self):
        with patch('requests.get') as i:
            i.return_value.text = 'BMW'
            with patch('random.randrange') as r:
                    r.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'SUV BMW')
                    self.assertIn(b'X5', response.data)

    def test_mercedes_hatchback(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Mercedes'
            with patch('random.randrange') as r:
                    r.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Hatchback Mercedes')
                    self.assertIn(b'A-Class', response.data)
    
    def test_mercedes_saloon(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Mercedes'
            with patch('random.randrange') as r:
                    r.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Saloon Mercedes')
                    self.assertIn(b'E-Class', response.data)
    
    def test_mercedes_suv(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Mercedes'
            with patch('random.randrange') as r:
                    r.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'SUV Mercedes')
                    self.assertIn(b'GLE', response.data)