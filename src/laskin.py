from services.validointi import Validointi
from services.shunting_yard import ShuntingYard
from services.rpn_evaluointi import RPNEvaluointi

class Laskin:

    # luokka välittää varsinaiseen laskimeen liittyviä toimintoja

    @classmethod
    def muunna_rpn_muotoon(cls, lauseke, muuttujat):
        lausekejono = Validointi.lausekkeesta_jono(lauseke, muuttujat)
        # karvalakkiversio siitä ettei virheellisen muotoinen lauseke mene eteenpäin
        if isinstance(lausekejono, str):
            print(lausekejono)
            return False
        rpn = ShuntingYard.rpn_muotoon(lausekejono)
        if not rpn:
            return False
        return rpn

    @classmethod
    def laske_tulos(cls, lauseke, muuttujat):
        rpn = Laskin.muunna_rpn_muotoon(lauseke, muuttujat)
        if not rpn:
            return False
        tulos = RPNEvaluointi.laske(rpn)
        if not tulos:
            return False
        # fiksaa omituisen bugin, jossa laskin ei tulosta mitään tuloksen ollessa 0...
        if tulos == 0.0:
            return "0.0"
        return tulos

    @classmethod
    def tallenna_muuttujaan(cls, syote, tulos, muuttujat):
        muuttujat[syote] = str(tulos)
        return muuttujat
        