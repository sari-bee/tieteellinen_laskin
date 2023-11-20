import unittest
from collections import deque
from services.shunting_yard import ShuntingYard

class TestShuntingYard(unittest.TestCase):
    def setUp(self):
        pass

    def test_plusmiinus(self):
        tulos = ShuntingYard.rpn_muotoon(deque(['3', '+', '-5', '-', '10']))
        self.assertEqual(deque(['3', '-5', '+', '10', '-']), tulos)

    def test_kertojako(self):
        tulos = ShuntingYard.rpn_muotoon(deque(['3', '*', '5', '/', '7.5']))
        self.assertEqual(deque(['3', '5', '*', '7.5', '/']), tulos)

    def test_potenssi(self):
        tulos = ShuntingYard.rpn_muotoon(deque(['3', '+', '5', '^', '2', '*', '2']))
        self.assertEqual(deque(['3', '5', '2', '^', '2', '*', '+']), tulos)

    def test_sulkulauseke_plusmiinus(self):
        tulos = ShuntingYard.rpn_muotoon(deque(['3', '*', '(', '1', '*', '2', '+', '4', ')']))
        self.assertEqual(deque(['3', '1', '2', '*', '4', '+', '*']), tulos)
        
    def test_sulkulauseke_kertojako(self):
        tulos = ShuntingYard.rpn_muotoon(deque(['3', '*', '(', '1', '*', '2', '/', '4', ')']))
        self.assertEqual(deque(['3', '1', '2', '*', '4', '/', '*']), tulos)