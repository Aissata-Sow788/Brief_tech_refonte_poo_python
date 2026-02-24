from Document import Document

class Magazine(Document):
    def __init__(self, titre, auteur, date_publication, periodiciter, disponible=True):
        super().__init__(titre, auteur, date_publication, disponible)
        self.periodiciter = periodiciter


    def Emprunt(self):
        if not self.disponible:
            print("le magazine est deja emprunter")
            return False
        else:
            self.disponible = False
            return True
            
    def Retour(self):
        if not self.disponible:
            self.disponible = True
            return True
        else:
            print("Le livre est déjà disponible")
            return False
        

    def __str__(self):
        # dispo = "Disponible" if self.disponible else "Emprunté"
        if self.disponible == True:
            dispo = "Disponible"
        else:
            dispo = "Emprunté"
            
        return f"Magazine: {self.titre} - Auteur: {self.auteur} - Genre : {self.periodiciter} - Statut:[{dispo}]"
    