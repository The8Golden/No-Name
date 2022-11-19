import Utils.Execute_Commande
from Utils.Execute_Commande import clear
def commande(command):

    try :
        command = int(command)
    except :
        print("erreur")
    if command == 1:
        Utils.Execute_Commande.zmap()
    elif command == 2 :

        check = Utils.Execute_Commande.ip()
        if check != None :
            print(check)
