from ..scraper import Scraper


class Zeit(Scraper):
    ID = "zeit.de"
    URL = "https://www.zeit.de/"
    USE_SESSION = False
    SUB_URLS = [
        ("index.html", URL + "index"),

        ("politik.html", URL + "politik/index"),
        ("gesellschaft.html", URL + "gesellschaft/index"),
        ("wirtschaft.html", URL + "wirtschaft/index"),
        ("kultur.html", URL + "kultur/index"),
        ("wissen.html", URL + "wissen/index"),
        ("gesundheit.html", URL + "gesundheit/index"),
        ("digital.html", URL + "digital/index"),
        ("campus.html", URL + "campus/index"),
        ("sinn.html", URL + "sinn/index"),
        ("arbeit.html", URL + "arbeit/index"),
        ("sport.html", URL + "sport/index"),
        ("zeit-magazin.html", URL + "zeit-magazin/index"),
        ("news.html", URL + "news/index"),
        ("christ-und-welt.html", URL + "christ-und-welt"),

        ("impressum.html", URL + "impressum/index"),
    ]
    SUB_LINK_NAMES = [
        "Datenschutz",
    ]


class ZeitSchule(Scraper):
    ID = "zeitfuerdieschule.de"
    URL = "https://www.zeitfuerdieschule.de"
    SUB_URLS = [
        ("index.html", URL),
        ("werte.html", URL + "/themen/werte/"),
        ("demokratie.html", URL + "/themen/demokratie/"),
        ("deutschland.html", URL + "/themen/deutschland/"),

        ("impressum.html", URL + "/impressum/"),
        ("datenschutz.html", "https://datenschutz.zeit.de/zeit-schule"),
    ]
