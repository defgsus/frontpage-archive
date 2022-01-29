from ..scraper import Scraper


class Compact(Scraper):
    ID = "compact-online.de"
    URL = "https://www.compact-online.de/"
    SUB_URLS = [
        ("index.html", URL),

        ("plus.html", URL + "plus/"),
        ("aktuell.html", URL + "compact-aktuell/"),
        ("tv.html", "https://tv.compact-online.de/"),

        ("impressum.html", URL + "rechtliches/impressum/"),
        ("datenschutz.html", URL + "rechtliches/datenschutz/"),
    ]
