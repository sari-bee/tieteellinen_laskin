import unittest
from collections import deque
from services.validointi import Validointi

class TestValidointi(unittest.TestCase):
    def setUp(self):
        self.muuttujat = {"A" : "35", "B" : "3"}

    def test_kielletty_merkki_alussa(self):
        tulos = Validointi.lausekkeesta_jono("+ 3 - 5",self.muuttujat)
        self.assertEqual("Syötteen alussa tai lopussa on virheellinen merkki, tarkista syöte",tulos)

    def test_kielletty_merkki_lopussa(self):
        tulos = Validointi.lausekkeesta_jono("3 - 5 +",self.muuttujat)
        self.assertEqual("Syötteen alussa tai lopussa on virheellinen merkki, tarkista syöte",tulos)

    def test_kaksi_miinusta_alussa(self):
        tulos = Validointi.lausekkeesta_jono("--3+5",self.muuttujat)
        self.assertEqual("Syötteen alussa virheellinen merkki, tarkista syöte", tulos)

    def test_numero_valilyonti_numero(self):
        tulos = Validointi.lausekkeesta_jono("3 5 + 7",self.muuttujat)
        self.assertEqual("Virheellinen syöte", tulos)

    def test_operaattorit_perakkain(self):
        tulos = Validointi.lausekkeesta_jono("3 + + 5",self.muuttujat)
        self.assertEqual("Virheellinen syöte", tulos)

    def test_miinusmerkkinen_numero_alussa(self):
        tulos = Validointi.lausekkeesta_jono("-4*63-2",self.muuttujat)
        self.assertEqual(deque(['-4','*','63','-','2']), tulos)

    def test_miinusmerkkinen_numero_keskella(self):
        tulos = Validointi.lausekkeesta_jono("2 / -4 * 6 - 8",self.muuttujat)
        self.assertEqual(deque(['2', '/', '-4','*','6', '-', '8']), tulos)

    def test_neliojuuri(self):
        tulos = Validointi.lausekkeesta_jono("sqrt(64)",self.muuttujat)
        self.assertEqual(deque(['64','^','0.5']), tulos)

    def test_neliojuuressa_kielletty_merkki(self):
        tulos = Validointi.lausekkeesta_jono("sr(64)",self.muuttujat)
        self.assertEqual("Syötteessä on virheellisiä merkkejä, tarkista syöte", tulos)

    def test_oikein_muodostettu_lausekejono(self):
        tulos = Validointi.lausekkeesta_jono("(2,5+42)x7%2",self.muuttujat)
        self.assertEqual(deque(['(','2.5','+','42',')','*','7','/','2']), tulos)

    def test_muuttuja_muutetaan_arvoksi1(self):
        tulos = Validointi.lausekkeesta_jono("3 + A",self.muuttujat)
        self.assertEqual(deque(['3','+','35']), tulos)

    def test_muuttuja_muutetaan_arvoksi2(self):
        tulos = Validointi.lausekkeesta_jono("5/B+9",self.muuttujat)
        self.assertEqual(deque(['5','/','3','+','9']), tulos)

    def test_virheellinen_syote_hylataan(self):
        tulos = Validointi.lausekkeesta_jono("5+BA",self.muuttujat)
        self.assertEqual(tulos,"Syötteessä on virheellisiä merkkejä, tarkista syöte")

    def test_numero_kesken_kun_muuttuja_syotetaan(self):
        tulos = Validointi.lausekkeesta_jono("4-3B",self.muuttujat)
        self.assertEqual(tulos,"Virheellinen syöte")

    def test_numeron_jalkeen_ei_voi_alkaa_sulut(self):
        tulos = Validointi.lausekkeesta_jono("4+5(7-8)",self.muuttujat)
        self.assertEqual(tulos,"Virheellinen syöte")

    def test_sulkujen_jalkeen_ei_voi_alkaa_numero(self):
        tulos = Validointi.lausekkeesta_jono("4+(5/7)8)",self.muuttujat)
        self.assertEqual(tulos,"Virheellinen syöte")
 