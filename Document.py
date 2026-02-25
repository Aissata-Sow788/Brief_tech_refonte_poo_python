from abc import ABC ,abstractmethod

class Document(ABC):
    def __init__(self, titre, auteur, date_publication,type, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.date_publication = date_publication
        self.type=type
        self.__disponible = disponible

      

    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def disponible(self, statut):
        self.__disponible = statut

    @abstractmethod
    def Emprunt(self):
        pass
    
    @abstractmethod
    def Retour(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass