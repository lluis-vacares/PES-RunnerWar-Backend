from unittest import TestCase
from src import Amigo


class Test(TestCase):
    def test_aggregate(self):
        self.assertEqual(Amigo.aggregate("marc0almi@hotmail.com", "cairigaray999@gmail.com"), {"codi": 200})

    def test_search_exist(self):
        self.assertEqual(Amigo.search("marc0almi@hotmail.com", "cairigaray999@gmail.com"), {"codi": 200})

    def test_delete(self):
        self.assertEqual(Amigo.delete("marc0almi@hotmail.com", "cairigaray999@gmail.com"), {"codi": 200})

    def test_search_no_exist(self):
        self.assertEqual(Amigo.search("marc0almi@hotmail.com", "no_existeix@gmail.com"), {"codi": 500})

    def test_get_friends(self):
        self.assertEqual(Amigo.get_friends("marc0almi@hotmail.com"), [{"numfriends": 3},
                                                                      {"_id": "cairigaray999@gmail.com", "accountname": "corico", "coins": 0, "points": 0, "faction": "yellow"},
                                                                      {"_id": "pau.josep.ruiz@estudiantat.upc.edu", "accountname": "PauRu99", "coins": 0, "points": 0, "faction": "green"},
                                                                      {"_id": "pauketsjr@gmail.com", "accountname": "FullPau", "coins": 0, "points": 0, "faction": "yellow"}])