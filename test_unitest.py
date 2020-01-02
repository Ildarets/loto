import unittest
from card_2 import Kartochki
from class_Gamer import Gamer

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


class Test_Gamer(unittest.TestCase):
    def setUp(self):
        self.gamer = Gamer(2,2)

    def tearDown(self):
        del self.gamer

    def test_init(self):
        self.assertEqual(self.gamer.list_card_gamer, [])

    def test_creat_card(self):
        self.assertEqual(len(self.gamer.list_card_gamer), 0)