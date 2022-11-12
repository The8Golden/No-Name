from Check_Commande import commande
from Utils.Gui_Designer import titlebar, clear
from time import sleep
from colorama import Fore


def Console():
    titlebar("Main Page")
    while True :
        command = open("command.txt", "r", encoding="utf-8")
        logo = open("GUI/LOGO.txt", "r", encoding="utf-8")

        print(logo.read() + " \n" + command.read())

        user_command = input("Merci de d'entrer un nombre : ")

        clear()
        commande(user_command)

        input(f"{Fore.GREEN}\n\n\nAppuyer sur Entrer pour continuer... {Fore.RESET}")
        clear()



Console()