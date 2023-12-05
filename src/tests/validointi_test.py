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
        self.assertEqual("Syötteen alussa tai lopussa on virheellinen merkki, tarkista syöte", tulos)

    def test_numero_valilyonti_numero(self):
        tulos = Validointi.lausekkeesta_jono("3 5 + 7",self.muuttujat)
        self.assertEqual("Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte", tulos)

    def test_operaattorit_perakkain(self):
        tulos = Validointi.lausekkeesta_jono("3 + + 5",self.muuttujat)
        self.assertEqual("Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte", tulos)

    def test_kolme_eri_operaattoria_perakkain(self):
        tulos = Validointi.lausekkeesta_jono("4-*+7",self.muuttujat)
        self.assertEqual("Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte", tulos)

    def test_miinukset_perakkain(self):
        tulos = Validointi.lausekkeesta_jono("4 - -5",self.muuttujat)
        self.assertEqual(deque(['4', '-', '-5']), tulos)

    def test_miinusmerkkinen_numero_alussa(self):
        tulos = Validointi.lausekkeesta_jono("-4*63-2",self.muuttujat)
        self.assertEqual(deque(['-4','*','63','-','2']), tulos)

    def test_miinusmerkkinen_numero_keskella(self):
        tulos = Validointi.lausekkeesta_jono("2/-4*6-8",self.muuttujat)
        self.assertEqual(deque(['2', '/', '-4','*','6', '-', '8']), tulos)

    def test_neliojuuri(self):
        tulos = Validointi.lausekkeesta_jono("sqrt(64)",self.muuttujat)
        self.assertEqual(deque(['(','64',')','^','(', '1', '/', '2', ')']), tulos)

    def test_neliojuuressa_kielletty_merkki(self):
        tulos = Validointi.lausekkeesta_jono("sr(64)",self.muuttujat)
        self.assertEqual("Juurifunktiossa virhe, tarkista syöte", tulos)

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
        self.assertEqual(tulos,"Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte")

    def test_muuttujaa_ei_maaritelty(self):
        tulos = Validointi.lausekkeesta_jono("5 + C", self.muuttujat)
        self.assertEqual(tulos,"Käytät muuttujaa joka ei ole määritelty, tarkista syöte")

    def test_aivan_omituisia_merkkeja(self):
        tulos = Validointi.lausekkeesta_jono("5+q",self.muuttujat)
        self.assertEqual(tulos,"Syötteessä on virheellisiä merkkejä, tarkista syöte")

    def test_numero_kesken_kun_muuttuja_syotetaan(self):
        tulos = Validointi.lausekkeesta_jono("4-3B",self.muuttujat)
        self.assertEqual(tulos,"Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte")

    def test_numeron_jalkeen_ei_voi_alkaa_sulut(self):
        tulos = Validointi.lausekkeesta_jono("4+5(7-8)",self.muuttujat)
        self.assertEqual(tulos,"Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte")

    def test_sulkujen_jalkeen_ei_voi_alkaa_numero(self):
        tulos = Validointi.lausekkeesta_jono("4+(5/7)8)",self.muuttujat)
        self.assertEqual(tulos,"Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte")

    def test_liian_suuri_juuri_hylataan(self):
        tulos = Validointi.lausekkeesta_jono("sq14(3)",self.muuttujat)
        self.assertEqual(tulos,"Juurifunktiossa virhe, tarkista syöte")

    def test_juuressa_useammat_sulut(self):
        tulos = Validointi.lausekkeesta_jono("sq5(2*(1+3)^2)",self.muuttujat)
        self.assertEqual(tulos,deque(['(', '2', '*', '(', '1', '+', '3', ')', '^', '2', ')', '^', '(', '1', '/', '5', ')']))

    def test_kahta_pilkkua_ei_saa_olla_perakkain(self):
        tulos = Validointi.lausekkeesta_jono("4+,,5",self.muuttujat)
        self.assertEqual(tulos,"Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte")

    def test_jos_sulut_eivat_lopu_syotetta_ei_hyvaksyta(self):
        tulos = Validointi.lausekkeesta_jono("3 + (4 + 5",self.muuttujat)
        self.assertEqual(tulos,"Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte")

    def test_trigonometriset_funktiot_lasketaan_oikein(self):
        tulos = Validointi.lausekkeesta_jono("sin(-8)+5",self.muuttujat)
        self.assertEqual(tulos,deque(['-0.9893582466233818','+','5']))
        tulos = Validointi.lausekkeesta_jono("cos(-8)+5",self.muuttujat)
        self.assertEqual(tulos,deque(['-0.14550003380861354','+','5']))
        tulos = Validointi.lausekkeesta_jono("tan(-8)+5",self.muuttujat)
        self.assertEqual(tulos,deque(['6.799711455220378','+','5']))

    def test_piin_arvo_muunnetaan_oikein(self):
        tulos = Validointi.lausekkeesta_jono("pi * 2",self.muuttujat)
        self.assertEqual(tulos,deque(['3.141592653589793','*','2']))

    def test_lauseke_sinin_sisalla_tuottaa_virheilmoituksen(self):
        tulos = Validointi.lausekkeesta_jono("sin(3-5)",self.muuttujat)
        self.assertEqual(tulos,"Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")
        tulos = Validointi.lausekkeesta_jono("sin(3*5)",self.muuttujat)
        self.assertEqual(tulos,"Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")

    def test_virheellinen_merkki_sinin_sisalla(self):
        tulos = Validointi.lausekkeesta_jono("sin(qw)",self.muuttujat)
        self.assertEqual(tulos, "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")
        tulos = Validointi.lausekkeesta_jono("sinqw)",self.muuttujat)
        self.assertEqual(tulos, "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")

    def test_kymmenkantainen_logaritmi_lasketaan_oikein(self):
        tulos = Validointi.lausekkeesta_jono("log(3)",self.muuttujat)
        self.assertEqual(tulos,deque(['0.47712125471966244']))

    def test_luonnollinen_logaritmi_lasketaan_oikein(self):
        tulos = Validointi.lausekkeesta_jono("ln(7)",self.muuttujat)
        self.assertEqual(tulos,deque(['1.9459101490553132']))

    def test_kannallinen_logaritmi_lasketaan_oikein(self):
        tulos = Validointi.lausekkeesta_jono("3 + log2(5)",self.muuttujat)
        self.assertEqual(tulos,deque(['3', '+', '2.321928094887362']))

    def test_negatiivinen_logaritmi_antaa_virheen(self):
        tulos = Validointi.lausekkeesta_jono("log(-3)",self.muuttujat)
        self.assertEqual(tulos, "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")
        tulos = Validointi.lausekkeesta_jono("ln(-3)",self.muuttujat)
        self.assertEqual(tulos, "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")
        tulos = Validointi.lausekkeesta_jono("log5(-3)",self.muuttujat)
        self.assertEqual(tulos, "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")

    def test_lauseke_logaritmin_sisalla_tuottaa_virheen(self):
        tulos = Validointi.lausekkeesta_jono("log2(5+6)",self.muuttujat)
        self.assertEqual(tulos, "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")

    def test_exp_tunnistetaan_oikein(self):
        tulos = Validointi.lausekkeesta_jono("3.6e-3*2",self.muuttujat)
        self.assertEqual(tulos,deque(['3.6e-3','*','2']))

    def test_tulee_virheilmoitus_jos_funktiossa_sulut_auki(self):
        tulos = Validointi.lausekkeesta_jono("sin(4356",self.muuttujat)
        self.assertEqual(tulos,"Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte")
        tulos = Validointi.lausekkeesta_jono("sq4(4356",self.muuttujat)
        self.assertEqual(tulos,"Juurifunktiossa virhe, tarkista syöte")
