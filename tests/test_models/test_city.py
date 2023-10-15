#!/usr/bin/python3

from tests.test_model import test_basemodel
from models.city import City

class test_city(test_basemodel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_name(self):
        x = self.value()
        self.assertEqual(type(x.name), str)

    def test_state_id(self):
        x = self.value()
        self.assertEqual(type(x.state_id), str)
