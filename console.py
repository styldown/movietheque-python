import os
import pprint

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def menu_film():
    while (True):
        clearConsole()
        print("********* Menu film **********")
        print("     1 :Ajouter un film")
        print("     2 :Supprimer un film")
        print("     3 :Liste des film")
        print("     4 :Quiter menu film")
        choix=input("Entrez votre choix : ")
        if choix not in ("1","2","3","4"):
            print("!!!!!!!!! Choix invalid !!!!!!!!!")
            input("appuyer sur entrer pour continuer")
            continue
        else :   
            return choix
        
def menu_clients():
    while (True):
        clearConsole()
        print("********* Menu clients **********")
        print("     1 :Ajouter un client")
        print("     2 :Chercher un client")
        print("     3 :Operations des clients")
        print("     4 :Quiter menu clients")
        choix=input("Entrez votre choix : ")
        if choix not in ("1","2","3","4"):
            print("!!!!!!!!! Choix invalid !!!!!!!!!")
            input("appuyer sur entrer pour continuer")
            continue
        else :   
            return choix
    
def menu_principale():
    while (True):
        clearConsole()
        print("********* Menu principale **********")
        print("     1 :Menu films")
        print("     2 :Menu clients")
        print("     3 :Quiter")
        choix=input("Entrez votre choix : ")
        if choix not in ("1","2","3"):
            print("!!!!!!!!! Choix invalid !!!!!!!!!")
            input("appuyer sur entrer pour continuer")
            continue
        else :
           return choix
       
def ajout_film():
    clearConsole()
    print("****** Ajouter un film*****")
    titre=input("Entrez le titre du film : ")
    realisateur=input("Entrez le nom du realisateur : ")
    return {"titre":titre,"realisateur":realisateur}

def affiche_liste_film(liste):
    clearConsole()
    print("****** Liste des films ******")
    print("ID , Titre , Realisateur , ID du détenteur")
    print("******************************************")
    liste.sort(key = lambda x: x[1])
    pprint.pprint(liste)
    input("Appuyez sur entrer pour quiter la liste")
    
def supprime_film():
    clearConsole()
    print("***** Supprimer film *****")
    id_film=input("Entrez l'ID du film a supprimer")
    return id_film
    
def affiche_liste_clients(liste):
    clearConsole()
    print("****** Liste des clients ******")
    print("******************************************")
    print("ID , Prenom , Nom , Adresse")
    pprint.pprint(liste)
    input("Appuyez sur entrer pour quiter la liste")

def ajout_client():
    clearConsole()
    print("****** Ajouter un client*****")
    nom=input("Entrez le nom : ")
    prenom=input("Entrez le prenom : ")
    adresse=input("Entrez l'adresse : ")
    return {"nom":nom,"prenom":prenom,"adresse":adresse} 

def recherche_client():
    clearConsole()  
    print("****** Chercher un client*****")
    nom=input("entrez le nom du client : ")
    return nom
           
def operation_client(client):
    while (True):
        clearConsole()
        print("*********" + client +"**********")
        print("     1 :Louer film")
        print("     2 :Remettre film")
        print("     3 :Liste des film loués")
        print("     4 :Changer adresse")
        print("     5 :Quiter menu operation")
        choix=input("Entrez votre choix : ")
        if choix not in ("1","2","3","4","5"):
            print("!!!!!!!!! Choix invalid !!!!!!!!!")
            input("appuyer sur entrer pour continuer")
            continue
        else :   
            return choix 
        
def initialisation_client():
    clearConsole()
    var=input("Entrez l'ID du client : ")
    return var 

def louer_film():
    clearConsole()
    var=input("Entrez l'ID du film a louer : ")
    return var

def remettre_film():
    clearConsole()
    var=input("Entrez l'ID du film a remettre : ")
    return var

def changer_adresse():
    clearConsole()
    var=input("Entrez une nouvelle adresse : ")
    return var

    
    
       