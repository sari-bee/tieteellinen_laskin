# Koodissa ei ole vielä mitään toiminnallisuutta, vain runko komentoriviltä käytettävälle
# sovellukselle ja testeille.

class Tervehdys:
    def __init__(self):
        self.tervehdys = "Hello world!"

    def __str__(self):
        return self.tervehdys

class Ui:
    def __init__(self):
        pass

    def suorita(self):
        while True:
            syote = input("Anna laskutoimitus tai lopeta painamalla L:\n")
            if syote == "L" or syote == "l":
                print("Kiitos!")
                break
            else:
                print(syote)
