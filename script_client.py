import sqlite3
import client
import console
import script_film

def gestion_client():
    while(True):
        choix_utilisateur=console.menu_clients()
        match choix_utilisateur:
            case "1" : 
                client=console.ajout_client()
                ajout_client(client)
            case "2" : 
                nom=console.recherche_client()
                chercher_client(nom)
            case "3" : operation_client()
            case "4" : break

def liste_film_client(id):
    connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
    curseur = connexion.cursor()
    sql="SELECT * FROM films WHERE DETENTEUR = ? "
    curseur.execute(sql, (id,))
    liste = curseur.fetchall()
    console.affiche_liste_clients(liste)
    connexion.close()
    
def ajout_client(c):
    new_client=client.client(c["nom"], c["prenom"],c["adresse"])
    new_client.enregistrer_client()

def chercher_client(n):
    connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
    curseur = connexion.cursor()
    sql="SELECT * FROM clients WHERE nom = ? or prenom =?"
    curseur.execute(sql, (n,n,))
    liste = curseur.fetchall()
    console.affiche_liste_clients(liste)
    connexion.close()

def operation_client():
    id_client=console.initialisation_client()
    connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
    curseur = connexion.cursor()
    sql="SELECT * FROM clients WHERE id_client   = ? "
    curseur.execute(sql, (id_client,))
    liste = curseur.fetchone()
    cl= client.Client(liste[1],liste[2],liste[3],liste[0])
    connexion.close()
    while(True):
        operation=console.operation_client((cl.get_nom() +" "+cl.get_prenom()))
        match operation:
            case "1" : 
                film=console.louer_film()
                cl.louer_film(film)
            case "2" : 
                film=console.remettre_film()
                cl.remettre_film(film)
            case "3" : 
                cl.list_film()
            case "4" : 
                adresse=console.changer_adresse()
                cl.changer_adresse(adresse) 
            case "5" : return
    
    

    