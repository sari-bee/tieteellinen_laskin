import unittest
from ui import Tervehdys

class TestTervehdys(unittest.TestCase):
    def test_tervehdys(self):
        self.assertEqual("Hello world!", str(Tervehdys()))