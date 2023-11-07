import unittest
from collections import deque
from services.validointi import Validointi

class TestValidointi(unittest.TestCase):
    def setUp(self):
        pass

    def test_kielletty_merkki_alussa(self):
        tulos = Validointi.lausekkeesta_jono("+ 3 - 5")
        self.assertEqual("Syötteen alussa on virheellinen merkki, tarkista syöte",tulos)

    def test_kielletty_merkki_lopussa(self):
        tulos = Validointi.lausekkeesta_jono("3 - 5 (")
        self.assertEqual("Syötteen lopussa on virheellinen merkki, tarkista syöte",tulos)

    def test_kaksi_miinusta_alussa(self):
        tulos = Validointi.lausekkeesta_jono("--3+5")
        self.assertEqual("Syötteen alussa virheellinen merkki, tarkista syöte", tulos)

    def test_numero_valilyonti_numero(self):
        tulos = Validointi.lausekkeesta_jono("3 5 + 7")
        self.assertEqual("Virheellinen syöte!", tulos)

    def test_operaattorit_perakkain(self):
        tulos = Validointi.lausekkeesta_jono("3 + + 5")
        self.assertEqual("Virheellinen syöte!", tulos)

    def test_miinusmerkkinen_numero_alussa(self):
        tulos = Validointi.lausekkeesta_jono("-4*63-2")
        self.assertEqual(deque(['-4','*','63','-','2']), tulos)

    def test_miinusmerkkinen_numero_keskella(self):
        tulos = Validointi.lausekkeesta_jono("2 / -4 * 6")
        self.assertEqual(deque(['2', '/', '-4','*','6']), tulos)

    def test_oikein_muodostettu_lausekejono(self):
        tulos = Validointi.lausekkeesta_jono("(2,5+42)x7%2")
        self.assertEqual(deque(['(','2.5','+','42',')','*','7','/','2']), tulos)
