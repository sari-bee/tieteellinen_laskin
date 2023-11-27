import sys
from laskin import Laskin

muutt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Ui:
    """Luokka, joka tuottaa käyttöliittymän ja sovellusvalikon.
    """

    def __init__(self):
        """Konstruktori alustaa tyhjän dictionaryn muuttujien hallintaan sovelluksen käynnistyessä.
        """

        self.muuttujat = {}

    def suorita(self):
        """Laskimen käynnistyessä suoritettava funktio, joka käynnistää sovellusvalikon.
        """

        print("\n* * * * * * * * * * * * *\n* Tervetuloa laskimeen! *\n* * * * * * * * * * * * *\n")
        self.valikko()

    def valikko(self):
        """Tulostaa sovellusvalikon ja kutsuu muita funktioita käyttäjän valintojen perusteella.
        """

        while True:
            print("Valitse vaihtoehdoista:")
            print("1 Laskin")
            print("2 Muunnos postfix-notaatioon")
            print("3 Lausekejoukon minimi- ja maksimiarvot")
            print("4 Pikaohje")
            print("5 Lopetus")
            syote = input("Valintasi: ")
            if syote == "1":
                self.laske()
            elif syote == "2":
                self.muunna()
            elif syote == "3":
                self.minmax()
            elif syote == "4":
                self.ohje()
            elif syote == "5":
                self.lopeta()
            else:
                print("-\nValinta virheellinen, kokeile uudestaan\n-")

    def laske(self):
        """Laskimen käyttöliittymä.
        """

        self.kaytossa_olevat_muuttujat()
        while True:
            syote = input("\nAnna laskutoimitus tai palaa päävalikkoon painamalla !\n")
            if syote == "!":
                print("\n")
                break
            if syote not in (" ", ""):
                tulos = Laskin.laske_tulos(syote, self.muuttujat)
                if tulos:
                    print(syote + " = " + str(tulos) + "\n")
                    t = input("Tallenna tulos antamalla muuttuja A-Z (ohita painamalla enter)\n")
                    if t in muutt:
                        self.muuttuja(t, tulos)
        self.valikko()

    def muuttuja(self, muuttuja, tulos):
        """Tallentaa laskun tuloksen muuttujaan.

        Args:
            muuttuja (String): Muuttuja, johon tulos halutaan tallentaa.
            tulos (Float): Muuttujaan tallennettava tulos.
        """

        self.muuttujat = Laskin.tallenna_muuttujaan(muuttuja, tulos, self.muuttujat)
        print("Talletettiin tulos muuttujaan " + muuttuja)
        self.laske()

    def kaytossa_olevat_muuttujat(self):
        """Tulostaa listan käytössä olevista muuttujista ja niiden arvoista.
        """

        if len(self.muuttujat) == 0:
            print("\nEi toistaiseksi muuttujia varattuna.")
        else:
            print("\nKäytössä olevat muuttujat:")
            for key in self.muuttujat:
                print(key + " = " + self.muuttujat[key])

    def muunna(self):
        """Postfix-muunnoksen käyttöliittymä.
        """

        while True:
            syote = input("\nAnna lauseke tai palaa valikkoon painamalla '!'\n")
            if syote == "!":
                print("\n")
                break
            if syote not in (" ", ""):
                rpn = Laskin.muunna_rpn_muotoon(syote, self.muuttujat)
                if rpn:
                    tulos = ""
                    i = 0
                    while i < len(rpn):
                        tulos = tulos + rpn[i] + " "
                        i = i+1
                    print(syote + " -> " + tulos + "\n")
        self.valikko()

    def minmax(self):
        """Tulostaa lausekejoukon suurimman ja pienimmän arvon antavat lausekkeet.
        """
        self.kaytossa_olevat_muuttujat()
        lausekkeet = []
        while True:
            syote = input("\nAnna vertailtava lauseke tai katso tulos ja lopeta painamalla '!'\n")
            if syote == "!":
                tulos = Laskin.minimit_ja_maksimit(lausekkeet, self.muuttujat)
                print("\n")
                if not tulos:
                    print("Ei vertailtavia arvoja")
                else:
                    print("Minimi:", tulos[0][0], "=", tulos[0][1])
                    print("Maksimi:", tulos[1][0], "=", tulos[1][1])
                print("\n")
                break
            if syote not in (" ", ""):
                lausekkeet.append(syote)
        self.valikko()

    def ohje(self):
        """Tulostaa komentoriville sovelluksen pikaohjeen.
        """

        print("\n* * * * * * * * * * * * Pikaohje * * * * * * * * * * * *")
        print("Sallitut operaattorit ja merkit: +, -, *, x, /, %, ^, (),")
        print("negatiiviset ja positiiviset kokonais- ja desimaaliluvut,")
        print("desimaalierottimena piste tai pilkku, neliöjuuri sq(x) tai")
        print("sqrt(x), y:s (y = 3-9) juuri sqy(x) tai sqrty(x). Laskun")
        print("jälkeen voit tallentaa tuloksen muuttujaan A-Z. Jos tallennat")
        print("arvon käytössä olevaan muuttujaan, vanha arvo korvautuu")
        print("uudella. Sovellus antaa virheilmoituksen, jos syöttämäsi")
        print("lauseke ei kelpaa. Muunnos postfix-muotoon -toiminnossa")
        print("voit tulostaa haluamasi infix-muotoisen lausekkeen postfix-")
        print("muodossa. Lausekejoukon minimi- ja maksimiarvot -toiminto")
        print("tulostaa syöttämiesi lausekkeiden joukosta suurimman ja")
        print("pienimmän arvon antavat lausekkeet arvoineen. Voit käyttää")
        print("myös määriteltyjä muuttujia. Laajempi ohje dokumentaatiossa.")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

    def lopeta(self):
        """Lopettaa ohjelman suorituksen.
        """

        print("\n* * * * * * * * *\n* Nähdään taas! *\n* * * * * * * * *\n")
        sys.exit()
