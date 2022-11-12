def commande(command):
    try :
        command = int(command)
    except :
        print("erreur")
    if command == 1 :
        Zmap()