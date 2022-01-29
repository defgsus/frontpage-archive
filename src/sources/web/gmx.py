from ...scraper import Scraper


class GMX(Scraper):
    ID = "gmx.net"
    URL = "https://www.gmx.net/"
    SUB_URLS = [
        ("index.html", URL),
        ("news.html", URL + "magazine/"),
        ("sport.html", URL + "magazine/sport/"),
        ("unterhaltung.html", URL + "magazine/unterhaltung/"),
        ("ratgeber.html", URL + "magazine/ratgeber/"),
        ("auto.html", URL + "magazine/auto/"),

        ("impressum.html", URL + "impressum/"),
        ("datenschutz.html", URL + "datenschutz/"),
    ]
