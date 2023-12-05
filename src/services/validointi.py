from collections import deque
import math

# Miinus voi kuulua sekä numeroon että olla operaattori joten se käsitellään erikoistapauksena.
sallitut = ["0","1","2","3","4","5","6","7","8","9",".",",","+","-","x","*",
                "%","/","(",")"," ","^","e"]
numerot = ["0","1","2","3","4","5","6","7","8","9",".",",","e"]
oper = ["+","x","*","%","/","^"]
muutt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Validointi:
    """Luokka tarkistaa syötteen muodon asianmukaisuuden ja muuntaa sen Deque-muotoon.
    """

    @classmethod
    def lausekkeesta_jono(cls, l1, muuttujat):
        """Muuntaa String-syötteen Deque-muotoon, jos se on muodoltaan oikeanlainen.

        Args:
            laus (String): Käyttäjän antama syöte.
            muuttujat (Dictionary): Käytössä olevat muuttujat.

        Returns:
            Syöte Deque-muotoon muutettuna tai String-muotoinen virheilmoitus jos syöte ei kelpaa.
        """

        if not Validointi.alku_loppu(l1):
            return Validointi.virheet(1)
        l2 = Validointi.muunnokset(l1)
        l3 = Validointi.juurimuunnos(l2)
        if not l3:
            return Validointi.virheet(3)
        l4 = Validointi.muuttujat_ja_piit(l3, muuttujat)
        if not l4:
            return Validointi.virheet(6)
        l5 = Validointi.trigonometria_logaritmi(l4)
        if not l5:
            return Validointi.virheet(4)
        l6 = Validointi.perakkaiset_merkit_ja_sulut(l5)
        if not l6:
            return Validointi.virheet(5)
        lauseke = l6.strip()
        lausekejono = deque()
        i = 0
        numero = ""
        edellinen = ""
        # Jos lausekkeen alussa on -, sen on pakko liittyä miinusmerkkiseen numeroon.
        if lauseke[0] == "-":
            numero = "-"
            i = 1
        while i < len(lauseke):
            if lauseke[i] != " ":
                if lauseke[i] not in sallitut:
                    return Validointi.virheet(2)
                if lauseke[i] == "-":
                    if edellinen in oper or edellinen == "-" or edellinen == "(":
                        numero = "-"
                    elif edellinen == "e":
                        numero = numero+lauseke[i]
                    else:
                        if len(numero) != 0:
                            lausekejono.append(numero)
                            numero = ""
                        lausekejono.append("-")
                elif lauseke[i] in numerot:
                    numero = numero + lauseke[i]
                else:
                    if len(numero) != 0:
                        lausekejono.append(numero)
                        numero = ""
                    lausekejono.append(lauseke[i])
                edellinen = lauseke[i]
            i = i+1
        if len(numero) != 0:
            lausekejono.append(numero)
        return lausekejono

    @classmethod
    def alku_loppu(cls, lauseke):
        """Tarkistetaan että lauseke alkaa ja loppuu sallitulla merkillä.

        Args:
            lauseke (String): Käsiteltävänä oleva syöte.

        Returns:
            True jos virheellisiä merkkejä ei löydetä; False muuten.
        """

        if lauseke[0] in oper or lauseke[0] == ")":
            return False
        if lauseke[-1] in oper or lauseke[-1] in ("(", ".", ",","-","s","n","c","t","l"):
            return False
        if lauseke[0] == "-" and lauseke[1] not in numerot:
            return False
        return True

    @classmethod
    def perakkaiset_merkit_ja_sulut(cls, l):
        """Tarkistaa syötteen muotoa peräkkäisten merkkien ja sulkujen täsmäävyyden osalta.

        Args:
            lauseke (String): Käsiteltävänä oleva syöte.

        Returns:
            Tarkistettu lauseke tai False, jos syöte on todettu virheellisen muotoiseksi.
        """

        edellinen = l[0]
        vali = False
        if l[0] == "(":
            sulkuja_auki = 1
        else:
            sulkuja_auki = 0
        i = 1
        while i < len(l):
            if l[i] == " ":
                vali = True
            else:
                if l[i] == "(" and edellinen in numerot:
                    return False
                if l[i] in numerot and (edellinen in numerot and vali):
                    return False
                if l[i] in oper and (edellinen in oper or edellinen == "-"):
                    return False
                if l[i] in numerot and edellinen == ")":
                    return False
                if l[i] == "." and edellinen == ".":
                    return False
                if l[i] == "(":
                    sulkuja_auki = sulkuja_auki + 1
                if l[i] == ")":
                    sulkuja_auki = sulkuja_auki - 1
                edellinen = l[i]
                vali = False
            i = i+1
        if sulkuja_auki != 0:
            return False
        return l

    @classmethod
    def muunnokset(cls, lauseke):
        """Muunnetaan syötetyt merkit helpommin käsiteltäviksi.

        Args:
            lauseke (String): Käsiteltävänä oleva syöte.

        Returns:
            Syöte, josta ylimääräiset tai väärät merkit on poistettu.
        """

        mappaukset = [('sqrt','s'), ('sq','s'), (',','.'), ('x','*'), ('%','/'),
            ('min', 'a'), ('max', 'b'), ('pi', 'p'), ('sin', 'n'), ('cos', 'c'), ('tan', 't'),
            ('ln','l'), ('log','o')]
        [lauseke := lauseke.replace(x, y) for x, y in mappaukset] # pylint: disable=expression-not-assigned
        return lauseke

    @classmethod
    def juurimuunnos(cls, lauseke):
        """Muunnetaan juuret potenssimuotoon käsittelyn helpottamiseksi.

        Args:
            lauseke (String): Käsiteltävänä oleva syöte.

        Returns:
            Syöte Stringinä juuret muutettuna potenssimerkinnöiksi tai False jos syöte virheellinen.
        """

        i = 0
        while i < len(lauseke)-3:
            if lauseke[i] == "s":
                alku = i
                if lauseke[i+1] == "(":
                    juuri = 2
                    i = i+2
                    vanha_lauseke = "s("
                elif lauseke[i+1] in ("2","3","4","5","6","7","8","9") and lauseke[i+2] == "(":
                    juuri = lauseke[i+1]
                    i = i+3
                    vanha_lauseke = "s"+juuri+"("
                else:
                    return False
                uusi_lauseke = "("+lauseke[i]
                vanha_lauseke = vanha_lauseke+lauseke[i]
                sulkuja_auki = 1
                while True:
                    i = i+1
                    vanha_lauseke = vanha_lauseke+lauseke[i]
                    if lauseke[i] == ")":
                        sulkuja_auki = sulkuja_auki-1
                        if sulkuja_auki == 0:
                            uusi_lauseke = uusi_lauseke+")^(1/"+str(juuri)+")"
                            break
                    if lauseke[i] == "(":
                        sulkuja_auki = sulkuja_auki+1
                    uusi_lauseke = uusi_lauseke+lauseke[i]
                    if i == len(lauseke)-1:
                        return False
                lauseke = lauseke.replace(vanha_lauseke,uusi_lauseke)
                i = alku
            i = i+1
        return lauseke

    @classmethod
    def muuttujat_ja_piit(cls, lauseke, muuttujat):
        """Muunnetaan lausekkeessa olevat muuttujat ja piit arvoikseen.

        Args:
            lauseke (String): Käsiteltävänä oleva syöte.

        Returns:
            Syöte Stringinä muuttujat ja piit muutettuina arvoikseen tai False jos käytetään ei-määriteltyä muuttujaa.
        """

        i = 0
        while i < len(lauseke):
            if lauseke[i] == "p":
                lauseke = lauseke.replace(lauseke[i], " " + str(math.pi) + " ")
            elif lauseke[i] in muuttujat:
                lauseke = lauseke.replace(lauseke[i], " " + muuttujat[lauseke[i]] + " ")
            elif lauseke[i] in muutt:
                return False
            i = i+1
        return lauseke

    @classmethod
    def trigonometria_logaritmi(cls, lauseke):
        """Muunnetaan trigonometriset funktiot ja logaritmit luvuiksi.

        Args:
            lauseke (String): Käsiteltävänä oleva syöte.

        Returns:
            Syöte Stringinä trigonometriset funktiot muutettuina luvuiksi.
        """

        i = 0
        while i < len(lauseke)-3:
            if lauseke[i] in ("n", "c", "t", "o", "l"):
                operaatio = lauseke[i]
                alku = i
                vanha = operaatio + "(" + lauseke[i+2]
                kanta = 10
                if lauseke[i+1] != "(":
                    if lauseke[i] == "o" and lauseke[i+1] in ("2","3","4","5","6","7","8","9") and lauseke[i+2] == "(":
                        kanta = lauseke[i+1]
                        vanha = operaatio + kanta + "(" + lauseke[i+3]
                        i = i+1
                    else:
                        return False
                i = i+2
                numero = ""
                if lauseke[i] == "-":
                    numero = "-"
                    i = i+1
                    vanha = vanha + lauseke[i]
                if lauseke[i] not in numerot:
                    return False
                numero = numero + lauseke[i]
                while True:
                    i = i+1
                    vanha = vanha + lauseke[i]
                    if lauseke[i] == ")":
                        break
                    if lauseke[i] == "-" and lauseke[i-1] != "e":
                        return False
                    if lauseke[i] not in numerot:
                        return False
                    numero = numero + lauseke[i]
                    if i == len(lauseke)-1:
                        return False
                match operaatio:
                    case "n":
                        lauseke = lauseke.replace(vanha, str(math.sin(float(numero.strip()))))
                    case "c":
                        lauseke = lauseke.replace(vanha, str(math.cos(float(numero.strip()))))
                    case "t":
                        lauseke = lauseke.replace(vanha, str(math.tan(float(numero.strip()))))
                    case "l":
                        if float(numero) <= 0:
                            return False
                        lauseke = lauseke.replace(vanha, str(math.log(float(numero.strip()))))
                    case _:
                        if float(numero) <= 0:
                            return False
                        lauseke = lauseke.replace(vanha, str(math.log(float(numero.strip()),int(kanta))))
                i = alku
            i = i+1
        return lauseke

    @classmethod
    def virheet(cls, virhe):
        """Virheilmoitusten vakiolauseet.

        Args:
            virhe (Int): Virhekoodi.

        Returns:
            Virhekoodia vastaava String-muotoinen virheilmoitus.
        """

        match virhe:
            case 1:
                return "Syötteen alussa tai lopussa on virheellinen merkki, tarkista syöte"
            case 2:
                return "Syötteessä on virheellisiä merkkejä, tarkista syöte"
            case 3:
                return "Juurifunktiossa virhe, tarkista syöte"
            case 4:
                return "Trigonometrisessa funktiossa tai logaritmissa virhe, tarkista syöte"
            case 5:
                return "Virheellisiä merkkejä peräkkäin tai sulut eivät täsmää, tarkista syöte"
            case 6:
                return "Käytät muuttujaa joka ei ole määritelty, tarkista syöte"
            case _:
                return "Virheellinen syöte"
