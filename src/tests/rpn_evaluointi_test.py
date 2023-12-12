import unittest
from collections import deque
from services.rpn_evaluointi import RPNEvaluointi

class TestRPNEvaluointi(unittest.TestCase):
    def setUp(self):
        pass

    def test_plusmiinus(self):
        tulos = RPNEvaluointi.laske(deque(['10', '3', '5', '+', '-']))
        self.assertEqual(2, tulos)

    def test_kertojako(self):
        tulos = RPNEvaluointi.laske(deque(['7.5', '3', '5', '*', '/']))
        self.assertEqual(0.5, tulos)

    def test_potenssi_ja_muuta(self):
        tulos = RPNEvaluointi.laske(deque(['3', '5', '2', '^', '2', '*', '+']))
        self.assertEqual(53, tulos)

    def test_neliojuuri(self):
        tulos = RPNEvaluointi.laske(deque(['8', '1', '3', '/', '^']))
        self.assertEqual(2, tulos)

    def test_nollatulos(self):
        tulos = RPNEvaluointi.laske(deque(['5', '5', '-']))
        self.assertEqual(0, tulos)

    def test_tulos_laskusta_palauttaa_false_vaaralla_operaattorilla(self):
        self.assertFalse(RPNEvaluointi.tulos_laskusta("€",3,4))

    def test_value_error_tunnistetaan(self):
        self.assertFalse(RPNEvaluointi.laske(deque(['a','+','3'])))
