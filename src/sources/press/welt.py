from ...scraper import Scraper


class Welt(Scraper):
    ID = "welt.de"
    URL = "https://www.welt.de"
    SUB_URLS = [
        ("index.html", URL),
        ("plus.html", URL + "/weltplus/"),
        ("newsticker.html", URL + "/newsticker/"),

        ("politik.html", URL + "/politik/"),
        ("wirtschaft.html", URL + "/wirtschaft/"),
        ("sport.html", URL + "/sport/"),
        ("panorama.html", URL + "/vermischtes/"),
        ("wissen.html", URL + "/wissenschaft/"),
        ("kultur.html", URL + "/kultur/"),
        ("meinung.html", URL + "/debatte/"),
        ("geschichte.html", URL + "/geschichte/"),
        ("reise.html", URL + "/reise/"),
        ("food.html", URL + "/food/"),
        ("regional.html", URL + "/regionales/"),
        ("sonderthemen.html", URL + "/sonderthemen/"),
    ]
    SUB_LINK_NAMES = [
        "Impressum",
        "Datenschutz",
    ]
