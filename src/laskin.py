from services.validointi import Validointi
from services.shunting_yard import ShuntingYard
from services.rpn_evaluointi import RPNEvaluointi

class Laskin:
    """Luokka välittää laskimeen liittyviä toimintoja käyttöliittymän ja palveluiden välillä.
    """

    @classmethod
    def muunna_rpn_muotoon(cls, lauseke, muuttujat):
        """Muuntaa infix-muotoisen lausekkeen postfix-muotoon.

        Args:
            lauseke (Deque): Infix-muotoinen matemaattinen lauseke.
            muuttujat (Dictionary): Käytössä olevat muuttujat.

        Returns:
            Deque, jossa matemaattinen lauseke postfix-muodossa tai False, jos lauseketta ei saada.
        """

        lausekejono = Validointi.lausekkeesta_jono(lauseke, muuttujat)
        # Jos validointi on tuottanut String-muotoisen virheilmoituksen, tulostetaan se
        if isinstance(lausekejono, str):
            print(lauseke,"->",lausekejono)
            return False
        return ShuntingYard.rpn_muotoon(lausekejono)

    @classmethod
    def laske_tulos(cls, lauseke, muuttujat):
        """Laskee annetun matemaattisen lausekkeen arvon.

        Args:
            lauseke (Deque): Infix-muotoinen matemaattinen lauseke.
            muuttujat (Dictionary): Käytössä olevat muuttujat.

        Returns:
            Matemaattisen lausekkeen arvo Float-muodossa tai False, jos laskeminen ei onnistu.
        """

        rpn = Laskin.muunna_rpn_muotoon(lauseke, muuttujat)
        if not rpn:
            return False
        tulos = RPNEvaluointi.laske(rpn)
        if not tulos:
            return False
        # Ilman tätä täsmennystä käyttöliittymä ei tulosta mitään tuloksen ollessa 0.0
        if tulos == 0.0:
            return "0.0"
        return tulos

    @classmethod
    def tallenna_muuttujaan(cls, syote, tulos, muuttujat):
        """Tallentaa lausekkeen arvon muuttujaan.

        Args:
            syote (String): Muuttuja, johon arvo tallennetaan.
            tulos (Float): Lausekkeelle saatu arvo.
            muuttujat (Dictionary): Käytössä olevat muuttujat.

        Returns:
            Päivitetty muuttujien Dictionary.
        """

        muuttujat[syote] = str(tulos)
        return muuttujat

    @classmethod
    def minimit_ja_maksimit(cls, lausekkeet, muuttujat):
        """Laskee lausekejoukon minimi- ja maksimiarvot.

        Args:
            lausekkeet (List): Lista vertailtavia lausekkeita.
        
        Returns:
            Tuple, jossa minimi- ja maksimiarvot.
        """
        arvot = []
        lausekearvoparit = {}
        i = 0
        while i < len(lausekkeet):
            arvo = float(Laskin.laske_tulos(lausekkeet[i], muuttujat))
            if arvo:
                lausekearvoparit[arvo] = lausekkeet[i]
                arvot.append(arvo)
            i = i+1
        if len(arvot) == 0:
            return False
        minimi = min(arvot)
        maksimi = max(arvot)
        return ((lausekearvoparit[minimi], minimi), (lausekearvoparit[maksimi], maksimi))
