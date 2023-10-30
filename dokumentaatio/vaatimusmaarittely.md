# Vaatimusmäärittely

Opinto-ohjelma: Tietojenkäsittelytiede, kandidaatin tutkinto

Projekti on komentoriviltä käytettävä tieteellinen laskin joka ottaa syötteenä matemaattisen lausekkeen infix-notaatiossa ja palauttaa lausekkeen arvon.

Projekti toteutetaan Pythonilla ja dokumentoidaan suomeksi. (Pystyn tarvittaessa vertaisarvioimaan myös Javalla toteutettuja ja ruotsiksi tai englanniksi dokumentoituja projekteja.)

Laskin ottaa syötteenään tavanomaisessa muodossa (ns. infix-notaatio) annetun matemaattisen lausekkeen. 
String-muodossa syötetystä lausekkeesta poimitaan yksittäiset tekijät listaksi. Lista parsitaan projektissa toteutettavalla shunting yard -algoritmilla Reverse Polish -notaatioon (ns. postfix-notaatio). Shunting yard -algoritmi perustuu sekä pinon että listan käyttöön. RPN-muodosta evaluoidaan lausekkeen arvo käyttäen pinoa ja palautetaan arvo käyttäjälle. Käytännössä toteutan pinot ja listat deque-tietorakenteella.

Infix-notaatiossa annetun lausekkeen evaluointi ohjelmallisesti on haastavaa, sillä lauseketta pitäisi pystyä tarkastelemaan kokonaisuutena jotta oikea presedenssijärjestys voitaisiin huomioida (suluissa olevat lausekkeet ensin, kertolaskut ennen yhteenlaskuja jne.). Postfix-muodossa olevan lausekkeen evaluointi oikeassa presedenssijärjestyksessä on yksinkertaista pinon avulla, sillä operaatio kohdistuu aina kahteen edelliseen muuttujaan, jotka ovat siis pinon päällä. Tästä syystä muutan infix-notaatiossa olevan lausekkeen postfix-muotoon ennen sen evaluointia.

Deque-tietorakenteessa lisäykset ja otot sekä listan alussa että lopussa ("pino-operaatiot") toimivat aikavaativuudella O(1) joten se on tehokas valinta tähän käyttötarkoitukseen.

Riippuvuuksien hallintaan käytetään Poetryä. Algoritmin oikea toiminta varmistetaan kattavalla yksikkötestauksella Unittest-kehystä hyödyntäen.

## Tekniset vaatimukset

- sovellus toimii unix-pohjaisissa käyttöjärjestelmissä
- Python-version tulee olla vähintään 3.10
- sovelluksen kieli on suomi

## Toiminnalliset vaatimukset

- laskin voidaan käynnistää komentoriviltä
- laskinta käytetään komentoriviltä sovellusvalikon kautta
- laskin hylkää syötteet, joissa on virheellisiä merkkejä tai jotka eivät ole infix-muodossa
    - virheellisistä syötteistä annetaan käyttäjälle huomautus
- laskin parsii Reverse Polish Notation -muotoon lausekkeet, jotka sisältävät
    - kokonaislukuja
    - desimaalilukuja
    - sulkuja
    - peruslaskutoimituksia +, -, x ja %
    - potensseja ja neliöjuuria (sqrt(y) ja sqrtx(y))
    - trigonometrisia funktiota (sin, cos, tan)
    - logaritmeja (logx(y) ja ln(y))
    - max/min -funktioita
    - muuttujia
- laskin evaluoi RPN-muodossa olevan lausekkeen ja palauttaa sen arvon
- tulos voidaan sijoittaa muuttujaan, jota voidaan käyttää jatkolaskuissa
- sovellusvalikosta voidaan avata pikaohje sovelluksen käyttöön
- laajempi ohje laaditaan erikseen repositorioon

## Lähteet

[Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
[Wikipedia: Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)