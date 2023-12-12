from collections import deque

operaattorit = set("+-*/^")

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
                try:
                    eka = float(numeropino.pop())
                    toka = float(numeropino.pop())
                except ValueError:
                    print("Virheellinen syöte")
                    return False
                tulos = RPNEvaluointi.tulos_laskusta(merkki, eka, toka)
                if str(tulos) == "0.0":
                    numeropino.append(tulos)
                elif not tulos:
                    return False
                else:
                    numeropino.append(tulos)
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
            Operaation tulos Float-muodossa tai virheviesti, jos operaatio ei onnistu.
        """
        try:
            match merkki:
                case "+":
                    return toka+eka
                case "-":
                    return toka-eka
                case "*":
                    return toka*eka
                case "^":
                    return toka**eka
                case "/":
                    return toka/eka
                case _:
                    return False
        except OverflowError:
            print("Tulos tai osatulos liian suuri, ylivuoto")
            return False
        except ZeroDivisionError:
            print("Yrität jakaa nollalla, yritätkö räjäyttää maailmankaikkeuden?")
            return False
