from ...scraper import Scraper


class WebDE(Scraper):
    ID = "web.de"
    URL = "https://web.de"
    SUB_URLS = [
        ("index.html", URL),
        ("news.html", URL + "/magazine/"),
        ("politik.html", URL + "/magazine/politik/"),
        ("panorama.html", URL + "/magazine/panorama/"),
        ("sport.html", URL + "/magazine/sport/"),
        ("unterhaltung.html", URL + "/magazine/unterhaltung/"),
        ("bestenliste.html", URL + "/magazine/bestenliste/"),
        ("ratgeber.html", URL + "/magazine/ratgeber/"),
        ("wissen.html", URL + "/magazine/wissen/"),
        ("gesundheit.html", URL + "/magazine/gesundheit/"),
        ("kolumnen.html", URL + "/magazine/kolumnen/"),
        ("infografiken.html", URL + "/magazine/infografiken/"),
        ("service.html", URL + "/magazine/services/"),
        ("corona.html", URL + "/magazine/news/coronavirus/"),

        ("impressum.html", URL + "/impressum/"),
        ("datenschutz.html", URL + "/datenschutz/"),
    ]
