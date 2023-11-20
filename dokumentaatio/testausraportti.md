# Testausraportti
20.11.2023

## Yksikkötestaus

Yksikkötestauksessa käytetään Unittest-kehystä. Automaattisilla testeillä testataan Laskin-luokka sekä Services-kansion luokat. Puhtaasti käyttöliittymän toiminnot jäävät automaattitestauksen ulkopuolelle. Automaattitesteillä testataan paitsi sovelluksen toimintaa oikeanmuotoisilla syötteillä, myös sovelluksen reagointia virheellisiin syötteisiin.

### Testikattavuus

Automaattisia testejä on 38 kappaletta. Testien haarautumakattavuus on 99%.

![Testikattavuus](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/testikattavuus_vko4.jpg)

Tavoitteena on 100% testauksen kokonaiskattavuus testattavien luokkien osalta ja lisäksi testien tulee testata toiminnallisuuksia mielekkäällä tavalla. Tällä hetkellä muutamat koodirivit jäävät automaattitestien ulkopuolelle. Niiden määrittelemät toiminnallisuudet on testattu manuaalisesti.

## Käyttöliittymätestaus

Käyttöliittymätestaus tullaan toteuttamaan manuaalisesti erikseen suunniteltuja testitapauksia hyödyntäen ja dokumentoidaan tähän raporttiin. Manuaalitestauksessa keskitytään erityisesti käyttöliittymän toimintaan ja käytettävyyteen. Pohjana ovat vaatimusmäärittelydokumentissa mainitut toiminnallisuudet ja toisaalta sovelluksen reagointi mielekkäällä tavalla virheellisiin syötteisiin.

### Käyttöliittymätestauksen testitapaukset

1. Sovelluksen peruskäyttö: Käyttäjä laskee lausekkeen 3*5-2, tallentaa tuloksen muuttujaan A ja tämän jälkeen laskee lausekkeen A+7, jonka arvoksi saadaan 20.
2. Virheellinen syöte: Käyttäjä syöttää vahingossa laskimeen lausekkeen 3*%-2. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.
3. Muuttujan arvon korvaaminen: Käyttäjä tallettaa lausekkeen 3+2 arvon muuttujaan A. Tämän jälkeen käyttäjä tallettaa lausekkeen 7+5 arvon muuttujaan A. Muuttujan A arvo on 12 eikä muita muuttujia ole määritelty.
4. Ei-määritellyn muuttujan käyttö: Käyttäjä tallettaa lausekkeen 3+2 arvon muuttujaan A. Tämän jälkeen käyttäjä yrittää laskea lausekkeen 5+B. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.
5. Postfix-muodon tulostaminen: Käyttäjä haluaa selvittää lausekkeen 3-5*2 postfix-muodon. Tulokseksi saadaan 3 5 2 * -. (Tämä on sovelluksen toimintaa ja käyttötapaus, jota ei vaatimusmäärittelyssä kuvattu.)
6. Postfix-muotoa ei hyväksytä syötteeksi: Käyttäjä antaa syötteeksi lausekkeen 3 5 2 * -, joka on valmiiksi postfix-muodossa. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.

Testitapauksia täydennetään ja käyttöliittymätestauksen yksityiskohtainen raportti kirjoitetaan myöhemmin.

## Muu testaus

Laskimen käyttämät tietorakenneoperaatiot toimivat aikavaativuudella O(1). Osa validoinneissa käytettävistä operaatioista toimii aikavaativuudella O(n). Huomioiden toteutuvat aikavaativuudet ja sen, etteivät sovellukselle annettavat syötteet ole tyypillisesti kovin suuria ei suorituskykytestaus ole tämän sovelluksen kontekstissa merkityksellistä. Myöskään vertailua muihin ratkaisuihin ei tehdä. Merkittävin testattava asia on sovelluksen reagointi mielekkäällä tavalla kaikenlaisiin, sekä oikeisiin että virheellisiin syötteisiin; erityisesti sovellus ei saa antaa virheellistä tulosta eikä tulosta virheellisellä syötteellä.