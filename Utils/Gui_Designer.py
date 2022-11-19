import os
from os import system
from colorama import Fore

def titlebar(title) -> None:
    system("title " + title)


def clear() -> None:
    try :
        os.system("cls")
    except :
        os.system("clear")

def erreur_base(text : str = "") -> str:
    print(Fore.RED)
    if text != "":
        print(text)
    print(f"Merci de reporter le probleme ci dessus sur le github https://github.com/The8Golden/No-Name ")
