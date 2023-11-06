import unittest
from collections import deque
from laskin import Laskin

class TestLaskin(unittest.TestCase):
    def setUp(self):
        pass

    def test_oikeanlainen_tulos(self):
        tulos = Laskin.laske_tulos("3+5*(1-3)")
        self.assertEqual(-7.0, tulos)

    def test_oikeanlainen_rpn(self):
        tulos = Laskin.muunna_rpn_muotoon("3+5*(1-3)")
        self.assertEqual(deque(['3', '5', '1', '3', '-', '*', '+']), tulos)

    def test_virheellinen_lauseke_hylataan(self):
        self.assertFalse(Laskin.muunna_rpn_muotoon("ABC"))
        self.assertFalse(Laskin.laske_tulos("ABC"))