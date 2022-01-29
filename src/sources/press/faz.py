from typing import Generator, Tuple

from ...scraper import Scraper


class FrankfurterAllgemeine(Scraper):
    ID = "faz.net"
    URL = "https://www.faz.net/"
    SUB_URLS = [
        ("index.html", URL + "aktuell/"),
        ("politik.html", URL + "aktuell/politik/"),
        ("wirtschaft.html", URL + "aktuell/wirtschaft/"),
        ("finanzen.html", URL + "aktuell/finanzen/"),
        ("feuilleton.html", URL + "aktuell/feuilleton/"),
        ("karriere.html", URL + "aktuell/karriere-hochschule/"),
        ("sport.html", URL + "aktuell/sport/"),
        ("gesellschaft.html", URL + "aktuell/gesellschaft/"),
        ("stil.html", URL + "aktuell/stil/"),
        ("rhein-main.html", URL + "aktuell/rhein-main/"),
        ("technik.html", URL + "aktuell/technik-motor/"),
        ("wissen.html", URL + "aktuell/wissen/"),
        ("reise.html", URL + "aktuell/reise/"),
    ]
    SUB_LINK_NAMES = [
        "Impressum",
        "Datenschutz",
    ]

