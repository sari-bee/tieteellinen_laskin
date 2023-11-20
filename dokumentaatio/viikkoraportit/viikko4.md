# Viikko 4

Tällä viikolla olen korjannut sulkujen sisällä olevien lausekkeiden käsittelyn shunting yard -algoritmilla. Lisäksi olen mahdollistanut muiden juurien (3-9) kuin kahden juuren käsittelyn lausekkeella sqrtx(y) ja olen vähän parantanut myös neliöjuuren käsittelyä. Olen tehnyt ensimmäisen version sovellusvalikon kautta käytettävästä pikaohjeesta. Olen hieman refaktoroinut koodia.

Olen ottanut koodin kommentointiin käyttöön Docstring-kommentit. (Jätin koodiin kuitenkin ainakin tässä vaiheessa myös muutamia algoritmin toimintaa selventäviä vapaatekstikommentteja.) Olen aloittanut toteutusraportin kirjoittamisen. Olen kirjoittanut ensimmäiset käyttöliittymän manuaalitestauksen testitapaukset. Lisäksi olen täydentänyt yksikkötestejä huomioimaan uudet toiminnallisuudet ja olen päivittänyt testausraporttia.

Opin tällä viikolla lisää shunting yard -algoritmin toiminnasta lausekkeissa, joissa on sulkuja. En ollut ensimmäisessä versiossa huomioinut, että sulkujen sisälläkin voi olla lausekkeita, joilla on tietty presedenssijärjestys ja jouduin lukemaan algoritmin ideasta vähän lisää että sain koodin toimimaan oikein. Haastavaa on ollut refaktorointi, koska en alun perin suunnitellut koodia riittävän pieniin itsenäisiin funktioihin perustuvaksi. Sain lähinnä poistettua funktioista toistoa yhdistämällä tapauksia, mutta funktiot ovat edelleen turhan pitkiä ja niitä on vaikea pilkkoa.

Ensi viikolla toteutan min, max-toiminnallisuuden sovellukseen ja lisäksi ainakin pohdin muiden puuttuvien toiminnallisuuksien eli trigonometristen funktioiden ja logaritmien toteutusvaihtoehtoja. Lisään syötteen validointeja ja niitä testaavia yksikkötestejä. Alan kirjoittaa käyttöohjetta ja täydennän toteutusraporttia. Täydennän käyttöliittymän manuaalitestauksen testaussuunnitelmaa ja toteutan ja raportoin ensimmäisiä manuaalitestejä. Teen ensimmäisen vertaisarvioinnin.

Käytin työhön tällä viikolla aikaa 18 tuntia.