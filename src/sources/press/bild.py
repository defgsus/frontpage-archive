from typing import Generator, Tuple

from ...scraper import Scraper


class Bild(Scraper):
    ID = "bild.de"
    URL = "https://www.bild.de"

    SUB_LINK_NAMES = [
        "News",
        "Politik",
        "Regio",
        "Unterhaltung",
        "Sport",
        "Fussball",
        "Lifestyle",
        "Ratgeber",
        "Auto",
        "Digital",
        "Inland",
        "Ausland",
        "Mystery",
        "Ein Herz für Kinder",
        "Kommentare und Kolumnen",
        "Stars",
        "Erotik",
        "Kino",
        "TV",
        "Reise",
        "Gesundheit",
        "Geld & Wirtschaft",
        "Wirtschaft",
        "Impressum",
        "Datenschutz",
    ]
