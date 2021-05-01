from unittest import TestCase
from src import Amigo


class Test(TestCase):
    def test_aggregate(self):
        self.assertEqual(Amigo.aggregate("email1", "email2"), {"codi": 200})

    def test_search_exist(self):
        self.assertEqual(Amigo.search("email1", "email2"), {"codi": 200})

    def test_delete(self):
        self.assertEqual(Amigo.delete("email1", "email2"), {"codi": 200})

    def test_search_no_exist(self):
        self.assertEqual(Amigo.search("email1", "email2"), {"codi": 500})

    def test_get_friends(self):
        self.assertEqual(Amigo.get_friends("Bakanalmi"), [{'numfriends': 4},
                                                         {'accountname': 'example', 'coins': 0, 'faction': 'red', 'points': 0},
                                                         {'accountname': 'corico', 'coins': 0, 'faction': 'yellow', 'points': 0},
                                                         {'accountname': 'back-end', 'coins': 0, 'faction': 'red', 'points': 0},
                                                         {'accountname': 'utest1', 'coins': 0, 'faction': 'red', 'points': 0}])