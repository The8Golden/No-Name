import requests
from os import system
from Utils.Gui_Designer import clear
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
    print(str(info["country"]))
    print(info)

    if file_exist(f"out/{ip}.txt") :
       with open(f"{ip}.txt", "w") as files :
            files.write(f"""
            ip = {str(info["query"])}
            Pays = 
            
            
            
            
            
            """)
    else :
        with open(f"out/{ip}.txt", "x") as files:
            files.write(f"""
             ip = {str(info["query"])}
             Pays = 





             """)




