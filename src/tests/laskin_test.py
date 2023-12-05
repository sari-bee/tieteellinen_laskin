import unittest
from collections import deque
from laskin import Laskin

class TestLaskin(unittest.TestCase):
    def setUp(self):
        self.muuttujat = {}

    def test_peruslausekkeen_oikea_tulos(self):
        tulos = Laskin.laske_tulos("3+5*(1-3^2)", self.muuttujat)
        self.assertEqual(-37.0, tulos)

    def test_neliojuuri_lasketaan_oikein(self):
        tulos = Laskin.laske_tulos("s(64)/2", self.muuttujat)
        self.assertEqual(4, tulos)

    def test_sulkujen_sisalla_oleva_lauseke_oikein(self):
        tulos = Laskin.laske_tulos("5*(1+2*4)", self.muuttujat)
        self.assertEqual(45, tulos)

    def test_useammat_sulut_ymmarretaan_oikein(self):
        tulos = Laskin.laske_tulos("2*(1+2*(1+3*(3-1)))",self.muuttujat)
        self.assertEqual(30,tulos)

    def test_oikeanlainen_rpn(self):
        tulos = Laskin.muunna_rpn_muotoon("3+5*(1-3)", self.muuttujat)
        self.assertEqual(deque(['3', '5', '1', '3', '-', '*', '+']), tulos)

    def test_virheellinen_lauseke_hylataan(self):
        self.assertFalse(Laskin.laske_tulos("ABC", self.muuttujat))

    def test_muuttujaan_tallennus_onnistuu(self):
        tulos = Laskin.tallenna_muuttujaan("A", "35", self.muuttujat)
        self.assertEqual({"A" : "35"}, tulos)

    def test_nollallajako(self):
        self.assertFalse(Laskin.laske_tulos("5/0", self.muuttujat))

    def test_viiden_juuren_sisalla_lauseke(self):
        tulos = Laskin.laske_tulos("sq5(200+2*21+1)", self.muuttujat)
        self.assertEqual(3, tulos)

    def test_minimit_ja_maksimit(self):
        tulos = Laskin.minimit_ja_maksimit(["3+5", "sq(64)", "5*9", "2-7"], self.muuttujat)
        self.assertEqual(tulos[0][1], -5)
        self.assertEqual(tulos[1][1], 45)

    def test_minimit_ja_maksimit_antaa_virheen_jos_ei_tulosta(self):
        self.assertFalse(Laskin.minimit_ja_maksimit(["A", "4**6"], self.muuttujat))

    def test_e_tunnistetaan_oikein(self):
        tulos = Laskin.laske_tulos("1/9999999",self.muuttujat)
        self.assertEqual(tulos, 1.00000010000001e-07)

    def test_kaikkien_muuttujien_alustus(self):
        Laskin.tallenna_muuttujaan("A", "35", self.muuttujat)
        tulos = Laskin.tallenna_muuttujaan("B", "3", self.muuttujat)
        self.assertEqual(tulos, {"A":"35", "B":"3"})
        tulos = Laskin.kaikkien_muuttujien_alustus(self.muuttujat)
        self.assertEqual(tulos,{})

    def test_yhden_muuttujan_alustus(self):
        Laskin.tallenna_muuttujaan("A", "35", self.muuttujat)
        tulos = Laskin.tallenna_muuttujaan("B", "3", self.muuttujat)
        self.assertEqual(tulos, {"A" : "35", "B" : "3"})
        tulos = Laskin.yksittaisen_muuttujan_alustus("A", self.muuttujat)
        self.assertEqual(tulos,{"B" : "3"})
