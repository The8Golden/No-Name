from colorama import Fore
import Commande
from Utils import Gui_Designer




class Console:
    def __init__(self):
        Gui_Designer.titlebar("Main Page")
        print(f"Bienvenue merci de choisir une commande ! \n {Fore.GREEN} Appuyer sur entrer pour continuer... {Fore.RESET}")
        input()
        command = open("command.txt", "r", encoding="utf-8")
        Logo = open("GUI/LOGO.txt", "r", encoding="utf-8")
        print(Logo.read() + " \n" + command.read())
        user_command = input("Merci de rentrer un nombre : ")
        Commande.commande(user_command)

Console()