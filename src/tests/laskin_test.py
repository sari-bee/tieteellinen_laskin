import unittest
from collections import deque
from laskin import Laskin

class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.muuttujat = {}

    def test_oikeanlainen_tulos(self):
        tulos = Laskin.laske_tulos("3+5*(1-3^2)", self.muuttujat)
        self.assertEqual(-37.0, tulos)

    def test_neliojuuri_lasketaan_oikein(self):
        tulos = Laskin.laske_tulos("s(64)/2", self.muuttujat)
        self.assertEqual(4, tulos)

    def test_oikeanlainen_rpn(self):
        tulos = Laskin.muunna_rpn_muotoon("3+5*(1-3)", self.muuttujat)
        self.assertEqual(deque(['3', '5', '1', '3', '-', '*', '+']), tulos)

    def test_virheellinen_lauseke_hylataan(self):
        self.assertFalse(Laskin.laske_tulos("ABC", self.muuttujat))

    def test_muuttujaan_tallennus_onnistuu(self):
        tulos = Laskin.tallenna_muuttujaan("A", "35", self.muuttujat)
        self.assertEqual({"A" : "35"}, tulos)

    def test_jos_sulut_eivat_lopu_syotetta_ei_hyvaksyta(self):
        self.assertFalse(Laskin.laske_tulos("3 + (4 + 5", self.muuttujat))

    def test_nollallajako(self):
        tulos = Laskin.laske_tulos("5/0", self.muuttujat)
        self.assertFalse(tulos)
