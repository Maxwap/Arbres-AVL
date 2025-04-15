# Mini-projet : Surveillance de Connexions Réseau avec AVL

## Fonctionnement du programme

Ce projet est une application console qui permet de surveiller et gérer les connexions entrantes sur un serveur. Chaque connexion est identifiée par une adresse IP et automatiquement horodatée lors de son ajout.

Le programme permet :
- d’ajouter une adresse IP,
- de supprimer une adresse IP spécifique,
- de nettoyer les connexions inactives depuis plus de X minutes,
- de rechercher une adresse IP,
- d’afficher les connexions triées par IP,
- de sauvegarder les connexions dans un fichier texte,
- et de recharger automatiquement les connexions enregistrées précédemment.

L’ensemble des interactions se fait via un menu simple et intuitif, accessible dans le terminal à l'exécution de `main.py`.

---

## Intérêt d’un arbre AVL dans ce contexte

L’utilisation d’un arbre AVL (arbre binaire de recherche auto-équilibré) permet de garantir des performances efficaces même lorsque le nombre de connexions devient important. Contrairement à une liste chaînée, où les opérations de recherche ou de suppression peuvent nécessiter un parcours complet, l’AVL offre une complexité logarithmique pour l’insertion, la suppression et la recherche.

Par rapport à un arbre binaire de recherche simple (BST), l’AVL évite les cas de déséquilibre (par exemple lorsque les données sont insérées en ordre croissant), ce qui garantit des performances stables dans tous les cas. Il offre également un tri naturel des adresses IP, ce qui simplifie l'affichage ou le nettoyage par parcours infixe.

---

## Architecture du projet

Le projet est structuré de manière modulaire :

- `Connexion` est une classe représentant une adresse IP accompagnée de son horodatage.
- `AVLTree` est une classe qui implémente un arbre AVL, avec toutes les opérations classiques : insertion, suppression, recherche, parcours, nettoyage et gestion des connexions inactives.
- `main.py` propose une interface utilisateur textuelle avec menu interactif.
- `connexions.txt` est un fichier texte utilisé pour sauvegarder et recharger automatiquement les connexions existantes.
- `test_avl_connexions.py` est un script de test permettant de simuler des connexions avec des dates dans le passé, afin de valider le bon fonctionnement du nettoyage, de la recherche, et de l'affichage.

---

## Choix algorithmiques

Les connexions sont comparées via leurs adresses IP pour le tri dans l’arbre. Le nettoyage des connexions repose sur la comparaison du timestamp de chaque nœud avec l’heure actuelle, en utilisant les outils du module `datetime`.

L’arbre est équilibré dynamiquement grâce aux rotations AVL, ce qui permet de maintenir une hauteur optimale et des performances constantes. Le fichier de sauvegarde est un simple fichier texte, lisible et réutilisable, sans dépendance à des formats externes.

Aucune bibliothèque externe n’est utilisée, conformément aux consignes du projet.

---

## Résultats et tests

Des tests ont été réalisés avec des adresses IP artificiellement horodatées. Ils montrent que :
- le tri des IPs fonctionne grâce au parcours infixe de l’arbre,
- les connexions inactives sont supprimées correctement selon un seuil défini,
- la recherche d’une IP fonctionne même après nettoyage,
- le programme reste stable et performant avec un volume croissant de connexions.

Le script de test `test_avl_connexions.py` simule plusieurs cas, avec des connexions récentes ou anciennes, pour vérifier le comportement du système.

---

## Utilisation

Pour lancer l’application principale :

