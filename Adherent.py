class Adherant:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom=prenom
        self.listeEmprunts = []  

    def __str__(self):
        
        return f"Adherent: {self.prenom} {self.nom}"   