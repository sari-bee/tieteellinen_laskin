from collections import deque

operaattorit = ["+","-","*","/","^"]

class RPNEvaluointi:
    """Luokan funktiot laskevat matemaattisen lausekkeen arvon.
    """

    @classmethod
    def laske(cls, rpn):
        """Lasketaan postfix-muotoisen lausekkeen arvo.

        Args:
            rpn (Deque): Postfix-muodossa oleva matemaattinen lauseke

        Returns:
            Lausekkeen arvo Float-muodossa tai False, jos ei lausekkeen arvoa voida laskea.
        """

        numeropino = deque()
        tulos = 0
        while len(rpn) > 0:
            merkki = rpn.popleft()
            if merkki in operaattorit:
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
        """Lasketaan yksittäisen operaation tulos.

        Args:
            merkki (String): Operaatiossa käytettävä operaattori.
            eka (Float): Ensimmäinen lukuarvo.
            toka (Float): Toinen lukuarvo.

        Returns:
            Operaation tulos Float-muodossa tai False, jos operaatiossa jaetaan nollalla.
        """

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
