from ...scraper import Scraper


class TOnline(Scraper):
    ID = "t-online.de"
    URL = "https://www.t-online.de/"
    SUB_URLS = [
        ("index.html", URL),
        ("politik.html", URL + "nachrichten/"),
        ("panorama.html", URL + "nachrichten/panorama/"),
        ("sport.html", URL + "sport/"),
        ("unterhaltung.html", URL + "unterhaltung/"),

        ("datenschutz.html", URL + "datenschutz/"),
    ]
    SUB_LINK_NAMES = [
        "Coronavirus",
        "Impressum",
    ]