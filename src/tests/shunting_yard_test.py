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