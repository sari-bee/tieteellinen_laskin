# Testausraportti
27.11.2023

## Yksikkötestaus

Yksikkötestauksessa käytetään Unittest-kehystä. Automaattisilla testeillä testataan Laskin-luokka sekä Services-kansion luokat. Puhtaasti käyttöliittymän toiminnot jäävät automaattitestauksen ulkopuolelle. Automaattitesteillä testataan paitsi sovelluksen toimintaa oikeanmuotoisilla syötteillä, myös sovelluksen reagointia virheellisiin syötteisiin.

### Testikattavuus

Automaattisia testejä on 45 kappaletta. Testien haarautumakattavuus on 99%.

![Testikattavuus](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/testikattavuus_vko5.jpg) 

Tavoitteena on 100% testauksen kokonaiskattavuus testattavien luokkien osalta ja lisäksi testien tulee testata toiminnallisuuksia mielekkäällä tavalla. Tällä hetkellä muutamat koodirivit jäävät automaattitestien ulkopuolelle. Niiden määrittelemät toiminnallisuudet on testattu manuaalisesti.

## Käyttöliittymätestaus

Käyttöliittymätestaus tullaan toteuttamaan manuaalisesti erikseen suunniteltuja testitapauksia hyödyntäen ja dokumentoidaan tähän raporttiin. Manuaalitestauksessa keskitytään erityisesti käyttöliittymän toimintaan ja käytettävyyteen. Pohjana ovat vaatimusmäärittelydokumentissa mainitut toiminnallisuudet ja toisaalta sovelluksen reagointi mielekkäällä tavalla virheellisiin syötteisiin.

### Käyttöliittymätestauksen testitapaukset

1. Sovelluksen peruskäyttö: Käyttäjä laskee lausekkeen 3x5-2, tallentaa tuloksen muuttujaan A ja tämän jälkeen laskee lausekkeen A+7, jonka arvoksi saadaan 20.

Raportti: Sovellus käynnistyy käyttöä ohjaavaan päävalikkoon. Laskimeen päästään painamalla 1. Sovellus kertoo, ettei muuttujia ole vielä varattuna. Lausekkeen 3x5-2 arvoksi saadaan 13.0. Sovellus kysyy, tallennetaanko tulos muuttujaan ja kertoo, että hyväksyttyjä muuttujia ovat A-Z. Valitaan A, jonka jälkeen sovellus kertoo, että käytössä on muuttuja A = 13.0. Lasketaan A+7, jonka arvoksi saadaan 20.0. Palataan päävalikkoon painamalla ! ja lopetetaan valitsemalla 5.

2. Virheellinen syöte: Käyttäjä syöttää vahingossa laskimeen lausekkeen 3x%-2. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.

Raportti: Ollaan laskimessa. Syötetään 3x%-2. Sovellus kertoo, että kyseessä on "Virheellinen syöte" ja pyytää seuraavaa laskutoimitusta. Virheilmoitus ei ole kovin yksityiskohtainen, mutta sovellus toimii sinänsä luotettavasti.

3. Muuttujan arvon korvaaminen: Käyttäjä tallentaa lausekkeen 3+2 arvon muuttujaan A ja lausekkeen 2-9 arvon muuttujaan B. Tämän jälkeen käyttäjä tallentaa lausekkeen 7+5 arvon muuttujaan A. Muuttujan A arvo on 12, muuttujan B arvo on -7 eikä muita muuttujia ole määritelty.

Raportti: Avataan sovellus ja laskin. Sovellus kertoo, ettei muuttujia ole varattuna. Syötetään 3+2 ja tallennetaan tulos muuttujaan A. Syötetään 2-9 ja tallennetaan tulos muuttujaan B. Sovellus kertoo, että käytössä ovat muuttujat A = 5.0 ja B = -7.0. Syötetään 7+5 ja tallennetaan tulos muuttujaan A. Sovellus kertoo, että käytössä ovat muuttujat A = 12.0 ja B = -7.0.

4. Ei-määritellyn muuttujan käyttö: Käyttäjä tallettaa lausekkeen 3+2 arvon muuttujaan A. Tämän jälkeen käyttäjä yrittää laskea lausekkeen 5+B. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.

Raportti: Avataan sovellus ja laskin. Sovellus kertoo, ettei muuttujia ole varattuna. Syötetään 3+2 ja tallennetaan tulos muuttujaan A. Sovellus kertoo, että käytössä on muuttuja A = 5.0. Syötetään 5+B. Sovellus ilmoittaa "Syötteessä on virheellisiä merkkejä, tarkista syöte" ja pyytää seuraavaa laskutoimitusta. Virheilmoitus ei ole kovin yksityiskohtainen, mutta sovellus toimii luotettavasti.

5. Täysin virheellisten merkkien käyttö: Käyttäjä syöttää lausekkeen 3/q. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.
6. Nollalla jako: Käyttäjä syöttää lausekkeen 3/0. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.
7. Postfix-muodon tulostaminen: Käyttäjä haluaa selvittää lausekkeen 3-5x2 postfix-muodon. Tulokseksi saadaan 3 5 2 * -. (Tämä on sovelluksen toimintaa ja käyttötapaus, jota ei vaatimusmäärittelyssä kuvattu.)
8. Postfix-muotoa ei hyväksytä syötteeksi: Käyttäjä antaa syötteeksi lausekkeen 3 5 2 * -, joka on valmiiksi postfix-muodossa. Sovelluksen tulee antaa selkeä virheilmoitus eikä se saa kaatua.
9. Funktion käyttö: Käyttäjä laskee lausekkeen sq3(2^2x2^2-8). Tulokseksi saadaan 2.
10. Lausekejoukon minimi- ja maksimiarvon selvittäminen: Käyttäjä laskee lausekkeen 3x5 ja tallentaa tuloksen muuttujaan A. Tämän jälkeen minimi- ja maksimiarvotoiminnallisuudelle annetaan lausekkeet Ax2, 5+7, 5+B ja 4-8. Sovellus antaa minimiksi lausekkeen 4-8 ja maksimiksi lausekkeen A*2. Lisäksi sovellus kertoo, että lauseke 5+B on virheellinen.

Käyttöliittymätestauksen yksityiskohtainen raportti täydennetään myöhemmin.

## Muu testaus

Laskimen käyttämät tietorakenneoperaatiot toimivat aikavaativuudella O(1). Pääosa validoinneissa käytettävistä operaatioista toimii aikavaativuudella O(n). Huomioiden toteutuvat aikavaativuudet ja sen, etteivät sovellukselle annettavat syötteet ole tyypillisesti kovin suuria ei suorituskykytestaus ole tämän sovelluksen kontekstissa merkityksellistä. Myöskään vertailua muihin ratkaisuihin ei tehdä. Merkittävin testattava asia on sovelluksen reagointi mielekkäällä tavalla kaikenlaisiin, sekä oikeisiin että virheellisiin syötteisiin; erityisesti sovellus ei saa antaa virheellistä tulosta eikä oikeannäköistä tulosta virheellisellä syötteellä.