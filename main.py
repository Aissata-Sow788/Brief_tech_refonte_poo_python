from Menu import Menu
import bcrypt
from utilisateur import Utilisateur


# from bd import get_connection

# # conn=get_connection()

# # if conn.is_connected():
# #     print("connection reussi")

menu = Menu()

def auth():
    while True:
        print("1: Inscription utilisateur \n" \
                "2: Se connecter \n")
        
        choix = input("entrez votre choix :")

        
        match choix:
            case "1":
                nom = input("nom :")
                prenom = input("prenom :")
                email = input("email :")
                mdp = input("mot de passe :")
                mdp_byte = mdp.encode("utf-8")
                mdp_hasher = bcrypt.hashpw(mdp_byte, bcrypt.gensalt())
                
                utilisateur = Utilisateur(nom, prenom, email, mdp_hasher)
                menu.bibliotheque.inscription(utilisateur)
                return
            case "2":

                email = input("email :")
                mdp = input("mot de passe :")
                if menu.bibliotheque.se_connecter(email, mdp):
                    menu.executer()
                else:
                    print("Email ou mot de passe invalide")

            case _:
                print("choix invalide")


auth()






                    
    






























