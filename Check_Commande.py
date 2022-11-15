import Utils.Execute_Commande

def commande(command):

    try :
        command = int(command)
    except :
        print("erreur")
    if command == 1:
        Utils.Execute_Commande.zmap()
    elif command == 2 :
         print(ip())