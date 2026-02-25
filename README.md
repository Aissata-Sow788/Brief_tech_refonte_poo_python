## Système de Gestion de Bibliothèque (Python POO)

# Description

Ce projet est une application en ligne de commande développée en Python utilisant les principes de la Programmation Orientée Objet (POO).

Il permet de gérer :

- Les livres

- Les magazines

- Les adhérents

- Les emprunts et retours de documents

Le projet met en pratique :

- L’abstraction (ABC, @abstractmethod)

- L’héritage

- Le polymorphisme

- L’encapsulation (@property)

- La gestion des erreurs

Les structures de contrôle (match case)

# Structure du Projet

🔹 Classe Document (abstraite)

Classe mère contenant :

titre

auteur

date_publication

disponible (encapsulé)

Méthodes abstraites :

Emprunt()

Retour()

__str__()

🔹 Classe Livre (hérite de Document)

Ajoute :

genre

Implémente :

Gestion de l’emprunt

Gestion du retour

Affichage formaté

🔹 Classe Magazine (hérite de Document)

Ajoute :

periodiciter

Implémente :

Gestion de l’emprunt

Gestion du retour

Affichage formaté

🔹 Classe Adherant

Contient :

nom

listeEmprunts

Permet de suivre les documents empruntés.

🔹 Classe Bibliothecaire

Gère :

La liste des documents

La liste des membres

L’ajout de livres et magazines

L’inscription des membres

La validation des prêts

Le retour des documents

L’affichage des informations

🔹 Classe Menu

Interface en ligne de commande permettant :

Ajouter un livre

Ajouter un magazine

Afficher les documents

Inscrire un membre

Afficher les membres

Valider un prêt

Afficher les emprunts d’un adhérent

Retourner un document

Quitter

# Fonctionnalités

- Ajouter des livres
- Ajouter des magazines
- Inscrire des membres
- Emprunter un document
- Retourner un document
- Vérifier la disponibilité
- Afficher les emprunts d’un membre
- Validation des entrées utilisateur

# Concepts POO utilisés

🔹 Abstraction avec ABC

🔹 Encapsulation avec attribut privé __disponible

🔹 Héritage (Livre, Magazine)

🔹 Polymorphisme (méthodes Emprunt et Retour)

🔹 Composition (Bibliothecaire contient des documents et membres)

# Lancer le Projet

Installer Python 3.10 ou plus

Exécuter le fichier :
python main.py