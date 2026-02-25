from Bibliothecaire import Bibliothecaire
from datetime import datetime
from Livre import Livre
from Magazine import Magazine
from Adherent import Adherant

class Menu:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()

    def executer(self):

        while True:
            print("\n", "-" * 10, "BIBLIOTHEQUE", "-" * 10)
            print("1: Ajouter livres\n" \
            "2: Ajouter magazine\n"\
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
                                                
                        type = input("type : ").strip().lower()
                        if not type.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("type doit etre une chaine de caractere")
                        
                        self.bibliotheque.ajouter_document(Livre(titre, auteur,date_publication, genre, type))
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
                        
                        genre = input("genre : ")
                           
                        type = input("type : ").strip().lower()
                        if not type.replace(" ", "").replace("'", "").isalpha():
                            raise ValueError("type doit etre une chaine de caractere")
                        
                        self.bibliotheque.ajouter_document(Magazine(titre, auteur,date_publication, genre, type))
                    except ValueError as e:
                        print("ERREUR: ",e)
                    
                case "3":
                    self.bibliotheque.Lister_document()

                case '4':
                    try:
                        prenom = input("prenom : ").strip()
                        if not prenom.replace(" ", "").isalpha():
                            raise ValueError('prenom invalide')
                        
                        nom = input("Nom : ").strip()
                        if not nom.replace(" ", "").isalpha():
                            raise ValueError('NOm invalide')
                        self.bibliotheque.InscrireMembre(Adherant(nom, prenom))
                    except ValueError as e:
                        print("Erreur : ", e)

                case '5':
                    self.bibliotheque.Lister_membres()
                
                case '6':
                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        
                        id_adherent=input("id_adherent: ").strip()

                        if not id_adherent.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                    except ValueError as e:
                        print("Erreur : ", e)

                    print('------------------Liste des documents-------------------')
                    self.bibliotheque.Lister_document()
                    try:
                        id_document=input("id_document: ").strip()

                        if not id_document.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                        
                        date_str = input("Entrer la date  prevu (YYYY-MM-DD) : ").strip()
                        try:
                            date_prevu = datetime.strptime(date_str, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                        
                        self.bibliotheque.valider_pret(int(id_adherent), int(id_document), date_prevu)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '7':
                    print('----------------Liste des adherants--------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        id_adherent=input("id_adherent: ").strip()

                        if not id_adherent.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                        
                        self.bibliotheque.Lister_Emprunt(int(id_adherent))
                    except ValueError as e:
                        print("Erreur : ", e)
                
                case '8':

                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        
                        id_adherent=input("id_adherent: ").strip()

                        if not id_adherent.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                    except ValueError as e:
                        print("Erreur : ", e)

                    print('------------------Liste des documents-------------------')
                    self.bibliotheque.Lister_document()
                    try:
                        id_document=input("id_document: ").strip()

                        if not id_document.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                        
                        date_str = input("Entrer la date  prevu (YYYY-MM-DD) : ").strip()
                        try:
                            date_prevu = datetime.strptime(date_str, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                        
                        
                        self.bibliotheque.Retourner_document(int(id_document), int(id_adherent), date_prevu)
                    except ValueError as e:
                        print("Erreur : ", e)
             
                        
                case '0':
                    print("BYE")
                    break  

                case _:
                    print("choix invalide")