import sys
from laskin import Laskin

muutt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# käyttöliittymä/sovellusvalikko
class Ui:
    def __init__(self):
        # muuttujat alustetaan aina sovelluksen käynnistyessä
        self.muuttujat = {}

    def suorita(self):
        print("\n* * * * * * * * * * * * *\n* Tervetuloa laskimeen! *\n* * * * * * * * * * * * *\n")
        self.valikko()

    def valikko(self):
        while True:
            print("Valitse vaihtoehdoista:")
            print("1 Laskin")
            print("2 Muunnos postfix-notaatioon")
            print("3 Pikaohje")
            print("4 Lopetus")
            syote = input("Valintasi: ")
            if syote == "1":
                self.laske()
            elif syote == "2":
                self.muunna()
            elif syote == "3":
                print("\nOhje on kesken :(\n")
            elif syote == "4":
                self.lopeta()
            else:
                print("-\nValinta virheellinen, kokeile uudestaan\n-")

    def laske(self):
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
                    t = input("\nTallenna tulos antamalla muuttuja A-Z (ohita painamalla enter)\n")
                    if t in muutt:
                        self.muuttuja(t, tulos)
        self.valikko()

    def muuttuja(self, muuttuja, tulos):
        self.muuttujat = Laskin.tallenna_muuttujaan(muuttuja, tulos, self.muuttujat)
        print("Talletettiin tulos muuttujaan " + muuttuja)
        self.laske()

    def kaytossa_olevat_muuttujat(self):
        if len(self.muuttujat) == 0:
            print("\nEi toistaiseksi muuttujia varattuna.")
        else:
            print("\nKäytössä olevat muuttujat:")
            for key in self.muuttujat:
                print(key + " = " + self.muuttujat[key])

    def muunna(self):
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

    def lopeta(self):
        print("\n* * * * * * * * *\n* Nähdään taas! *\n* * * * * * * * *\n")
        sys.exit()
