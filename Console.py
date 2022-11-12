from colorama import Fore
import Commande
from Utils.Gui_Designer import titlebar, clear


class Console:
    def __init__(self):
        titlebar("Main Page")
        command = open("command.txt", "r", encoding="utf-8")
        logo = open("GUI/LOGO.txt", "r", encoding="utf-8")
        print(logo.read() + " \n" + command.read())
        user_command = input("Merci de rentrer un nombre : ")
        Commande.commande(user_command)

Console()

