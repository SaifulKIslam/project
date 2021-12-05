from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as v:
            with patch("requests.post") as p:
                v.return_value.text = "Audi"
                p.return_value.text = "A3"

                response = self.client.get(url_for('index'))
                self.assertIn(b'Your car is a Audi A3. The shape of the car is a Hatchback', response.data)