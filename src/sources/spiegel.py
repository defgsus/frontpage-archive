from typing import Dict, Generator, Tuple, Union, Optional

import bs4

from ..scraper import Scraper


class Spiegel(Scraper):
    ID = "spiegel.de"
    URL = "https://www.spiegel.de/"


class SpiegelDaily(Scraper):
    ID = "spiegeldaily.de"
    URL = "https://www.spiegeldaily.de/"

