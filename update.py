import argparse
import datetime
import traceback
from multiprocessing.pool import ThreadPool
from typing import List

import src.sources  # register classes
from src.scraper import Scraper, scraper_classes
from src.summary import summary, PROJECT_PATH


def parse_args() -> dict:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f", "--filter", type=str, nargs="*",
        help="One or more scraper names to limit the download"
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, nargs="?", default=False, const=True,
        help="Print a lot of stuff"
    )
    parser.add_argument(
        "-j", "--threads", type=int, default=1,
        help="Number of parallel threads (per scraper)"
    )
    parser.add_argument(
        "-u", "--update-readme", type=bool, nargs="?", default=False, const=True,
        help="Update README with statistics"
    )

    return vars(parser.parse_args())


def scrape(scraper: Scraper) -> str:
    """
    Run the scraper, return result message text
    """
    msg = f"### {scraper.ID}\n\n"

    try:
        report = scraper.download()

        for key, value in report.items():
            if value:
                msg += f"- {value} {key}\n"

    except Exception as e:
        msg += f"```\n{traceback.format_exc(limit=-2)}```\n"

    return msg


def main(filter: List[str], verbose: bool, threads: int, update_readme: bool):

    filtered_classes = []
    for name in sorted(scraper_classes.keys()):
        if not filter or name in filter:
            filtered_classes.append(scraper_classes[name])

    print(f"update @ {datetime.datetime.utcnow().replace(microsecond=0)} UTC\n")

    scrapers = [
        scraper_class(verbose=verbose)
        for scraper_class in filtered_classes
    ]

    messages = ThreadPool(threads).map(scrape, scrapers)
    messages.sort()

    print("\n".join(messages))

    if update_readme:
        readme_template = (PROJECT_PATH / "templates" / "README.md").read_text()
        readme_template %= {
            "table": summary(list(scraper_classes.values()))
        }
        (PROJECT_PATH / "README.md").write_text(readme_template)


if __name__ == "__main__":
    main(**parse_args())
