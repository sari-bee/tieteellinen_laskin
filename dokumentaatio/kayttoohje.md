# Käyttöohje: Tieteellinen laskin

## Lataaminen

Lataa projekti [Github-releasena](https://github.com/sari-bee/tieteellinen_laskin/releases)

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install --no-root
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

Sovellus avautuu päävalikkoon. Valitsemalla 1 pääset laskimeen. Valitsemalla 2 voit muuntaa infix-muotoisen lausekkeen postfix-muotoon. Valitsemalla 3 voit tulostaa lausekejoukon suurimman ja pienimmän arvon antavat lausekkeet. Valitsemalla 4 pääset muuttujien alustustoimintoon. Valitsemalla 5 aukeaa pikaohje. Valitsemalla 6 suljet sovelluksen.

### Laskin

Kun avaat laskimen, sovellus tulostaa näkyviin mahdolliset käytössä olevat muuttujat arvoineen. Muuttujat alustetaan aina sovelluksen käynnistyessä; lisäksi voit alustaa ne suorituksen aikana päävalikon kautta. Mahdollisia muuttujia ovat isot kirjaimet A-Z.

Syötä infix-muotoinen matemaattinen lauseke. Mahdollisia lausekkeen osia ovat
- positiiviset ja negatiiviset kokonais- ja desimaaliluvut
- sulut
- peruslaskutoimitukset +, -, * (tai x), / (tai %)
- potenssit ^
- neliöjuuri sqrt(x) (tai sq(x))
- y:nnet juuret sqrty(x) (tai sqy(x)), missä y = 2-9
- trigonometriset funktiot sin(x), cos(x) ja tan(x)
- piin arvo: pi
- kymmenkantainen logaritmi log(x)
- luonnollinen logaritmi ln(x)
- logaritmit logy(x), missä y = 2-9
- käytössä olevat muuttujat
Huomioi, että kaikkien operaattorien tulee olla eksplisiittisesti kirjoitettu lausekkeeseen (esim. älä kirjoita '3A', missä A on muuttuja, vaan '3*A'). Trigonometristen funktioiden ja logaritmien sisällä voi olla vain yksittäisiä lukuja tai muuttujia, laske tarvittaessa ensin funktion sisällä olevan lausekkeen arvo ja tallenna se muuttujaan. Negatiivisessa luvussa miinusmerkin ja luvun tulee olla kirjoitettu yhteen.

Laskin tulostaa lausekkeen arvon ja kysyy, haluatko tallentaa tuloksen muuttujaan. Tallenna tulos muuttujan antamalla haluamasi muuttuja tai ohita painamalla Enter. Jos yrität tallentaa tuloksen käytössä olevaan muuttujaan, sovellus varmistaa haluatko korvata muuttujan nykyisen arvon. Sovellus tulostaa käytössä olevat muuttujat ja palaa laskin-tilaan.

Sovellus antaa virheilmoituksen, jos syötät virheellisen lausekkeen. Takaisin päävalikkoon pääset syöttämällä '!'.

### Muunnos postfix-notaatioon

Syötä infix-muotoinen matemaattinen lauseke. Sovellus palauttaa lausekkeen postfix-muodossa (käänteisessä puolalaisessa notaatiossa, RPN). Mahdolliset muuttujat sekä trigonometriset funktiot ja logaritmit korvataan niiden arvoilla. Huomioi, että kaikkien operaattorien tulee olla eksplisiittisesti kirjoitettu lausekkeeseen (esim. älä kirjoita '3A', missä A on muuttuja, vaan '3*A').

Sovellus antaa virheilmoituksen, jos syötät virheellisen lausekkeen. Takaisin päävalikkoon pääset syöttämällä '!'.

### Lausekejoukon maksimi- ja minimiarvot

Syötä haluamasi määrä matemaattisia lausekkeita, joita haluat vertailla. Voit käyttää myös määriteltyjä muuttujia, jotka tulostuvat näytölle toiminnon avautuessa. Valitsemalla '!' sovellus tulostaa syötetyn joukon suurimman ja pienimmän arvon antavat lausekkeet arvoineen ja palaa päävalikkoon.

### Muuttujien alustus

Toiminnon avautuessa näytölle tulostuvat varattuna olevat muuttujat arvoineen. Valitsemalla 1 voit alustaa kaikki muuttujat. Valitsemalla 2 voit alustaa yksittäisen muuttujan. Takaisin päävalikkoon pääset syöttämällä '!'.

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