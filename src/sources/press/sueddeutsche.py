from ...scraper import Scraper


class Sueddeutsche(Scraper):
    ID = "sueddeutsche.de"
    URL = "https://www.sueddeutsche.de/"
    SUB_URLS = [
        ("index.html", URL),
        ("plus.html", "https://plus.sueddeutsche.de/"),
        ("politik.html", URL + "politik"),
        ("wirtschaft.html", URL + "wirtschaft"),
        ("meinung.html", URL + "meinung"),
        ("panorama.html", URL + "panorama"),
        ("sport.html", URL + "sport"),

        ("impressum.html", URL + "impressum"),
        ("impressum.html", URL + "datenschutz"),
    ]
