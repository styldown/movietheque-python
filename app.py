import script_film
import script_client
import console
import sqlite3


connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
curseur = connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON")
curseur.executescript('''
    CREATE TABLE IF NOT EXISTS clients(
    id_client INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom TEXT,
    prenom TEXT,
    adresse TEXT);
    CREATE TABLE IF NOT EXISTS films(
    id_film INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    titre TEXT,
    realisateur TEXT,
    detenteur INTEGER,
    FOREIGN KEY(detenteur) REFERENCES clients(id_client));
    ''')
connexion.commit()
connexion.close()
while(True):
    choix_utilisateur=console.menu_principale()
    match choix_utilisateur:
        case "1" : script_film.gestion_film()
        case "2" : script_client.gestion_client()
        case "3" : break
print("*****FIN DE PROGRAMME*****")
        
    