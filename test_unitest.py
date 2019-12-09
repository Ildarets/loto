import unittest
from card_2 import Kartochki

class TestKartochki(unittest.TestCase):
    def setUp(self):
        self.card = Kartochki()

    def tearDown(self):
        del self.card

    def test_init(self):
        self.assertEqual(self.card.list_card,[])
        self.assertEqual(len(self.card.index_str[0]), 5)
        self.assertEqual(len(self.card.index_str[1]), 5)
        self.assertEqual(len(self.card.index_str[2]), 5)
        self.assertEqual(len(self.card.index_str), 3)

    def test_card_list(self):
        self.card.card_list()
        self.assertEqual(len(self.card.list_card), 15)

    def test_card_str(self):
        self.card.card_list()
        self.card.card_str()
        self.assertEqual(len(self.card.list_f[0]), 9)
        self.assertEqual(len(self.card.list_f[1]), 9)
        self.assertEqual(len(self.card.list_f[2]), 9)



