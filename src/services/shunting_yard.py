from collections import deque

numerot = ["0","1","2","3","4","5","6","7","8","9","."]
operaattorit = ["+","-","*","/"]

class ShuntingYard:

    # funktio ottaa infix-notaatiossa olevan lausekkeen ja palauttaa sen postfix-muodon
    @classmethod
    def rpn_muotoon(cls, lausekejono):
        sulut = False
        numerojono = deque()
        operaattoripino = deque()
        while len(lausekejono) > 0:
            merkki = lausekejono.popleft()
            # aloitetaan sulkujen sisällä oleva lauseke
            if merkki == "(":
                operaattoripino.append("(")
                sulut = True
            # lisätään sulkujen sisällä oleva lauseke jonoon
            if merkki == ")":
                while True:
                    edellinen = operaattoripino.pop()
                    if edellinen == "(":
                        break
                    numerojono.append(edellinen)
                sulut = False
            # kaikki numerot lisätään suoraan jonoon
            # pituusvaatimuksella huomioidaan tässä vaiheessa helpoiten myös miinusmerkkiset numerot
            if merkki in numerot or len(merkki) > 1:
                numerojono.append(merkki)
            if merkki in operaattorit:
                # suluissa olevien lausekkeiden käsittely kokonaisuutena
                if sulut:
                    operaattoripino.append(merkki)
                else:
                    # jos operaattori on + tai -, lisätään mahdolliset aiemmat operaattorit
                    # jonoon ennen näitä koska näiden presedenssi on matalin
                    if merkki in ("+", "-"):
                        while len(operaattoripino) > 0:
                            numerojono.append(operaattoripino.pop())
                    # jos operaattori on * tai %, huomioidaan myös presedenssijärjestys
                    else:
                        while len(operaattoripino) > 0:
                            edellinen = operaattoripino.pop()
                            if edellinen in ("*", "/"):
                                numerojono.append(edellinen)
                            else:
                                operaattoripino.append(edellinen)
                                break
                    operaattoripino.append(merkki)
        while len(operaattoripino) > 0:
            numerojono.append(operaattoripino.pop())
        return numerojono
