from collections import deque

operaattorit = ["+","-","*","/"]

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
                if merkki == "+":
                    tulos = toka+eka
                elif merkki == "-":
                    tulos = toka-eka
                elif merkki == "*":
                    tulos = toka*eka
                else:
                    if eka == 0:
                        return "Yrität jakaa nollalla, yritätkö räjäyttää maailmankaikkeuden?"
                    tulos = toka/eka
                numeropino.append(tulos)
            else:
                numeropino.append(merkki)
        return numeropino.pop()
