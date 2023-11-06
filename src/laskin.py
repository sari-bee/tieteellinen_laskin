from services.validointi import Validointi
from services.shunting_yard import ShuntingYard
from services.rpn_evaluointi import RPNEvaluointi

class Laskin:

    # luokka välittää varsinaiseen laskimeen liittyviä toimintoja

    @classmethod
    def laske_tulos(cls, lauseke):
        lausekejono = Validointi.lausekkeesta_jono(lauseke)
        # karvalakkiversio siitä ettei virheellisen muotoinen lauseke mene eteenpäin
        if isinstance(lausekejono, str):
            print(lausekejono)
            return False
        rpn = ShuntingYard.rpn_muotoon(lausekejono)
        tulos = RPNEvaluointi.laske(rpn)
        return tulos

    @classmethod
    def muunna_rpn_muotoon(cls, lauseke):
        lausekejono = Validointi.lausekkeesta_jono(lauseke)
        # karvalakkiversio siitä ettei virheellisen muotoinen lauseke mene eteenpäin
        if isinstance(lausekejono, str):
            print(lausekejono)
            return False
        rpn = ShuntingYard.rpn_muotoon(lausekejono)
        return rpn