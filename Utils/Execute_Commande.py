import os

import requests
from os import system
from Utils.Gui_Designer import clear, erreur_base
from Utils.FILE import file_exist
from colorama import Fore

def zmap():
    logo = open("./GUI/ZMAP.txt", "r", encoding="utf-8")
    print(logo.read())

    port = input("Pour quel port voulez vous générer : ")
    clear()
    count = input("Combien voulez vous en générer ? (défaut = 100 ) : ")
    clear()
    filename = input("Comment voulez vous nommé le fichier de sorti ? (défaut = Zmap_Output): ")

    print(count + " " + port + " " +filename)
    system(f"zmap -p {port} -n  {count} -o {filename}.csv")


def help_command(number):
    match number :
        case 1 :
            print("Permet de générer une liste d'ip dans un .csv avec un port spécifique.")
        case 2 :
            print("Donne des informations sur une ip donné")
        case 3 :
            print("Fermer l'application ...")

def ip():
    ip = input( Fore.RED +"Merci d'entrer l'ip que vous voulez regarder :" + Fore.RESET)
    info = requests.get( f"http://ip-api.com/json/{ip}").json()

    #print(info)                   #debug for dev

    with open(f"{os.getcwd()}/out/ip_info/{ip}.txt", "w", encoding="utf-8" ) as files :
        try :
            files.write(f"""
ip = {str(info["query"])}
Pays = {str(info["country"])}
countryCode {str(info["countryCode"])}
Region = {str(info["regionName"])}
Ville = {str(info["city"])}
Zone de Temp = {str(info["timezone"])}
isp = {str(info["isp"])}
org = {str(info["org"])}
as = {str(info["as"])}
             """)
        except Exception:
            clear()
            erreur_base(f"Erreur pour écrire le fichier le fichier {ip}.txt ")
        else:
            return f"Le fichier a bien était créer ! {Fore.YELLOW + os.getcwd()}out\\{ip}.txt{Fore.RESET}"

