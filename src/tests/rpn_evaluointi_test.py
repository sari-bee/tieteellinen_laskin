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

    def test_nollallajako(self):
        tulos = RPNEvaluointi.laske(deque(['5', '0', '/']))
        self.assertEqual("Yrität jakaa nollalla, yritätkö räjäyttää maailmankaikkeuden?", tulos)

