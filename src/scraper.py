import os
import sys
import glob
from pathlib import Path
from typing import Generator, Tuple, Union, Optional

import requests
import bs4

scraper_classes = dict()


class Scraper:

    ID: str = None      # must be filename compatible
    NAME: str = None    # leave None to copy ID
    URL: str = None

    # set to True in abstract classes
    ABSTRACT: bool = False

    # request timeout in seconds
    REQUEST_TIMEOUT: float = 10

    BASE_PATH: Path = Path(__file__).resolve().parent.parent / "docs" / "snapshots"

    def __init_subclass__(cls, **kwargs):
        if not cls.ABSTRACT:

            if cls.NAME is None:
                cls.NAME = cls.ID

            for required_key in ("ID", "NAME", "URL"):
                assert getattr(cls, required_key), f"Define {cls.__name__}.{required_key}"

            if cls.ID in scraper_classes:
                raise AssertionError(f"Duplicate name '{cls.ID}' for class {cls.__name__}")

            scraper_classes[cls.ID] = cls

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "github.com/defgsus/frontpage-archive"
        }

    @classmethod
    def path(cls) -> Path:
        return cls.BASE_PATH / cls.ID

    def iter_files(self) -> Generator[Tuple[str, str], None, None]:
        """
        Yield tuples of (filename, text-content)

        The base method simply yields "index.html" and the response from self.URL
        """
        response = self.request(self.URL)
        yield "index.html", response.text

    def download(self) -> dict:
        """
        Download all files via `iter_files` and store to disk.

        Returns a small report dict
        """
        report = {
            "files": 0,
        }
        for short_filename, content in self.iter_files():

            filename = self.path() / short_filename
            os.makedirs(str(filename.parent), exist_ok=True)

            self.log("storing", filename)
            filename.write_text(content)
            report["files"] += 1

        return report

    def log(self, *args):
        if self.verbose:
            print(f"{self.__class__.__name__}:", *args, file=sys.stderr)

    def request(self, url: str, method: str = "GET", **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self.REQUEST_TIMEOUT)
        self.log("requesting", url)
        return self.session.request(method=method, url=url, **kwargs)

    @classmethod
    def to_soup(cls, html) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(html, features="html.parser")
