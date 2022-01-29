from typing import Generator, Tuple

from ...scraper import Scraper


class FrankfurterRundschau(Scraper):
    ID = "fr.de"
    URL = "https://www.fr.de/"
    SUB_URLS = [
        ("index.html", URL),
        ("politik.html", URL + "politik/"),
        ("meinung.html", URL + "meinung/"),
        ("eintracht-frankfurt.html", URL + "eintracht-frankfurt/"),
        ("frankfurt.html", URL + "frankfurt/"),
        ("wissen.html", URL + "wissen/"),
        ("panorama.html", URL + "panorama/"),
        ("impressum.html", URL + "ueber-uns/impressum/"),
        ("datenschutz.html", URL + "ueber-uns/datenschutz/"),
    ]

