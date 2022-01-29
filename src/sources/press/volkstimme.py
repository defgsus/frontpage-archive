from ...scraper import Scraper


class Volksstimme(Scraper):
    ID = "volksstimme.de"
    URL = "https://www.volksstimme.de/"
    SUB_URLS = [
        ("index.html", URL),

        ("sport.html", URL + "sport"),
        ("deutschland-und-welt.html", URL + "deutschland-und-welt"),
        ("panorama.html", URL + "panorama"),
        ("panorama.html", URL + "panorama"),
        ("panorama.html", URL + "panorama"),
        ("kultur.html", URL + "kultur"),
        ("leben.html", URL + "leben"),
        ("blaulicht.html", URL + "blaulicht"),

        ("impressum.html", URL + "vs/general/impressum-195"),
        ("datenschutz.html", URL + "vs/general/datenschutzerklaerung-198"),
    ]
