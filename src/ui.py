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
            print("4 Muuttujien alustus")
            print("5 Pikaohje")
            print("6 Lopetus")
            syote = input("Valintasi: ")
            match syote:
                case "1":
                    self.laske()
                case "2":
                    self.muunna()
                case "3":
                    self.minmax()
                case "4":
                    self.muuttujien_alustus()
                case "5":
                    self.ohje()
                case "6":
                    self.lopeta()
                case _:
                    print("-\nValinta virheellinen, kokeile uudestaan\n-")

    def laske(self):
        """Laskimen käyttöliittymä.
        """

        self.kaytossa_olevat_muuttujat()
        while True:
            syote = input("\nAnna laskutoimitus tai palaa päävalikkoon painamalla '!'\n")
            if syote == "!":
                print("\n")
                break
            if syote not in (" ", ""):
                tulos = Laskin.laske_tulos(syote.strip(), self.muuttujat)
                if tulos:
                    print(syote.strip() + " = " + str(tulos) + "\n")
                    t = input("Tallenna tulos antamalla muuttuja A-Z (ohita painamalla enter)\n")
                    if t in muutt:
                        if t in self.muuttujat:
                            syote = input("Muuttuja on varattu, korvaa nykyinen arvo painamalla '!' tai anna toinen muuttuja A-Z\n")
                            if syote == "!":
                                self.muuttuja(t, tulos)
                            elif syote in muutt:
                                self.muuttuja(syote, tulos)
                        else:
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

    def muuttujien_alustus(self):
        """Mahdollistaa muuttujien alustamisen.
        """

        while True:
            self.kaytossa_olevat_muuttujat()
            print("\n1 Kaikkien muuttujien alustus")
            print("2 Yksittäisen muuttujan alustus")
            valinta = input("\nValitse 1 tai 2 tai palaa päävalikkoon painamalla '!'\n")
            match valinta:
                case "!":
                    break
                case "1":
                    syote = input("\nOlet alustamassa kaikki muuttujat. Vahvista valitsemalla K (ohita painamalla enter)\n")
                    if syote in ("K", "k"):
                        self.muuttujat = Laskin.kaikkien_muuttujien_alustus(self.muuttujat)
                case "2":
                    syote = input("\nAnna alustettava muuttuja A-Z (ohita painamalla enter)\n")
                    if syote in self.muuttujat:
                        self.muuttujat = Laskin.yksittaisen_muuttujan_alustus(syote, self.muuttujat)
                case _:
                    print("-\nValinta virheellinen, kokeile uudestaan\n-")
        print("\n")
        self.valikko()

    def muunna(self):
        """Postfix-muunnoksen käyttöliittymä.
        """

        while True:
            syote = input("\nAnna lauseke tai palaa valikkoon painamalla '!'\n")
            if syote == "!":
                print("\n")
                break
            if syote not in (" ", ""):
                rpn = Laskin.muunna_rpn_muotoon(syote.strip(), self.muuttujat)
                if rpn:
                    tulos = ""
                    i = 0
                    while i < len(rpn):
                        tulos = tulos + rpn[i] + " "
                        i = i+1
                    print(syote.strip() + " -> " + tulos + "\n")
        self.valikko()

    def minmax(self):
        """Tulostaa lausekejoukon suurimman ja pienimmän arvon antavat lausekkeet.
        """

        self.kaytossa_olevat_muuttujat()
        lausekkeet = []
        while True:
            if len(lausekkeet) > 0:
                laus = "\nSyötetyt lausekkeet:"
                for item in lausekkeet:
                    laus = laus + "  " + item
                print(laus)
            syote = input("\nAnna vertailtava lauseke tai katso tulos ja lopeta painamalla '!'\n")
            if syote == "!":
                tulos = Laskin.minimit_ja_maksimit(lausekkeet, self.muuttujat)
                if not tulos:
                    print("\nEi vertailtavia arvoja\n")
                else:
                    print("\nMinimi:", tulos[0][0], "=", tulos[0][1])
                    print("Maksimi:", tulos[1][0], "=", tulos[1][1], "\n")
                break
            if syote not in (" ", ""):
                lausekkeet.append(syote.strip())
        self.valikko()

    def ohje(self):
        """Tulostaa komentoriville sovelluksen pikaohjeen.
        """

        print("\n* * * * * * * * * * * * * Pikaohje * * * * * * * * * * * * *")
        print("\nSallitut operaattorit, merkit ja funktiot:")
        print("+, -, *, x, /, %, ^, (), negatiiviset ja positiiviset kokonais-")
        print("ja desimaaliluvut, desimaalierottimena piste tai pilkku. Neliöjuuri")
        print("sqrt(x), y:s (y = 2-9) juuri sqrty(x). Trigonometriset funktiot")
        print("sin(x), cos(x) ja tan(x) sekä pi. Logaritmit log(x), ln(x) ja")
        print("logy(x), missä y = 2-9.")
        print("\nLaskun jälkeen voit tallentaa tuloksen muuttujaan A-Z. Muuttujia")
        print("voi käyttää laskuissa. Päävalikosta voit alustaa muuttujat.")
        print("\nSovellus antaa virheilmoituksen, jos lauseke ei kelpaa. Logaritmien")
        print("ja trigonometristen funktioiden sisällä voi olla vain yksittäisiä lukuja")
        print("tai muuttujia, tallenna tarvittaessa ensin lausekkeen arvo muuttujaan.")
        print("\nMuunnos postfix-muotoon -toiminto:")
        print("Tulostaa syöttämäsi infix-muotoisen lausekkeen postfix-muodossa.")
        print("\nLausekejoukon minimi- ja maksimiarvot -toiminto:")
        print("Tulostaa syöttämiesi lausekkeiden joukosta suurimman ja pienimmän")
        print("arvon antavat lausekkeet arvoineen.")
        print("\nLaajempi ohje dokumentaatiossa.\n")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

    def lopeta(self):
        """Lopettaa ohjelman suorituksen.
        """

        print("\n* * * * * * * * *\n* Nähdään taas! *\n* * * * * * * * *\n")
        sys.exit()
