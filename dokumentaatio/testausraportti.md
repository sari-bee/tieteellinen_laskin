# Testausraportti
13.11.2023

## Yksikkötestaus

Yksikkötestauksessa käytetään Unittest-kehystä. Automaattisilla testeillä testataan Laskin-luokka sekä Services-kansion luokat. Puhtaasti käyttöliittymän toiminnot jäävät automaattitestauksen ulkopuolelle. Automaattitesteillä testataan paitsi sovelluksen toimintaa oikeanmuotoisilla syötteillä, myös sovelluksen reagointia virheellisiin syötteisiin.

### Testikattavuus

Automaattisia testejä on 32 kappaletta. Testien haarautumakattavuus on 99%.

![Testikattavuus](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/testikattavuus_viikko3.jpg)

Tavoitteena on 100% testauksen kokonaiskattavuus testattavien luokkien osalta ja lisäksi testien tulee testata toiminnallisuuksia mielekkäällä tavalla. Tällä hetkellä muutamat koodirivit jäävät automaattitestien ulkopuolelle. Niiden määrittelemät toiminnallisuudet on testattu manuaalisesti.

## Järjestelmätestaus

Järjestelmätestaus tullaan toteuttamaan manuaalisesti erikseen suunniteltuja testitapauksia hyödyntäen ja dokumentoidaan tähän raporttiin. Manuaalitestauksessa keskitytään erityisesti käyttöliittymän toimintaan ja käytettävyyteen. Pohjana ovat vaatimusmäärittelydokumentissa mainitut toiminnallisuudet ja toisaalta sovelluksen reagointi mielekkäällä tavalla virheellisiin syötteisiin.

## Muu testaus

Laskimen käyttämät tietorakenneoperaatiot toimivat aikavaativuudella O(1). Osa validoinneissa käytettävistä operaatioista toimii aikavaativuudella O(n). Huomioiden toteutuvat aikavaativuudet ja sen, etteivät sovellukselle annettavat syötteet ole tyypillisesti kovin suuria ei suorituskykytestaus ole tämän sovelluksen kontekstissa merkityksellistä. Myöskään vertailua muihin ratkaisuihin ei tehdä. Merkittävin testattava asia on sovelluksen reagointi mielekkäällä tavalla kaikenlaisiin, sekä oikeisiin että virheellisiin syötteisiin; erityisesti sovellus ei saa antaa virheellistä tulosta eikä tulosta virheellisellä syötteellä.