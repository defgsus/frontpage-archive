from pathlib import Path
from typing import List

import tabulate

from .giterator import Giterator
from .scraper import Scraper


PROJECT_PATH: Path = Path(__file__).resolve().parent.parent


def summary(scrapers: List[Scraper]):
    scrapers = sorted(scrapers, key=lambda s: s.ID)

    git = Giterator(PROJECT_PATH)

    rows = []
    for scraper in scrapers:
        commit = git.first_commit(scraper.path())
        if commit:
            rows.append({
                "id": f"[{scraper.ID}](docs/snapshots/{scraper.ID})",
                "since": commit.committer_date.date().isoformat(),
                "files": len(list(scraper.path().glob("*.html"))) - 1,
                "url": scraper.URL,
            })
        continue

        first_date = None
        num_commits = 0
        num_changes = 0
        filename_set = set()
        for commit in git.iter_commits(scraper.path()):
            if first_date is None:
                first_date = commit.committer_date
            num_commits += 1
            for ch in commit.changes:
                filename_set.add(ch["name"])
                try:
                    num_changes += int(ch["addtions"])
                except:
                    pass

        if first_date:
            rows.append({
                "url": scraper.URL,
                "files": len(filename_set) - 1,
                "commits": num_commits,
                "changes": num_changes,
            })

    return tabulate.tabulate(
        rows,
        tablefmt="pipe",
        headers="keys",
    )
