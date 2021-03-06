import re
import os
import sys
import glob
import json
import datetime
import traceback
import urllib.parse
from pathlib import Path
from typing import Generator, Tuple, Union, Optional, List

import requests
import bs4

scraper_classes = dict()


class Scraper:

    ID: str = None      # must be filename compatible
    NAME: str = None    # leave None to copy ID
    URL: str = None

    # base implementation of iter_files() yields these urls
    #   defaults to [("index.html", URL)]
    SUB_URLS: List[Tuple[str, str]] = []

    # add names of links to follow on the first SUB_URLS page, like "Impressum"
    SUB_LINK_NAMES = []

    # set to True in abstract classes
    ABSTRACT: bool = False

    # request timeout in seconds
    REQUEST_TIMEOUT: float = 10
    # Set to false to run every request in individual session
    USE_SESSION: bool = True

    BASE_PATH: Path = Path(__file__).resolve().parent.parent / "docs" / "snapshots"

    def __init_subclass__(cls, **kwargs):
        if not cls.ABSTRACT:

            if cls.NAME is None:
                cls.NAME = cls.ID

            for required_key in ("ID", "NAME", "URL"):
                assert getattr(cls, required_key), f"Define {cls.__name__}.{required_key}"

            if not cls.SUB_URLS:
                cls.SUB_URLS = [("index.html", cls.URL)]

            if cls.ID in scraper_classes:
                raise AssertionError(f"Duplicate name '{cls.ID}' for class {cls.__name__}")

            scraper_classes[cls.ID] = cls

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "github.com/defgsus/frontpage-archive"
        }
        self.status = dict()

    @classmethod
    def path(cls) -> Path:
        return cls.BASE_PATH / cls.ID

    def iter_files(self) -> Generator[Tuple[str, str], None, None]:
        """
        Yield tuples of (filename, text-content)

        The base method yields all filenames and web responses from self.SUB_URLS
        """
        first_page = None
        for filename, url in self.SUB_URLS:

            try:
                content = self.request(url, filename=filename).text

                if first_page is None:
                    first_page = content

                yield filename, content
            except:
                self.log(traceback.format_exc())
                pass

        if first_page is not None:
            yield from self.iter_sub_link_files(first_page)

    def iter_sub_link_files(self, markup: str) -> Generator[Tuple[str, str], None, None]:
        """
        Iterates through self.SUB_LINK_NAMES and yields all response of links
        whose text matches one of the names.

        :param markup: str of html
        """
        requested_urls = set()
        filename_counter = dict()

        soup = self.to_soup(markup)
        for a in soup.find_all("a"):
            if not a.text:
                continue

            link_name = a.text.strip()
            if a.get("href") and link_name in self.SUB_LINK_NAMES:

                url = urllib.parse.urljoin(self.URL, a["href"])
                if url in requested_urls:
                    continue
                requested_urls.add(url)

                filename = "".join(c for c in link_name.lower() if "a" <= c <= "z")
                filename_counter[filename] = filename_counter.get(filename, 0) + 1

                if filename_counter[filename] > 1:
                    filename = f"{filename}{filename_counter[filename]}"

                try:
                    response = self.request(url, filename=filename)
                except:
                    self.log(traceback.format_exc())
                    continue

                yield filename + ".html", response.text

    def download(self) -> dict:
        """
        Download all files via `iter_files` and store to disk.

        Returns a small report dict
        """
        self.status = dict()

        report = {
            "files": 0,
        }
        try:
            for short_filename, content in self.iter_files():

                filename = self.path() / short_filename
                os.makedirs(str(filename.parent), exist_ok=True)

                self.log("storing", filename)
                filename.write_text(content)
                report["files"] += 1
        except:
            report["exception"] = traceback.format_exc(limit=-2)

        (self.path() / "status.json").write_text(
            json.dumps(self.status, indent=2, sort_keys=True, ensure_ascii=False)
        )
        report["request_exceptions"] = sum([1 for s in self.status.values() if s.get("exception")])
        return report

    def log(self, *args):
        if self.verbose:
            print(f"{self.__class__.__name__}:", *args, file=sys.stderr)

    def request(
            self,
            url: str,
            method: str = "GET",
            filename: Optional[str] = None,
            **kwargs,
    ) -> requests.Response:
        """
        Do a HTTP request
        :param url: str, full url
        :param method: str, defaults to "GET"
        :param filename: optional str, The key in the `status.json` file, defaults to url
        :param kwargs: any additional requests.request() arguments
        :return: requests.Response instance
        """
        kwargs.setdefault("timeout", self.REQUEST_TIMEOUT)
        self.log("requesting", url)

        status_key = filename or url

        self.status[status_key] = status = {
            "date": datetime.datetime.utcnow().isoformat(),
            "url": url,
        }
        try:
            if self.USE_SESSION:
                response = self.session.request(method=method, url=url, **kwargs)
            else:
                response = requests.request(method=method, url=url, **kwargs)
            self.log(response.status_code, f"{len(response.content):,}")

            status.update({
                "status": response.status_code,
                "headers": dict(response.headers),
            })
            return response
        except Exception as e:
            status.update({
                "exception": f"{e.__class__.__name__}: {e}"
            })
            raise

    @classmethod
    def to_soup(cls, html: str) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(html, features="html.parser")

    @classmethod
    def strip(cls, x: Optional[Union[str, bs4.Tag]]) -> Optional[str]:
        if x is None:
            return None
        elif isinstance(x, str):
            text = x
        elif isinstance(x, bs4.Tag):
            text = x.text
        else:
            raise TypeError(f"Can not strip type {type(x).__name__} ({x})")

        if text is None:
            return None

        text = text.strip().replace("\n", " ").replace("\t", " ")
        return _RE_MULTI_SPACE.sub(" ", text)

    @classmethod
    def create_article_dict(
            cls,
            title: Optional[str] = None,
            teaser: Optional[str] = None,
            url: Optional[str] = None,
            image_url: Optional[str] = None,
            image_title: Optional[str] = None,
    ) -> dict:
        return {
            "title": title,
            "teaser": teaser,
            "url": url,
            "image_url": image_url,
            "image_title": image_title,
        }

    def iter_articles(self, filename: str, content: str) -> Generator[dict, None, None]:
        """
        Override this to extract article data from each scraped file.

        Base implementation looks for common <article> tag structures
        """
        soup = self.to_soup(content)
        for tag in soup.find_all("article"):
            if not (tag.text and tag.text.strip()):
                continue

            headline = tag.find("h3")
            if not headline:
                continue

            article = self.create_article_dict(
                title=self.strip(headline),
                teaser=self.strip(tag.find("p")),
            )

            a = tag.find("a")
            if a and a.get("href"):
                article["url"] = a["href"]

            image = tag.find("img")
            if image and image.get("src"):
                article["image_url"] = image["src"]
                if image.get("alt"):
                    article["image_title"] = self.strip(image["alt"])

            yield article


_RE_MULTI_SPACE = re.compile(r"\s+")
