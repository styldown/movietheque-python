import film
import console
import sqlite3

def gestion_film():
    while(True):
        choix_utilisateur=console.menu_film()
        match choix_utilisateur:
            case "1" : 
                film=console.ajout_film()
                ajout_film(film)
            case "2" : 
                id_film=console.supprime_film()
                supprime_film(id_film)
            case "3" : liste_film()
            case "4" : return
            
def ajout_film(f):
    new_film=film.Film(f["titre"], f["realisateur"])
    new_film.entregistrer_film()
    

def supprime_film(id):
    connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
    curseur = connexion.cursor()
    sql="DELETE FROM FILMS WHERE id_film =?"
    curseur.execute(sql,(id,))
    connexion.commit()
    connexion.close()

def liste_film():
    connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM FILMS")
    liste = curseur.fetchall()
    console.affiche_liste_film(liste)
    connexion.close()

    
