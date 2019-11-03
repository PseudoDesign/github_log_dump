"""
Dump github PR data to a dictionary
"""
from github.Repository import Repository
import progressbar


def pr_dump(
        repository: Repository,
        progress_bar: bool = False,) -> dict:

    if progress_bar:
        bar = progressbar.ProgressBar(maxval=44, widgets=[progressbar.Percentage(), progressbar.Bar()]).start()
    else:
        bar = None

    if bar:
        bar.finish()


def cmdline():
    pass
