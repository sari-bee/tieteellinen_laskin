# Tieteellinen laskin

Tämä on Algoritmit ja tekoäly -harjoitustyönä tehtävä tieteellinen laskin.

[![codecov](https://codecov.io/gh/sari-bee/tieteellinen_laskin/graph/badge.svg?token=EP3JOCDFUW)](https://codecov.io/gh/sari-bee/tieteellinen_laskin)
![CI](https://github.com/sari-bee/tieteellinen_laskin/workflows/CI/badge.svg)

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Testausraportti](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/testausraportti.md)

[Toteutusraportti](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/toteutusraportti.md)

## Viikkoraportit

[Viikko 1](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko1.md)

[Viikko 2](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko2.md)

[Viikko 3](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko3.md)

[Viikko 4](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko4.md)

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install
```

Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

Suorita testit komennolla

```bash
poetry run invoke test
```

Käynnistä sovellus suorittaen ensin testit komennolla
```bash
poetry run invoke devstart
```

Aja testikattavuusraportti komennolla

```bash
poetry run invoke coverage
```

Tee Pylint-tarkastukset komennolla

```bash
poetry run invoke lint
```