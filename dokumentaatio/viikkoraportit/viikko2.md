# Viikko 2

Tällä viikolla olen rakentanut perusvalikon komentoriviltä käytettävään sovellukseen. Laskin osaa parsia Reverse Polish Notation -muotoon lausekkeet, jotka sisältävät positiivisia ja negatiivisia kokonaislukuja ja desimaalilukuja, suluissa olevia lausekkeita ja peruslaskutoimituksia +, -, x ja %. Laskin evaluoi RPN-muodossa olevan lausekkeen ja palauttaa sen arvon. Toteutukseen on lisätty myös ensimmäiset syötteen validoinnit.

Olen aloittanut yksikkötestien kirjoittamisen ja testikattavuuden seuraamiseen olen ottanut käyttöön coverage-työkalun. Koodin laadun staattiseen analyysiin olen ottanut käyttöön pylint-työkalun. Koodin kommentoinnin hoidan tässä vaiheessa vapaatekstikommenteilla, mutta myöhemmässä vaiheessa teen tämän strukturoidusti.

Opin tällä viikolla miten shunting yard -algoritmin idea toimii käytännön ohjelmoinnissa. RPN-muodossa olevan lausekkeen evaluointi ei sinänsä ole hankalaa, mutta sitäkään en ollut aiemmin tehnyt joten toki sen idea piti myös miettiä läpi käytännön tasolla.

Suurimmat haasteet tällä viikolla liittyivät siihen että en hartaasta googlaamisesta huolimatta saanut omaa virtuaaliympäristöäni käyttämään konsistentisti Python-versiota 3.10, jonka olin itse määritellyt pienimmäksi sallituksi versioksi vaatimusmäärittelyssä. Tästä syystä jouduin ainakin toistaiseksi hautaamaan haaveet käyttää match-rakennetta, joka selkeyttäisi koodia huomattavasti if-else-rakenteisiin verrattuna. Itse algoritmin rakentaminen oli vielä tässä vaiheessa suhteellisen yksinkertaista, kun laskutoimituksia ja niihin liittyviä presedenssisääntöjä on aika vähän.

Seuraavalla viikolla alan rakentaa muuttujanhallintaa. Lisäksi laajennan toiminnallisuutta potensseihin ja neliöjuuriin. Laajennan ja selkeytän syötteen validointia ja virheellisten syötteiden hylkäämistä. Lisäksi refaktoroin algoritmeja pienemmiksi funktioiksi kun toiminnallisuutta tulee lisää. Aloitan testausraportin kirjoittamisen.

Käytin työhön tällä viikolla aikaa 15 tuntia.