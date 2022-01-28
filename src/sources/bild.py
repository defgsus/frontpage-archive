import urllib.parse
from typing import Generator, Tuple

from ..scraper import Scraper


class Bild(Scraper):
    ID = "bild.de"
    URL = "https://www.bild.de"

    LINK_NAMES = [
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
    def iter_files(self) -> Generator[Tuple[str, str], None, None]:
        index = self.request(self.URL).text
        yield "index.html", index

        requested_urls = set()
        filename_counter = dict()

        soup = self.to_soup(index)
        for a in soup.find_all("a"):
            if not a.text:
                continue

            link_name = a.text.strip()
            if a.get("href") and link_name in self.LINK_NAMES:

                url = urllib.parse.urljoin(self.URL, a["href"])
                if url in requested_urls:
                    continue
                requested_urls.add(url)

                try:
                    response = self.request(url)
                except:
                    continue

                filename = "".join(c for c in link_name.lower() if "a" <= c <= "z")
                filename_counter[filename] = filename_counter.get(filename, 0) + 1

                if filename_counter[filename] > 1:
                    filename = f"{filename}{filename_counter[filename]}"

                yield filename + ".html", response.text
