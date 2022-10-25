import sqlite3

class Film:
    def __init__(self, titre, realisateur,detenteur=None, id=None):
        self.__id=id
        self.__titre=titre
        self.__realisateur=realisateur
        self.__detenteur=detenteur
        
    def set_id(self, id):
        self.__id=id
        
    def get__id(self):
        return self.__id
        
    def get_titre(self):
        return self.__titre
    
    def get_realisateur(self):
        return(self.__realisateur)
    
    def set_detenteur(self, detenteur):
        self.__detenteur=detenteur
    
    def get_detenteur(self):
        return self.__detenteur
    
    def entregistrer_film(self):
        connexion = sqlite3.connect(r"movietheque\data\basededonnes.db")
        curseur = connexion.cursor()
        film=( self.__titre, self.__realisateur )
        curseur.execute("INSERT INTO films (titre, realisateur) VALUES (?, ?)", film)
        connexion.commit()
        connexion.close()
    
    def supprimer_film(self):
        pass
    

    