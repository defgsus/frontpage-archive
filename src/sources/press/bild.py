import urllib.parse
from typing import Generator, Tuple

from ...scraper import Scraper


class Bild(Scraper):
    ID = "bild.de"
    URL = "https://www.bild.de"

    SUB_LINK_NAMES = [
        "News",
        "Politik",
        "Regio",
        "Unterhaltung",
        "Sport",
        "Fussball",
        "Lifestyle",
        "Ratgeber",
        "Auto",
        "Digital",
        "Inland",
        "Ausland",
        "Mystery",
        "Ein Herz für Kinder",
        "Kommentare und Kolumnen",
        "Stars",
        "Erotik",
        "Kino",
        "TV",
        "Reise",
        "Gesundheit",
        "Geld & Wirtschaft",
        "Wirtschaft",
        "Impressum",
        "Datenschutz",
    ]

    def iter_articles(self, filename: str, content: str) -> Generator[dict, None, None]:
        soup = self.to_soup(content)
        for tag in soup.find_all("article"):
            if not (tag.text and tag.text.strip()):
                continue

            headline = tag.find("h3")
            if not headline:
                continue

            article = {
                "title": self.strip(headline),
                "teaser": self.strip(tag.find("p")),
                "url": None,
                "image_url": None,
                "image_title": None,
            }

            a = tag.find("a")
            if a and a.get("href"):
                article["url"] = urllib.parse.urljoin(self.URL, a["href"])

            image = tag.find("img")
            if image and image.get("src"):
                article["image_url"] = image["src"]
                if image.get("alt"):
                    article["image_title"] = self.strip(image["alt"])

            yield article
