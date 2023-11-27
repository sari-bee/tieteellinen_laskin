# Käyttöohje: Tieteellinen laskin

## Lataaminen

Tällä hetkellä voit ladata viimeisimmän version lähdekoodin kloonaamalla projektin. Jatkossa projektista tehdään myös Github-release.

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install
```

Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

Käynnistä sovellus ajaen ensin testit komennolla

```bash
poetry run invoke devstart
```

## Sovelluksen käyttö

Sovellus avautuu päävalikkoon. Valitsemalla 1 pääset laskimeen ja muuttujien hallintaan. Valitsemalla 2 voit muuntaa infix-muotoisen lausekkeen postfix-muotoon. Valitsemalla 3 voit tulostaa lausekejoukon suurimman ja pienimmän arvon antavat lausekkeet. Valitsemalla 4 aukeaa pikaohje. Valitsemalla 5 suljet sovelluksen.

### Laskin

Kun avaat laskimen, sovellus tulostaa näkyviin mahdolliset käytössä olevat muuttujat arvoineen. Muuttujat alustetaan aina sovelluksen käynnistyessä. Mahdollisia muuttujia ovat isot kirjaimet A-Z.

Syötä infix-muotoinen matemaattinen lauseke. Mahdollisia lausekkeen osia ovat positiivisten ja negatiivisten kokonais- ja desimaalilukujen lisäksi sulut, peruslaskutoimitukset +, -, * (tai x), / (tai %), potenssit ^, neliöjuuri sqrt(x) (tai sq(x)), y:nnet juuret sqrty(x) (tai sqy(x)), missä y = 3-9 sekä käytössä olevat muuttujat. Huomioi, että kaikkien operaattorien tulee olla eksplisiittisesti kirjoitettu lausekkeeseen (esim. älä kirjoita '3A', missä A on muuttuja, vaan '3*A'). Lisäksi negatiivisessa luvussa miinusmerkin ja luvun tulee olla kirjoitettu yhteen.

Laskin tulostaa lausekkeen arvon ja kysyy, haluatko tallentaa tuloksen muuttujaan. Tallenna tulos muuttujan antamalla haluamasi muuttuja tai ohita painamalla Enter. Jos tallennat tuloksen käytössä olevaan muuttujaan, vanha arvo korvautuu uudella. Sovellus tulostaa käytössä olevat muuttujat ja palaa laskin-tilaan.

Sovellus antaa virheilmoituksen, jos syötät virheellisen lausekkeen. Takaisin päävalikkoon pääset syöttämällä '!'.

### Muunnos postfix-notaatioon

Syötä infix-muotoinen matemaattinen lauseke. Sovellus palauttaa lausekkeen postfix-muodossa (käänteisessä puolalaisessa notaatiossa, RPN). Mahdolliset muuttujat korvataan niiden arvoilla. Huomioi, että kaikkien operaattorien tulee olla eksplisiittisesti kirjoitettu lausekkeeseen (esim. älä kirjoita '3A', missä A on muuttuja, vaan '3*A').

Sovellus antaa virheilmoituksen, jos syötät virheellisen lausekkeen. Takaisin päävalikkoon pääset syöttämällä '!'.

### Lausekejoukon maksimi- ja minimiarvot

Syötä haluamasi määrä matemaattisia lausekkeita, joita haluat vertailla. Voit käyttää myös määriteltyjä muuttujia, jotka tulostuvat näytölle toiminnon avautuessa. Valitsemalla '!' sovellus tulostaa syötetyn joukon suurimman ja pienimmän arvon antavat lausekkeet arvoineen ja palaa päävalikkoon.

## Testit

Suorita testit komennolla

```bash
poetry run invoke test
```

Aja testikattavuusraportti komennolla

```bash
poetry run invoke coverage
```

Tee Pylint-tarkastukset komennolla

```bash
poetry run invoke lint
```



