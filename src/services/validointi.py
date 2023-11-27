from collections import deque

# Miinus voi kuulua sekä numeroon että olla operaattori joten se käsitellään erikoistapauksena.
sallitut = ["0","1","2","3","4","5","6","7","8","9",".",",","+","-","x","*","%","/","(",")"," ","^"]
muutt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numerot = ["0","1","2","3","4","5","6","7","8","9",".",","]
oper = ["+","x","*","%","/","^"]

class Validointi:
    """Luokka tarkistaa syötteen muodon asianmukaisuuden ja muuntaa sen Deque-muotoon.
    """

    @classmethod
    def lausekkeesta_jono(cls, lauseke1, muuttujat):
        """Muuntaa String-syötteen Deque-muotoon, jos se on muodoltaan oikeanlainen.

        Args:
            laus (String): Käyttäjän antama syöte.
            muuttujat (Dictionary): Käytössä olevat muuttujat.

        Returns:
            Syöte Deque-muotoon muutettuna tai String-muotoinen virheilmoitus jos syöte ei kelpaa.
        """

        if not Validointi.alku_loppu(lauseke1):
            return Validointi.virheet(1)
        lauseke2 = Validointi.muunnokset(lauseke1)
        lauseke3 = Validointi.juurimuunnos(lauseke2)
        if not lauseke3:
            return Validointi.virheet(0)
        lauseke = Validointi.perakkaiset_merkit_ja_sulut(lauseke3)
        if not lauseke:
            return Validointi.virheet(0)
        lausekejono = deque()
        i = 0
        numero = ""
        edellinen = ""
        # Jos lausekkeen alussa on -, sen on pakko liittyä miinusmerkkiseen numeroon.
        if lauseke[0] == "-":
            numero = "-"
            i = 1
        while i < len(lauseke):
            # Syötteessä olevat muuttujat muutetaan vastaaviksi arvoiksi.
            if lauseke[i] in muuttujat:
                lausekejono.append(muuttujat[lauseke[i]])
                edellinen = muuttujat[lauseke[i]]
            elif lauseke[i] != " ":
                if lauseke[i] not in sallitut:
                    return Validointi.virheet(2)
                if lauseke[i] == "-":
                    if edellinen in oper or edellinen == "-" or edellinen == "(":
                        numero = "-"
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
        if lauseke[-1] in oper or lauseke[-1] in ("(", ".", ",","-","s"):
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
                if (l[i] in muutt or l[i] == "(") and (edellinen in numerot or edellinen in muutt):
                    return False
                if l[i] in numerot and (edellinen in muutt or (edellinen in numerot and vali)):
                    return False
                if l[i] in oper and (edellinen in oper or edellinen == "-"):
                    return False
                if (l[i] in numerot or l[i] in muutt) and edellinen == ")":
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
            ('min', 'a'), ('max', 'b')]
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
        while i < len(lauseke):
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
                    if lauseke[i] == ")":
                        sulkuja_auki = sulkuja_auki-1
                        if sulkuja_auki == 0:
                            uusi_lauseke = uusi_lauseke+")^(1/"+str(juuri)+")"
                            vanha_lauseke = vanha_lauseke+")"
                            break
                    if lauseke[i] == "(":
                        sulkuja_auki = sulkuja_auki+1
                    uusi_lauseke = uusi_lauseke+lauseke[i]
                    vanha_lauseke = vanha_lauseke+lauseke[i]
                lauseke = lauseke.replace(vanha_lauseke,uusi_lauseke)
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

        if virhe == 1:
            return "Syötteen alussa tai lopussa on virheellinen merkki, tarkista syöte"
        if virhe == 2:
            return "Syötteessä on virheellisiä merkkejä, tarkista syöte"
        return "Virheellinen syöte"
