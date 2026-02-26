class Utilisateur:
    def __init__(self, nom, prenom, email, mdp):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mdp = mdp

    def __str__(self):
        return f"prenom : {self.prenom}, nom : {self.nom}, email : {self.email}"
    
    