from Bibliothecaire import Bibliothecaire
from datetime import datetime

class Menu:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()

    def executer(self):

        while True:
            print("\n", "-" * 10, "BIBLIOTHEQUE", "-" * 10)
            print("1: Ajouter livre \n" \
            "2: Ajouter Magazine \n"\
            "3: Afficher documents \n" \
            "4: Inscrire membres \n" \
            "5: Afficher membres \n" \
            "6: Valider pret \n" \
            "7: Afficher les emprunts d'un adherant \n" \
            "8: Retourner un document\n"
            "0: Quitter")

            choix = input("\nEntrez votre choix : ")
            
            match choix:
                case "1":
                    try:
                        titre = input("titre : ").strip().lower()
                        if not titre.replace(" ","").replace("'", "").isalpha():
                            raise ValueError("le titre doit etre une chaine caractere ")
                        
                        auteur = input("auteur : ").strip().lower()
                        if not auteur.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("l'auteur doit etre une chaine de caractere")
                        
                        date_str = input("Entrer la date (YYYY-MM-DD) : ").strip()
                        
                        try:
                            date_publication = datetime.strptime(date_str, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                        
                        genre = input("genre : ").strip().lower()
                        if not genre.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("Genre doit etre une chaine de caractere")
                        
                        self.bibliotheque.ajouter_livre(titre, auteur,date_publication, genre)
                    except ValueError as e:
                        print("ERREUR: ",e)
                case "2": 
                    try:
                        titre = input("titre : ").strip().lower()
                        if not titre.replace(" ","").replace("'", "").isalpha():
                            raise ValueError("le titre doit etre une chaine caractere ")
                        
                        auteur = input("auteur : ").strip().lower()
                        if not auteur.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("l'auteur doit etre une chaine de caractere")
                        

                        date_str = input("Entrer la date (YYYY-MM-DD) : ").strip()
                        
                        try:
                            date_publication = datetime.strptime(date_str, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                        
                        periodiciter = input("periodiciter : ").strip().lower()
                        if not periodiciter.replace(" ", "").replace("'", "").isalnum():
                            raise ValueError("periodiciter doit etre une chaine de caractere")
                        
                        self.bibliotheque.ajouter_magazine(titre, auteur, date_publication, periodiciter)
                    except ValueError as e:
                        print("ERREUR: ",e)
                    
                case "3":
                    self.bibliotheque.Lister_document()

                case '4':
                    try:
                        nom = input("Nom : ").strip()
                        if not nom.replace(" ", "").isalpha():
                            raise ValueError('NOm invalide')
                        self.bibliotheque.InscrireMembre(nom)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '5':
                    self.bibliotheque.Lister_membres()
                
                case '6':
                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        
                        nom_membre=input("Nom: ").strip().lower()

                        if not nom_membre.replace(" ", "").isalpha():

                            raise ValueError("le nnom doit etre une chaine de caractere")
                    except ValueError as e:
                        print("Erreur : ", e)
                    
                    self.bibliotheque.Lister_document()
                    try:
                        titre_livre=input("Titre: ").strip().lower()
                        if not titre_livre.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("le titre doit etre une chaine de cractere")
                        
                        self.bibliotheque.valider_pret(nom_membre,titre_livre)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '7':
                    print('----------------Liste des adherants--------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        nom=input('Nom: ').strip()
                        if not nom.replace(" ", "").isalpha():
                            raise ValueError("le nom doit etre une chaine de caractere")
                        self.bibliotheque.Lister_Emprunt(nom)
                    except ValueError as e:
                        print("Erreur : ", e)
                
                case '8':

                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        
                        nom_membre=input("Nom: ").strip().lower()

                        if not nom_membre.replace(" ", "").isalpha():

                            raise ValueError("le nnom doit etre une chaine de caractere")
                    except ValueError as e:
                        print("Erreur : ", e)

                    print('------------------Liste des livres-------------------')
                    self.bibliotheque.Lister_document()
                    try:
                        titre_livre=input("Titre: ").strip().lower()
                        if not titre_livre.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("le titre doit etre une chaine de cractere")
                        
                        self.bibliotheque.Retourner_document(nom_membre,titre_livre)
                    except ValueError as e:
                        print("Erreur : ", e)
             
                        
                case '0':
                    print("BYE")
                    break  

                case _:
                    print("choix invalide")