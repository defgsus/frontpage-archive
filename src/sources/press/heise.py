from ...scraper import Scraper


class Heise(Scraper):
    ID = "heise.de"
    URL = "https://www.heise.de/"
    SUB_URLS = [
        ("index.html", URL),
        ("it.html", URL + "newsticker/it/"),
        ("wissen.html", URL + "newsticker/wissen/"),
        ("mobiles.html", URL + "newsticker/mobiles/"),
        ("security.html", URL + "security/"),
        ("entertainment.html", URL + "newsticker/entertainment/"),
        ("netzpolitik.html", URL + "newsticker/netzpolitik/"),
        ("wirtschaft.html", URL + "newsticker/wirtschaft/"),
        ("journal.html", URL + "newsticker/journal/"),
        ("newsticker.html", URL + "newsticker/"),
        ("plus.html", URL + "plus/"),

        ("impressum.html", URL + "impressum.html"),
        ("datenschutz.html", URL + "Datenschutzerklaerung-der-Heise-Medien-GmbH-Co-KG-4860.html"),
    ]
