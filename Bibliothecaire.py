from Livre import Livre
from Magazine import Magazine
from Adherent import Adherant

class Bibliothecaire:
    def __init__(self):
        self. documents = []
        self.liste_adherants = []
        
    
    def ajouter_livre(self, titre, auteur, date_publication, genre):
        livre = Livre(titre, auteur, date_publication, genre)

        self.documents.append(livre)
        print("Livre ajouter avec succes")

    def ajouter_magazine(self, titre, auteur, date_publication, periodiciter):
        magazine = Magazine(titre, auteur, date_publication, periodiciter)

        self.documents.append(magazine)
        print("Livre ajouter avec succes")



    def InscrireMembre(self,nom):
        adherant= Adherant(nom)

        self.liste_adherants.append(adherant)
        print("Membre ajoute")


    def Lister_document(self):
        if self.documents==[]:
            print("La liste est vide")
        else:
            print("--------------------- La liste des Documents ----------------------")
            for document in self.documents:
                print(document)  

    def Lister_Emprunt(self,nom_adherant):
        adherant_trouver=None
        if self.liste_adherants==[]:
            print("la liste est vide")
        else:
            for adherant in self.liste_adherants:
                if adherant.nom==nom_adherant:
                    adherant_trouver=adherant

            if adherant_trouver==None:
                print("cette membre n'existe pas") 
                return 

            if adherant_trouver.listeEmprunts==[]: 
                print(f"{adherant_trouver.nom} n'a pas encore emprunter de documents ")
            else:
                print(f"------------------Liste des documents emprunter par {adherant_trouver.nom} ---------------------")    
                for i in adherant_trouver.listeEmprunts:
                    print(i)  

   

        
    def Lister_membres(self):
        if self.liste_adherants==[]:
            print("La liste des membres est vide")
        else:
            for membre in self.liste_adherants:
                print(membre)                

    def valider_pret(self, nom_membre, titre_document):

        document_trouvee = None
        for i in self.documents:
            if i.titre == titre_document:
                document_trouvee = i

        membre_trouvee = None
        for m in self.liste_adherants:
            if m.nom == nom_membre:
                membre_trouvee =  m

        if document_trouvee==None and membre_trouvee==None:
            print("livre et membre non existant")
            return
        
        if membre_trouvee is None:
            print("Membre introuvable")
            return
        else:
            if document_trouvee is None:
                print("Document introuvable")
                return
            else:
        
                resultat = document_trouvee.Emprunt()
                    
                if resultat:
                    membre_trouvee.listeEmprunts.append(document_trouvee)
                    print("Pret validé avec succès.")


    def Retourner_document(self, nom_membre, titre_document):

        document_trouvee = None
        for i in self.documents:
            if i.titre == titre_document:
                document_trouvee = i
                print(f"Document trouver {i}")

        membre_trouvee = None
        for m in self.liste_adherants:
            if m.nom == nom_membre:
                membre_trouvee =  m

        if document_trouvee==None and membre_trouvee==None:
            print("livre et membre non existant")
            return
        
        if membre_trouvee is None:
            print("Membre introuvable")
            return
        else:
            if document_trouvee is None:
                print("Document introuvable")
                return
            else:

                resultat = document_trouvee.Retour()
                    
                if resultat:
                    membre_trouvee.listeEmprunts.remove(document_trouvee)
                    print("Le document a ete retourner avec succès.")     