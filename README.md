# Tieteellinen laskin

Tämä on Algoritmit ja tekoäly -harjoitustyönä tehtävä tieteellinen laskin.

[![codecov](https://codecov.io/gh/sari-bee/tieteellinen_laskin/graph/badge.svg?token=EP3JOCDFUW)](https://codecov.io/gh/sari-bee/tieteellinen_laskin)
![CI](https://github.com/sari-bee/tieteellinen_laskin/workflows/CI/badge.svg)

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Testausraportti](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/testausraportti.md)

## Viikkoraportit

[Viikko 1](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko1.md)

[Viikko 2](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko2.md)

[Viikko 3](https://github.com/sari-bee/tieteellinen_laskin/blob/main/dokumentaatio/viikkoraportit/viikko3.md)

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install
```

Käynnistä sovellus komennolla

```bash
poetry run python3 src/index.py
```

Suorita testit komennolla

```bash
poetry run pytest src
```

Aja testikattavuusraportti komennoilla

```bash
poetry run coverage run --branch -m pytest src
poetry run coverage report -m
```

Tee Pylint-tarkastukset komennolla

```bash
poetry run pylint src
```