from Livre import Livre
from Magazine import Magazine
from Adherent import Adherant
from bd import get_connection
import bcrypt

class Bibliothecaire:
    def __init__(self):
        self. documents = []
        self.liste_adherants = []
        
    @staticmethod
    def ajouter_document(document):
        try:
            connection = get_connection()
            cusor = connection.cursor()

            query = "insert into documents (titre, auteur, date_publication, genre, type) values (%s, %s, %s, %s, %s)"
            cusor.execute(query, (document.titre, document.auteur, document.date_publication, document.genre, document.type))
            connection.commit()
            print("document ajouter avec succes")
        except Exception as e:
            print("Erreur lors de l'ajout d'un document :", e)
            
        finally:
            cusor.close()
            connection.close()
    
    @staticmethod
    def InscrireMembre(adherent):
        try:
            connection = get_connection()
            Cursor = connection.cursor()

            query = "insert into adherents (nom, prenom) values (%s, %s)"
            Cursor.execute(query, (adherent.nom, adherent.prenom))
            connection.commit()
            print("Adharent ajouter avec succes")
        except Exception as e:
            print("Erreur lors de l'ajout de l'adherent :", e)

        finally:
            Cursor.close()
            connection.close()
        



    @staticmethod
    def Lister_document():
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)

            query = "select * from documents"
            cursor.execute(query)
            for document in cursor.fetchall():
                if document["disponible"] == 1:
                    statut = 'disponible'
                else:
                    statut = "emprunter"
                print(f"id_document : {document["id"]}, Titre :{document["titre"]}, auteur : {document["auteur"]}, type : {document["type"]}, statut : {statut}")
        except Exception as e:
            print("Erreur lors de l'affichage :",e)

        finally:
            cursor.close()
            connection.close()


    def Lister_Emprunt(self,id_adherent):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)

            query = "select * from adherents where id = %s"
            cursor.execute(query, (id_adherent,))

            adherant = cursor.fetchone()

            if adherant is None:
                print("Adherent introuvable")
                return
            
            sql = "select a.prenom, a.nom, d.titre from emprunts e inner join adherents a on e.id_adherent = a.id inner join documents d on e.id_document = d.id where id_adherent = %s and e.etat = 'emprunter'"
            cursor.execute(sql, (id_adherent,))
            emprunt = cursor.fetchall()
            if emprunt == []:
                print("La liste des emprunts est vide")
            for e in emprunt:
                print(f"Prenom : {e["prenom"]}, nom : {e["nom"]} -> {e["titre"]}")
        except Exception as e:
            print(e)
            

     
   

    @staticmethod
    def Lister_membres():
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)

            query = "select * from adherents"
            cursor.execute(query)
            for adherent in cursor.fetchall():
                print(f"id_adherent : {adherent["id"]}, nom : {adherent["nom"]}, prenom : {adherent["prenom"]}")
        except Exception as e:
            print("Erreur lors de l'affichage des adherent :",e)

        finally:
            cursor.close()
            connection.close()              

    @staticmethod
    def valider_pret(id_adherent, id_document, date_prevu):
        try:

            connection = get_connection()
            cursor = connection.cursor(dictionary=True)

            query = "select * from documents where id = %s"
            cursor.execute(query, (id_document,))

            document = cursor.fetchone()

            if document is None:
                print("Document introuvable")
                return
            
            
            query = "select * from adherents where id = %s"
            cursor.execute(query, (id_adherent,))

            adherant = cursor.fetchone()

            if adherant is None:
                print("Adherent introuvable")
                return
            
            if document['type'] == 'livre':
                livre = Livre(document['titre'], document['auteur'], document['date_publication'], document['genre'], document['type'])
                if livre.Emprunt():
                        
                    query = "insert into emprunts (id_document, id_adherent, date_prevu) values (%s, %s, %s)"
                    cursor.execute(query, (document["id"], adherant["id"], date_prevu))
                    sql = "update documents set disponible = %s where id = %s"
                    cursor.execute(sql, (livre.disponible, document['id']))
                    connection.commit()

            if document['type'] == 'magazine':
                magazine = Magazine(document["titre"], document["auteur"], document["date_publication"], document["genre"], document["type"])
                if magazine.Emprunt():
                        
                    query = "insert into emprunts (id_document, id_adherent, date_prevu) values (%s, %s, %s)"
                    cursor.execute(query, (document['id'], adherant['id'], date_prevu))
                    sql = "update documents set disponible = %s where id = %s"
                    cursor.execute(sql, (magazine.disponible, document['id']))
                    connection.commit()
            print("L'emprunt a ete effectuer avec succes")
        except Exception as e:
            print("Erreur lors de la validation du pret:", e)

        finally:
            cursor.close()
            connection.close()
    
  
    
    @staticmethod
    def Retourner_document(id_document, id_adherent, date_prevu):
        try:

            connection = get_connection()
            cusor = connection.cursor(dictionary=True)

            query = "select * from documents where id = %s"
            cusor.execute(query, (id_document,))
            document = cusor.fetchone()
            print(document)

            if document is None:
                print("Document introuvable")
                return
            

            query = "select * from adherents where id = %s"
            cusor.execute(query, (id_adherent,))
            adherent = cusor.fetchone()

            if adherent is None:
                print("Adherent introuvable")
                return

            
            if document['type'] == 'livre':
                livre = Livre(document['titre'], document['auteur'], document['date_publication'], document['genre'], document['type'])
                if not livre.Retour():
                    query = "update documents set disponible = %s where id = %s"
                    cusor.execute(query, (livre.disponible, document['id']))
                    connection.commit()
                    print("Documents retourner avec succes")

                    sql = "update emprunts set etat = %s where id_adherent = %s and id_document = %s and date_prevu = %s"
                    cusor.execute(sql, ('retourner', adherent['id'], document['id'],  date_prevu))
                    connection.commit()
                     

            if document['type'] == 'magazine':
                magazine = Magazine(document['titre'], document['auteur'], document['date_publication'], document['genre'], document['type'])
                if not magazine.Retour():

                    query = "update documents set disponible = %s where id = %s"
                    cusor.execute(query, (magazine.disponible, document['id']))
                    connection.commit()
                    print("Documents retourner avec succes")
        except Exception as e:
            print("Erreur lors du retour:", e)

        finally:
            cusor.close()
            connection.close()

    @staticmethod
    def inscription(utilisateurs):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "insert into utilisateurs (nom, prenom, email, mdp) values (%s,%s,%s,%s)"
            cursor.execute(query, (utilisateurs.nom, utilisateurs.prenom, utilisateurs.email, utilisateurs.mdp))
            connection.commit()
            print("Utilisateur ajouter avec succes")

        except Exception as e:
            print("Erreur lors de l'ajout de l'utilisteur :", e)

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def rechercher_user( email):

        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)

            query = "select * from utilisateurs where email = %s "
            cursor.execute(query, (email,))
            return cursor.fetchone()
        
        except Exception as e:
            print("Erreur lors de la recherche :", e)

        finally:
            cursor.close()
            connection.close()

    
    def se_connecter(self, email, mdp):

        user = self.rechercher_user(email)

        if user is None:
            print("Email invalide")
            return False
        else:
            mdp_hasher = user["mdp"]
            if bcrypt.checkpw(mdp.encode("utf-8"),mdp_hasher.encode("utf-8")):
                return True
            
            







                

        

     