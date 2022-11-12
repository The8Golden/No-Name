import os
from os import system


def titlebar(title) -> None:
    system("title " + title)


def clear() -> None:
    os.system("clear")
