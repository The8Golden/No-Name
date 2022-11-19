import os
from os import system
from colorama import Fore
import random

def titlebar(title) -> None:
    system("title " + title)


def clear() -> None:
    try :
        os.system("cls")
    except Exception :
        os.system("clear")

def erreur_base(text : str = "") -> str:
    print(Fore.RED)
    if text != "":
        print(text)
    print(f"Merci de reporter le probleme ci dessus sur le github https://github.com/The8Golden/No-Name ")

def random_color() :
    color = [Fore.BLACK, Fore.BLUE,Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW ]
    return random.choice(color)