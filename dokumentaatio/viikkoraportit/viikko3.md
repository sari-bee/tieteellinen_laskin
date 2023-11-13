# Viikko 3

Tällä viikolla olen laajentanut laskimen toiminnallisuutta ymmärtämään potensseja ja neliöjuuria (kahden juuri, sqrt(X)). Lisäksi olen mahdollistanut arvon sijoittamisen muuttujaan. Olen hieman refaktoroinut koodia ja olen lisännyt validointeja syötteen tarkistukseen.

Olen lisännyt yksikkötestejä ja aloittanut testausraportin kirjoittamisen. Testikattavuutta seurataan coverage-työkalulla, ja uusin testikattavuusraportti päivitetään testausdokumenttiin. Koodin laadun seuraamiseen on käytössä Pylint-tarkistus, ja kaikki huomiot joko korjataan tai niistä tehdään korjaussuunnitelma tuleville viikoille.

Suurin oppi tällä viikolla oli keksiä, miten toteutan muuttujanhallinnan käytännössä ja miten rakennan sen käyttöliittymään niin että se on näppärä mutta kuitenkin selkeä käyttää. Haastavaa oli myös miettiä, miten refaktoroin koodia pieniin funktioihin niin, että toiminnallisuus pysyisi kuitenkin selkeänä, ja tämä jäikin vielä osin pohdittavaksi. Haastavaa on myös miettiä testaustapauksia kattamaan mahdollisimman paljon erilaisia virheellisiä syötteitä.

Ensi viikolla toiminnallisuuksien osalta lisään mahdollisuuden käyttää myös muita juuria ja korjaan sulkujen sisällä olevan lausekkeen evaluoinnin huomioimaan presedenssijärjestyksen. Aloitan sovellusvalikon kautta käytettävän pikaohjeen kirjoittamisen. Teen koodin refaktorointia lisää, erityisesti validointien osalta ja otan koodin kommentointiin käyttöön Docstring-kommentit. Alan kirjoittaa toteutusraporttia. Alan suunnitella käyttöliittymän manuaalitestauksen testitapauksia.

Käytin työhön tällä viikolla aikaa 17 tuntia.