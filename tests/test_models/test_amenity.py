#!/usr/bin/python3

from test.test_model.test_base_model import test_basemodel
from models.amenity import Amenity

class test_Amenity(test_basemodel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name "Amenity"
        self.value = Amenity

    def test_Aname(self):
        x = self.value()
        self.assertEqual(type(x.name), str)
