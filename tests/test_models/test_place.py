#!usr/bin/python3

from models.place import Place
form tests.test_models.test_base_model import test_basemodel

class test_place(test_basemodel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_user_id(self):
        x = self.value()
        self.assertEqual(type(x.user_id), str)

    def test_city_id(self):
        x = self.value()
        self.assertEqual(type(x.city_id), str)

    def test_name(self):
        x = self.value()
        self.assertEqual(type(x.name), str)

    def test_number_rooms(self):
        x = self.value()
        self.assertEqual(type(x.number_rooms), int)

    def test_description(self):
        x = self.value()
        self.assertEqual(type(x.description), str)

    def test_number_bathrooms(self):
        x = self.value()
        self.assertEqual(type(x.number_bathrooms), int)

    def test_max_guest(self):
        x = self.value()
        self.assertEqual(type(x.max_guest), int)

    def test_price_by_night(self):
        x = self.value()
        self.assertEqual(type(x.price_by_night), int)

    def test_latitude(self):
        x = self.value()
        self.assertEqual(type(x.latitude), float)

    def test_longitude(self):
        x = self.value()
        self.assertEqual(type(x.longitude), float)

    def test_aminity_ids(self):
        x = self.value()
        self.assertEqual(type(x.amenity_ids), list)


