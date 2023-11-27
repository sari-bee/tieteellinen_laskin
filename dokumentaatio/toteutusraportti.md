# Toteutusraportti

Työssä ei ole käytetty laajoja kielimalleja.

## Ohjelman rakenne

Sovellus on tieteellinen laskin, joka ottaa syötteenään tavanomaisessa ns. infix-notaatiossa annetun matemaattisen lausekkeen, muuntaa sen shunting yard -algoritmia hyödyntäen postfix-notaatioon (Reverse Polish Notation, RPN) ja evaluoi sen RPN-muodosta palauttaen lausekkeen arvon. Saatu tulos voidaan tallentaa muuttujaan, jota voidaan käyttää jatkolaskuissa. Vaatimusmäärittelystä poiketen rakensin sovellukseen myös mahdollisuuden muuntaa infix-notaation postfix-notaatioon evaluoimatta sitä. Lisäksi voidaan palauttaa lausekejoukon minimi- ja maksimiarvon antavat lausekkeet. Sovellusta käytetään komentoriviltä sovellusvalikon ohjaamana.

Sovelluksen käynnistyessä alustetaan muuttujien hallintaan käytettävä dictionary-tietorakenne. Käyttöliittymätoiminnot sijaitsevat UI-luokassa. RPN-konversioon ja lausekkeen evaluointiin sekä muuttujahallintaan liittyviä toiminnallisuuksia välittää Laskin-luokka. Varsinainen sovelluslogiikka sijaitsee services-kansion luokissa Validointi, jossa tarkistetaan syötteen oikeellisuutta, ShuntingYard, jossa muunnetaan syöte RPN-muotoon ja RPNEvaluointi, jossa RPN-muodossa oleva lauseke evaluoidaan ja sen arvo palautetaan. Shunting yard -algoritmi käyttää toiminnassaan jonoa ja pinoa ja evaluointialgoritmi pinoa. Nämä on konkreettisesti toteutettu deque-tietorakenteilla. Minimi-maksimitoiminnallisuudessa käytetään lausekkeiden väliaikaishallintaan listaa (ja lisäksi lauseke-arvoparien hallintaan dictionarya).

## Aikavaativuudet ja suorituskyky

Pino- ja jono-operaatiot toimivat aikavaativuudella O(1). Validoinneista perustuvat pääosin syötteen läpikäyntiin ja toimivat aikavaativuudella O(n), missä n on syötteen koko. Muuttujanhallinnassa käytettävän dictionary-tietorakenteen operaatiot toimivat aikavaativuudella O(1). Koska laskimelle annettavien syötteiden koko ei ole kovin suuri ja koska operaatioiden aikavaativuudet ovat maltillisia, ei algoritmin tehokkuus tässä tapauksessa ole kriittistä toiminnan kannalta eikä niitä ole analysoitu tätä laajemmin.

## Käytettävyys ja syötteiden validointi

Sovellusta käytetään komentoriviltä ohjaavan valikon avulla. Sovelluksessa on myös avattavissa pikaohje, josta selviävät mm. komennot, joita voidaan käyttää matemaattisten funktioiden syöttämiseen. Mikäli käyttäjä antaa virheellisen syötteen, näytetään virheilmoitus. Tällaisia virheellisiä syötteitä ovat mm. ei-sallittujen merkkien käyttäminen, syötteet joissa sulut eivät ole pareittain, syötteet joissa numeroita tai operaattoreita on useampia peräkkäin, syötteet jotka alkavat tai loppuvat operaattorilla, ja yritys jakaa nollalla.

## Puutteet ja parannusehdotukset

Laskimelle olisi voinut rakentaa myös graafisen käyttöliittymän. En halunnut tehdä sitä sillä ajatuksella, että komentorivisovellukselle on helpompi tuoda jokin valmis lauseke esimerkiksi copy-paste-toiminnolla, jolloin laskimen käyttö on joustavampaa. Toisaalta komentorivisovelluksen käyttö tarkoittaa, että syötteen validoinnin tulee olla huomattavasti laajempaa, koska käyttäjä voi antaa syötteeksi mitä vain. Se, olisiko laskimen käyttö graafisella käyttöliittymällä miellyttävämpää on ehkä osin makuasiakin.

Käyttäjälle virheellisestä syötteestä näytettävät virheilmoitukset ovat suhteellisen yleisluontoisia. Arvelin, että käyttäjä kyllä itse huomaa virheen useimmissa tapauksissa, ja hyvin tarkkojen virheilmoitusten rakentaminen olisi tarkoittanut, että erilaisia ilmoitusvaihtoehtoja olisi valtavasti.

Koodin rakenteessa suurin ongelma on, että funktiot ovat pitkiä ja niissä on paljon if-else-rakenteita. Olin suunnitellut käyttäväni match-rakennetta, joka olisi selkeyttänyt koodia, mutta en itse saanut konsistentisti virtuaaliympäristöäni käyttämään Python-versiota 3.10, joka olisi vaatimus match-rakenteen käytölle. Funktioiden pituus johtui myös siitä, että en alun alkaen suunnitellut koodia riittävän huolellisesti, jolloin refaktorointi riittävän pieniksi funktioiksi osoittautui yllättävän hankalaksi. Tästä syystä mm. Pylint-analyysissä koodin laatu jää hieman alle tavoitteen, vaikka käytän suhteellisen liberaaleja Pylint-määrittelyjä.

## Lähteet

[Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

[Wikipedia: Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)