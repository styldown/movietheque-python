from asyncio.windows_events import NULL
import sqlite3
import console

class Client:
    def __init__(self, nom, prenom, adresse, id=None):
        self.__prenom= prenom
        self.__nom= nom
        self.__adresse= adresse
        self.__id= id
        
    def get_id(self):
        return self.__id
        
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom    
        
    def enregistrer_client(self):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        c=( self.__nom, self.__prenom, self.__adresse )
        curseur.execute("INSERT INTO clients (nom, prenom ,adresse) VALUES (?, ?, ?)", c)
        connexion.commit()
        connexion.close()
    
    def modifier_adresse(self, adresse):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        sql = "UPDATE clients SET adresse = ? WHERE id = ?"
        curseur.execute(sql, (adresse,self.get_id()))
        connexion.commit()
        connexion.close()
    
    def louer_film(self, id_film):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        sql = "UPDATE films SET detenteur = ? WHERE id_film = ?"
        curseur.execute(sql, (self.get_id(),id_film))
        connexion.commit()
        connexion.close()
    
    def remettre_film(self, id_film):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        sql = "UPDATE films SET detenteur = NULL WHERE id_film = ?"
        curseur.execute(sql, (id_film))
        connexion.commit()
        connexion.close()
        
    def changer_adresse(self, adresse):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        sql = "UPDATE clients SET adresse = ? WHERE id_client = ?"
        curseur.execute(sql, (adresse,self.get_id()))
        connexion.commit()
        connexion.close()
        
    def list_film(self):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        sql = "SELECT * FROM films WHERE detenteur = ?"
        liste= curseur.execute(sql, (str(self.__id)))
        liste = curseur.fetchall()
        console.affiche_liste_film(liste)
        connexion.close()
    