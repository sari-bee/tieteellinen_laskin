from collections import deque

numerot = set("0123456789.")
operaattorit = set("+-*/^")

class ShuntingYard:
    """Luokka tuottaa infix-muotoisesta matemaattisesta lausekkeesta postfix-muotoisen.
    """

    @classmethod
    def rpn_muotoon(cls, lausekejono):
        """Muunnetaan infix-muotoinen lauseke postfix-muotoon.

        Args:
            lausekejono (Deque): Infix-muotoinen matemaattinen lauseke Deque-muodossa.

        Returns:
            Postfix-muotoinen lauseke Deque-muodossa tai False, jos lauseke ei ole validi.
        """

        sulkuja_kesken = 0
        numerojono = deque()
        operaattoripino = deque()
        while len(lausekejono) > 0:
            merkki = lausekejono.popleft()
            # Merkitään sulkujen sisällä oleva lauseke alkavaksi.
            if merkki == "(":
                operaattoripino.append("(")
                sulkuja_kesken = sulkuja_kesken + 1
            # Lisätään koko sulkujen sisällä oleva lauseke jonoon.
            if merkki == ")":
                while True:
                    edellinen = operaattoripino.pop()
                    if edellinen == "(":
                        break
                    numerojono.append(edellinen)
                sulkuja_kesken = sulkuja_kesken - 1
            # Kaikki numerot lisätään suoraan jonoon.
            # Pituusvaatimuksella huomioidaan negatiiviset numerot.
            if merkki in numerot or len(merkki) > 1:
                numerojono.append(merkki)
            if merkki in operaattorit:
                if sulkuja_kesken > 0:
                    if merkki != "^":
                        edellinen = operaattoripino.pop()
                        if merkki in ("+","-"):
                            while True:
                                if edellinen == "(":
                                    break
                                numerojono.append(edellinen)
                                edellinen = operaattoripino.pop()
                        elif edellinen != "(":
                            while True:
                                if edellinen not in ("*","/","^"):
                                    break
                                numerojono.append(edellinen)
                                edellinen = operaattoripino.pop()
                        operaattoripino.append(edellinen)
                    operaattoripino.append(merkki)
                else:
                    # Jos operaattori on + tai -, lisätään mahdolliset aiemmat operaattorit
                    # jonoon ennen näitä koska näiden presedenssi on matalin.
                    if merkki in ("+", "-"):
                        while len(operaattoripino) > 0:
                            numerojono.append(operaattoripino.pop())
                    # Jos operaattori on * tai %, vain ^ menee presedenssissä edelle.
                    elif merkki in ("*", "/"):
                        while len(operaattoripino) > 0:
                            edellinen = operaattoripino.pop()
                            if edellinen in ("*", "/", "^"):
                                numerojono.append(edellinen)
                            else:
                                operaattoripino.append(edellinen)
                                break
                    operaattoripino.append(merkki)
        while len(operaattoripino) > 0:
            numerojono.append(operaattoripino.pop())
        return numerojono
