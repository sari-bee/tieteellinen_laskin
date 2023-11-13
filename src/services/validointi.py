from collections import deque

# miinus voi kuulua sekä numeroon että olla operaattori joten se käsitellään erikoistapauksena
sallitut = ["0","1","2","3","4","5","6","7","8","9",".",",","+","-","x","*","%","/","(",")"," ","^"]
numerot = ["0","1","2","3","4","5","6","7","8","9",".",","]
oper = ["+","x","*","%","/","^"]

class Validointi:

    # funktio tarkistaa syötteen muotoa ja muuntaa sen samalla jonoksi
    # shunting yard -käsittelyä varten
    @classmethod
    def lausekkeesta_jono(cls, laus, muuttujat):
        if not Validointi.alku_loppu(laus):
            return Validointi.virheet(1)
        lauseke = Validointi.muunnokset(laus)
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
                return Validointi.virheet(2)
        while i < len(lauseke):
            # muuttujat muutetaan arvoiksi
            if lauseke[i] in muuttujat:
                if numero_kesken:
                    return Validointi.virheet(0)
                if i == len(lauseke)-1:
                    lausekejono.append(muuttujat[lauseke[i]])
                    i = i+1
                elif lauseke[i+1] in oper or lauseke[i+1] in ("-", " "):
                    lausekejono.append(muuttujat[lauseke[i]])
                    edellinen = muuttujat[lauseke[i]]
                    i = i+1
                else:
                    return Validointi.virheet(3)
            # alkaako neliöjuuri?
            elif lauseke[i] == "s":
                if lauseke[i+1] != "(":
                    return Validointi.virheet(3)
                i = i+2
                luku = lauseke[i]
                while True:
                    i = i+1
                    if lauseke[i] == ")":
                        lausekejono.append(luku)
                        i = i+1
                        break
                    luku = luku+lauseke[i]
                lausekejono.append("^")
                lausekejono.append("0.5")
            elif lauseke[i] == " ":
                i = i+1
                numero_kesken = False
            else:
                # tarkistetaan ettei syötteessä ole virheellisiä merkkejä
                if lauseke[i] not in sallitut:
                    return Validointi.virheet(3)
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
                        return Validointi.virheet(0)
                    elif edellinen == ")":
                        return Validointi.virheet(0)
                    numero = numero + lauseke[i]
                    numero_kesken = True
                elif lauseke[i] == "(" and edellinen in numerot:
                    return Validointi.virheet(0)
                else:
                    # kahta operaattoria ei saa olla peräkkäin
                    if lauseke[i] in oper and edellinen in oper:
                        return Validointi.virheet(0)
                    # jos törmätään operaattoriin, päätellään että edellinen numero päättyi
                    if len(numero) != 0:
                        lausekejono.append(numero)
                        numero_kesken = False
                        numero = ""
                    lausekejono.append(lauseke[i])
                edellinen = lauseke[i]
                i = i+1
        if len(numero) != 0:
            lausekejono.append(numero)
        return lausekejono

    @classmethod
    def alku_loppu(cls, lauseke):
        # tarkistetaan että lausekkeen alussa ja lopussa ei ole kiellettyjä merkkejä
        if lauseke[0] in oper or lauseke[0] in (")", ".", ","):
            return False
        if lauseke[-1] in oper or lauseke[-1] in ("(", ".", ",","-","s"):
            return False
        return True

    @classmethod
    def muunnokset(cls, lauseke):
        # muunnetaan käytettävä merkistö yhtenäiseksi ja helposti käsiteltäväksi
        mappaukset = [('sqrt','s'), ('sq','s'), (',','.'), ('x','*'), ('%','/')]
        [lauseke := lauseke.replace(a, b) for a, b in mappaukset] # pylint: disable=expression-not-assigned
        return lauseke

    @classmethod
    def virheet(cls, virhe):
        # vakiolauseet virheilmoituksiin
        if virhe == 1:
            return "Syötteen alussa tai lopussa on virheellinen merkki, tarkista syöte"
        if virhe == 2:
            return "Syötteen alussa virheellinen merkki, tarkista syöte"
        if virhe == 3:
            return "Syötteessä on virheellisiä merkkejä, tarkista syöte"
        return "Virheellinen syöte"
