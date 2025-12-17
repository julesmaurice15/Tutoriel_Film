# Projet Film

Ce dépôt regroupe notre travail pour le cours d'Agilité.

## 📅 Itération 1 : Initialisation et version Java

Cette première phase a consisté à mettre en place des classes de base sur BlueJ et de créer un tutoriel.

- **Documentation :** Ajout du sujet `Agilité Itération 1 Tutoriel.pdf`.
- **Modélisation :** Création des classes `Film.java` et `Categorie.java`.
- **Tests Unitaires :** Implémentation de la classe de test `FilmTest.java` (JUnit) pour valider le comportement des objets.

## 📅 Itération 2 : Python, exigences et tests fonctionnels

Cette seconde phase s'est concentrée sur la conversion du code Java existant vers le langage Python, ainsi que la création d'US, du code correspondant ainsi que des tests fonctionnels associés.

- **Conversion du code :** Traduction des classes Java vers Python dans le fichier `film.py`, `test.py`, `main.py` et `categorie.py`.
- **Tests Python :** Adaptation des tests JUnit vers le module `unittest` dans `test.py`.
- **Tests fonctionnels :** Création de deux US dans /features et des steps associés en utilisant behave.

## 🚀 Comment exécuter le projet

Pour lancer le programme principal :

```bash
python main.py
```

Pour lancer les tests unitaires :

```bash
python test.py
```

Pour lancer les tests fonctionnels :

```bash
behave
```
