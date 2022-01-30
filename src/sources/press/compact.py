from typing import Generator
from ...scraper import Scraper


class Compact(Scraper):
    ID = "compact-online.de"
    URL = "https://www.compact-online.de/"
    SUB_URLS = [
        ("index.html", URL),

        ("plus.html", URL + "plus/"),
        ("aktuell.html", URL + "compact-aktuell/"),
        ("tv.html", "https://tv.compact-online.de/"),

        ("impressum.html", URL + "rechtliches/impressum/"),
        ("datenschutz.html", URL + "rechtliches/datenschutz/"),
    ]

    def iter_articles(self, filename: str, content: str) -> Generator[dict, None, None]:
        soup = self.to_soup(content)
        for tag in soup.find_all("div", {"class": "content"}):
            if not (tag.text and tag.text.strip()):
                continue

            article = self.create_article_dict(
                title=self.strip(tag.find("div", {"class": "post-meta"})),
                teaser=self.strip(tag.find("div", {"class": "excerpt"}))
            )

            yield article
            