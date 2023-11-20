from collections import deque

# Miinus voi kuulua sekä numeroon että olla operaattori joten se käsitellään erikoistapauksena.
sallitut = ["0","1","2","3","4","5","6","7","8","9",".",",","+","-","x","*","%","/","(",")"," ","^"]
numerot = ["0","1","2","3","4","5","6","7","8","9",".",","]
oper = ["+","x","*","%","/","^"]

class Validointi:
    """Luokka tarkistaa syötteen muodon asianmukaisuuden ja muuntaa sen Deque-muotoon.
    """

    @classmethod
    def lausekkeesta_jono(cls, laus, muuttujat):
        """Muuntaa String-syötteen Deque-muotoon, jos se on muodoltaan oikeanlainen.

        Args:
            laus (String): Käyttäjän antama syöte.
            muuttujat (Dictionary): Käytössä olevat muuttujat.

        Returns:
            Syöte Deque-muotoon muutettuna tai String-muotoinen virheilmoitus jos syöte ei kelpaa.
        """

        if not Validointi.alku_loppu(laus):
            return Validointi.virheet(1)
        lause = Validointi.muunnokset(laus)
        lauseke = Validointi.juurimuunnos(lause)
        if not lauseke:
            return Validointi.virheet(0)
        lausekejono = deque()
        i = 0
        numero = ""
        edellinen = ""
        numero_kesken = False
        # Jos lausekkeen alussa on -, sen on pakko liittyä miinusmerkkiseen numeroon.
        if lauseke[0] == "-":
            if lauseke[1] not in numerot:
                return Validointi.virheet(2)
            numero = "-"
            i = 1
            numero_kesken = True
        while i < len(lauseke):
            # Syötteessä olevat muuttujat muutetaan vastaaviksi arvoiksi.
            if lauseke[i] in muuttujat:
                if numero_kesken:
                    return Validointi.virheet(0)
                if i == len(lauseke)-1 or lauseke[i+1] in oper or lauseke[i+1] in ("-", " "):
                    lausekejono.append(muuttujat[lauseke[i]])
                    edellinen = muuttujat[lauseke[i]]
                else:
                    return Validointi.virheet(3)
            elif lauseke[i] == " ":
                numero_kesken = False
            else:
                if lauseke[i] not in sallitut:
                    return Validointi.virheet(3)
                if lauseke[i] == "-":
                    if edellinen in oper or edellinen == "-" or edellinen == "(":
                        numero = "-"
                        numero_kesken = True
                    else:
                        if len(numero) != 0:
                            lausekejono.append(numero)
                            numero_kesken = False
                            numero = ""
                        lausekejono.append("-")
                elif lauseke[i] in numerot:
                    # Kahta numeroa joiden välissä on välilyönti tai sulku ei saa olla peräkkäin.
                    if (len(numero) != 0 and not numero_kesken) or edellinen == ")":
                        return Validointi.virheet(0)
                    numero = numero + lauseke[i]
                    numero_kesken = True
                elif lauseke[i] == "(" and edellinen in numerot:
                    return Validointi.virheet(0)
                else:
                    # Kahta operaattoria ei saa olla peräkkäin.
                    if lauseke[i] in oper and edellinen in oper:
                        return Validointi.virheet(0)
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
        """Tarkistetaan että lauseke alkaa ja loppuu sallitulla merkillä.

        Args:
            lauseke (String): Käyttäjän syöte.

        Returns:
            True jos virheellisiä merkkejä ei löydetä; False muuten.
        """

        if lauseke[0] in oper or lauseke[0] in (")", ".", ","):
            return False
        if lauseke[-1] in oper or lauseke[-1] in ("(", ".", ",","-","s"):
            return False
        return True

    @classmethod
    def muunnokset(cls, lauseke):
        """Muunnetaan syötetyt matemaattiset funktiot helpommin käsiteltäviksi.

        Args:
            lauseke (String): Käyttäjän syöte.

        Returns:
            Käyttäjän syöte, josta ylimääräiset funktioiden merkit on poistettu.
        """

        mappaukset = [('sqrt','s'), ('sq','s'), (',','.'), ('x','*'), ('%','/')]
        [lauseke := lauseke.replace(a, b) for a, b in mappaukset] # pylint: disable=expression-not-assigned
        return lauseke

    @classmethod
    def juurimuunnos(cls, lauseke):
        """Muunnetaan juuret potenssimuotoon käsittelyn helpottamiseksi.

        Args:
            lauseke (String): Käsiteltävänä oleva käyttäjän syöte

        Returns:
            Syöte String-muodossa niin, että juuret on muutettu potenssimerkinnöiksi.
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
                while True:
                    i = i+1
                    if lauseke[i] == ")":
                        uusi_lauseke = uusi_lauseke+")^(1/"+str(juuri)+")"
                        vanha_lauseke = vanha_lauseke+")"
                        break
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
            return "Syötteen alussa virheellinen merkki, tarkista syöte"
        if virhe == 3:
            return "Syötteessä on virheellisiä merkkejä, tarkista syöte"
        return "Virheellinen syöte"
