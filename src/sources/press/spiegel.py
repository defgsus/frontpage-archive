from ...scraper import Scraper


class Spiegel(Scraper):
    ID = "spiegel.de"
    URL = "https://www.spiegel.de/"
    SUB_URLS = [
        ("index.html", URL),
        ("schlagzeilen.html", URL + "schlagzeilen/"),
        ("plus.html", URL + "plus/"),
        ("coronavirus.html", URL + "thema/coronavirus/"),
        ("politik.html", URL + "politik/"),
        ("ausland.html", URL + "ausland/"),
        ("panorama.html", URL + "panorama/"),
        ("sport.html", URL + "sport/"),
        ("wirtschaft.html", URL + "wirtschaft/"),
        ("wissenschaft.html", URL + "wissenschaft/"),
        ("netzwelt.html", URL + "netzwelt/"),
        ("kultur.html", URL + "kultur/"),
        ("leben.html", URL + "thema/leben/"),
        ("karriere.html", URL + "karriere/"),
        ("geschichte.html", URL + "geschichte/"),
        ("auto.html", URL + "auto/"),
        ("tests.html", URL + "tests/"),
        ("deinspiegel.html", URL + "deinspiegel/"),
        ("audio.html", URL + "audio/"),
        ("video.html", URL + "video/"),
        ("impressum.html", URL + "impressum/"),
        ("datenschutz.html", URL + "datenschutz-spiegel"),
    ]


class SpiegelDaily(Scraper):
    ID = "spiegeldaily.de"
    URL = "https://www.spiegeldaily.de/"
    SUB_URLS = [
        ("index.html", URL),
        ("freizeit.html", URL + "category/freizeit/"),
        ("leben.html", URL + "category/leben/"),
        ("lebensstil.html", URL + "category/lebensstil/"),
        ("allgemeines.html", URL + "category/allgemeines/"),
        ("datenschutz.html", URL + "datenschutzerklaerung/"),
    ]
