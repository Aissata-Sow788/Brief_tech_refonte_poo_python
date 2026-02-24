from Document import Document

class Livre(Document):
    def __init__(self, titre, auteur, date_publication, genre, disponible=True):
        super().__init__(titre, auteur, date_publication, disponible)
        self.genre = genre
     

    def Emprunt(self):
        if not self.disponible:
            print("le livre est deja emprunter")
            return False
        else:
            self.disponible=False
            return True
            

    def Retour(self):
        if not self.disponible:
            self.disponible = True
            return True
        else:
            print("Le livre est déjà disponible")
            return False
        
       

        
    def __str__(self):
        if self.disponible == True:
            dispo = "Disponible"
        else:
            dispo = "Emprunté"
            
        return f"Livre: {self.titre} - Auteur: {self.auteur} - Genre : {self.genre} - Statut:[{dispo}]"

       
