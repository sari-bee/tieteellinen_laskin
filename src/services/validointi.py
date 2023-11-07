from collections import deque

# miinus voi kuulua sekä numeroon että olla operaattori joten se käsitellään erikoistapauksena
sallitut = ["0","1","2","3","4","5","6","7","8","9",".",",","+","-","x","*","%","/","(",")"," "]
numerot = ["0","1","2","3","4","5","6","7","8","9",".",","]
oper = ["+","x","*","%","/"]

class Validointi:

    # funktio tarkistaa syötteen muotoa ja muuntaa sen samalla jonoksi
    # shunting yard -käsittelyä varten
    @classmethod
    def lausekkeesta_jono(cls, lauseke):
        # tarkistetaan että lausekkeen alussa ja lopussa ei ole kiellettyjä merkkejä
        if lauseke[0] in oper or lauseke[0] in (")", ".", ","):
            return "Syötteen alussa on virheellinen merkki, tarkista syöte"
        if lauseke[-1] in oper or lauseke[-1] in ("(", ".", ",","-"):
            return "Syötteen lopussa on virheellinen merkki, tarkista syöte"
        lausekejono = deque()
        i = 0
        numero = ""
        edellinen = ""
        numero_kesken = False
        # jos lausekkeen alussa on -, sen on pakko liittyä miinusmerkkiseen numeroon
        if lauseke[0] == "-":
            if lauseke[1] in numerot:
                numero = "-"
                i = 1
                numero_kesken = True
            else:
                return "Syötteen alussa virheellinen merkki, tarkista syöte"
        while i < len(lauseke):
            if lauseke[i] == " ":
                i = i+1
                numero_kesken = False
            else:
                # tarkistetaan ettei syötteessä ole virheellisiä merkkejä
                if lauseke[i] not in sallitut:
                    return "Syötteessä on virheellisiä merkkejä, tarkista syöte"
                # miinusmerkin erityiskäsittely: se voi olla operaattori tai osa lukua
                if lauseke[i] == "-":
                    if edellinen in oper or edellinen == "-" or edellinen == "(":
                        numero = "-"
                        numero_kesken = True
                    else:
                        # jos törmätään operaattoriin, päätellään että edellinen numero päättyi
                        if len(numero) != 0:
                            lausekejono.append(numero)
                            numero_kesken = False
                            numero = ""
                        lausekejono.append("-")
                elif lauseke[i] in numerot:
                    # kahta numeroa joiden välissä on välilyönti ei saa olla peräkkäin
                    if len(numero) != 0 and not numero_kesken:
                        return "Virheellinen syöte!"
                    # sallitaan sekä pilkku että piste desimaalierottimena
                    if lauseke[i] == ",":
                        numero = numero + "."
                    else:
                        numero = numero + lauseke[i]
                    numero_kesken = True
                else:
                    # kahta operaattoria ei saa olla peräkkäin
                    if lauseke[i] in oper and edellinen in oper:
                        return "Virheellinen syöte!"
                    # jos törmätään operaattoriin, päätellään että edellinen numero päättyi
                    if len(numero) != 0:
                        lausekejono.append(numero)
                        numero_kesken = False
                        numero = ""
                    # sallitaan kertomerkkinä sekä x että *
                    if lauseke[i] == "x":
                        lausekejono.append("*")
                    # sallitaan jakolaskumerkkinä sekä % että /
                    elif lauseke[i] == "%":
                        lausekejono.append("/")
                    else:
                        lausekejono.append(lauseke[i])
                edellinen = lauseke[i]
                i = i+1
        if len(numero) != 0:
            lausekejono.append(numero)
        return lausekejono
