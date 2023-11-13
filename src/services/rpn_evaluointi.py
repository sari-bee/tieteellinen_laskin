from collections import deque

operaattorit = ["+","-","*","/","^"]

class RPNEvaluointi:

    # funktio palauttaa RPN-muodossa olevan lausekkeen arvon
    @classmethod
    def laske(cls, rpn):
        numeropino = deque()
        tulos = 0
        while len(rpn) > 0:
            merkki = rpn.popleft()
            if merkki in operaattorit:
                # numerot pinossa käänteisessä järjestyksessä
                eka = float(numeropino.pop())
                toka = float(numeropino.pop())
                tulos = RPNEvaluointi.tulos_laskusta(merkki, eka, toka)
                if tulos:
                    numeropino.append(tulos)
                else:
                    return False
            else:
                numeropino.append(merkki)
        return numeropino.pop()

    @classmethod
    def tulos_laskusta(cls,merkki,eka,toka):
        if merkki == "+":
            tulos = toka+eka
        elif merkki == "-":
            tulos = toka-eka
        elif merkki == "*":
            tulos = toka*eka
        elif merkki == "^":
            tulos = toka**eka
        else:
            if eka == 0:
                print("Yrität jakaa nollalla, yritätkö räjäyttää maailmankaikkeuden?")
                return False
            tulos = toka/eka
        return tulos
