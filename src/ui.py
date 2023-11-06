import sys
from laskin import Laskin

# käyttöliittymä/sovellusvalikko
class Ui:
    def __init__(self):
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
        while True:
            syote = input("\nAnna laskutoimitus tai palaa valikkoon painamalla '!'\n")
            if syote == "!":
                print("\n")
                break
            if syote not in (" ", ""):
                tulos = Laskin.laske_tulos(syote)
                if tulos:
                    print(syote + " = " + str(tulos) + "\n")
        self.valikko()

    def muunna(self):
        while True:
            syote = input("\nAnna lauseke tai palaa valikkoon painamalla '!'\n")
            if syote == "!":
                print("\n")
                break
            if syote not in (" ", ""):
                rpn = Laskin.muunna_rpn_muotoon(syote)
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
