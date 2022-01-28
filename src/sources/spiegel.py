from typing import Dict, Generator, Tuple, Union, Optional

import bs4

from ..scraper import Scraper


class Spiegel(Scraper):

    ID = "spiegel.de"
    NAME = "spiegel.de"
    URL = "https://www.spiegel.de/"

    def iter_files(self) -> Generator[Tuple[str, str], None, None]:
        response = self.request(self.URL)
        yield "index.html", response.text
