# Analyse des Ventes de Jeux Vidéo — Application Streamlit

Bienvenue dans l'application **Analyse des Ventes de Jeux Vidéo** ! Ce document vous guidera à travers la compréhension et l'utilisation de cette application interactive construite avec Streamlit, y compris ses fonctionnalités, la structure des fichiers, et son fonctionnement. Que vous soyez analyste, passionné de jeux vidéo, ou simplement curieux d'explorer des données de ventes, cette application est faite pour vous.

## 1. Vue d'ensemble du projet

L'application d'analyse des ventes de jeux vidéo fournit une interface web interactive permettant de visualiser et analyser les ventes de jeux vidéo dans différentes régions. Avec **Streamlit** comme technologie principale, l'application permet aux utilisateurs de comparer les ventes, d'analyser les tendances temporelles, et d'explorer les relations entre diverses caractéristiques des jeux, telles que le genre, la plateforme et l'éditeur. Cet outil est idéal pour obtenir des insights sur le marché du jeu vidéo et comprendre ce qui fait le succès de certains jeux dans différentes régions.

## 2. Fonctionnalités clés

### 2.1 Exploration des données

- **Affichage interactif des données** : L'application affiche un résumé des données de ventes de jeux vidéo, que vous pouvez filtrer et explorer à l'aide d'une interface intuitive.

### 2.2 Analyse comparative

- **Comparaison des ventes** : Sélectionnez plusieurs jeux vidéo et comparez leurs ventes dans différentes régions (Amérique du Nord, Europe, Japon, Autres). Les ventes sont présentées dans un graphique à barres empilées pour une comparaison visuelle facile.

### 2.3 Analyse temporelle

- **Ventes par année** : Analysez les ventes de jeux vidéo en sélectionnant une année de sortie spécifique. Cette fonctionnalité permet de visualiser les jeux populaires pour une année donnée.
- **Évolution des ventes** : Affiche des graphiques en courbe montrant l'évolution des ventes d'un jeu au fil du temps, fournissant des insights sur l'évolution de sa popularité.

### 2.4 Visualisations des données

- Utilise **Matplotlib** pour générer des visualisations intuitives telles que des graphiques à barres empilées et des courbes pour faciliter la compréhension des tendances des données.

## 3. Structure du projet

La structure des fichiers du projet est la suivante :

```
Video_game_SQLA/
├── .github/workflows/
│   └── python_tests.yml  # Actions GitHub pour les tests CI
├── .pytest_cache/
├── .venv/                # Environnement virtuel pour le projet
├── app/
│   └── utils.py          # Fonctions utilitaires pour l'application
├── assets/
│   └── one_piece.jpg     # Image pour la bannière d'accueil
├── data/
│   ├── vgsales_cleaned.csv     # Données nettoyées
│   ├── vgsales.csv       # Données brutes de ventes de jeux vidéo
│   └── vgsales.numbers
├── database/
│   ├── __init__.py
│   ├── database.py       # Gestion de la connexion à la base de données et création des sessions
│   ├── models.py         # Modèles SQLAlchemy pour les tables de la base de données
│   └── vgsale.db         # Base de données SQLite contenant les données de ventes
├── notebook/
├── test/
│   ├── __init__.py
│   └── test_database.py  # Tests unitaires pour les interactions avec la base de données
├── .gitignore            # Fichiers et dossiers à ignorer dans Git
├── app.py                # Point d'entrée principal de l'application Streamlit
├── guide_detail.md       # Guide détaillé pour l'utilisation de l'application
├── initialize_db.py      # Script pour initialiser la base de données
├── populate_db.py        # Script pour remplir la base de données à partir du CSV
├── ReadME.md             # Document actuel
└── requirements.txt      # Dépendances Python pour le projet
```

## 4. Instructions d'installation

Suivez ces étapes pour configurer et exécuter l'application en local :

### 4.1 Prérequis

- Python 3.8+
- Outil d'environnement virtuel (venv)

### 4.2 Installation

1. **Clonez le dépôt** :

   ```sh
   git clone <https://github.com/Mathieu-Soussignan/Video_game_SQLA.git>
   cd Video_game_SQLA
   ```

2. **Créez un environnement virtuel** :

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows, utilisez .venv\Scripts\activate
   ```

3. **Installez les dépendances** :

   ```sh
   pip install -r requirements.txt
   ```

4. **Initialisez la base de données** :

   ```sh
   python initialize_db.py
   ```

5. **Remplissez la base de données** :

   ```sh
   python populate_db.py
   ```

### 4.3 Lancer l'application

Pour lancer l'application Streamlit :

```sh
streamlit run app.py
```

Cela lancera un serveur local, et vous pourrez interagir avec l'application via votre navigateur web.

## 5. Description détaillée des fichiers

### 5.1 Fichiers de l'application

- **app.py** : Point d'entrée principal de l'application. Contient le code Streamlit pour créer l'interface utilisateur interactive, y compris les visualisations de données et les filtres pour sélectionner des jeux et des années.
- **app/utils.py** : Fonctions d'assistance utilisées pour simplifier certaines tâches répétitives dans l'application.

### 5.2 Gestion de la base de données

- **database/models.py** : Définit le schéma pour chaque table de la base de données SQLite à l'aide de SQLAlchemy. Les tables incluent :
  - **Genre** : Représente le genre d'un jeu (ex. : Action, Aventure).
  - **Editeur** : Représente les éditeurs des jeux.
  - **Plateforme** : Représente les plateformes de jeu.
  - **AnneeDeSortie** : Contient les informations sur les années de sortie.
  - **JeuVideo** : Représente un jeu vidéo et contient des relations avec le genre, l'éditeur, la plateforme et l'année de sortie.
  - **Ventes** : Contient les données de ventes pour chaque jeu dans différentes régions.
- **database/database.py** : Gère la connectivité de la base de données, y compris la création de sessions pour les requêtes.
- **database/vgsale.db** : Le fichier de base de données SQLite où toutes les données des jeux vidéo sont stockées.

### 5.3 Population des données

- **populate\_db.py** : Remplit la base de données avec les données du fichier `data/vgsales_cleaned.csv`. Ce script lit le fichier CSV à l'aide de **pandas**, crée des instances des modèles définis dans `models.py` et les ajoute à la base de données pour éviter les doublons.
- **initialize\_db.py** : Configure la base de données en créant des tables à l'aide des métadonnées de SQLAlchemy.

### 5.4 Tests

- **test/test\_database.py** : Contient des tests unitaires écrits avec **pytest**. Les tests incluent :
  - **Instantiation des modèles** : Vérification que chaque modèle peut être créé sans erreurs.
  - **Relations de la base de données** : Vérification du bon fonctionnement des clés étrangères et des relations.

## 6. Fonctionnalités de l'application en détail

### 6.1 Visualisations des données

- **Graphiques à barres** : Comparez les ventes régionales des jeux vidéo sélectionnés.
- **Graphiques à barres empilées** : Comparez différents jeux avec une vue segmentée des performances régionales.
- **Graphiques en courbe** : Visualisez comment les ventes ont évolué au fil du temps pour des jeux spécifiques.

### 6.2 Filtres et interactions

- **Comparaison des jeux** : Les utilisateurs peuvent sélectionner un ou plusieurs jeux et voir directement leurs performances dans différentes régions.
- **Analyse par année** : L'application inclut un menu déroulant de sélection d'année pour filtrer les jeux par année de sortie, fournissant des insights temporels.

## 7. Comment utiliser l'application

1. **Explorer les données** : L'application affiche les premières entrées des données de ventes de jeux vidéo, aidant les utilisateurs à avoir un aperçu.
2. **Comparer les jeux** : Utilisez le widget de sélection multiple pour comparer plusieurs jeux et voir leurs ventes par région.
3. **Analyse temporelle** : Sélectionnez une année pour voir quels jeux étaient les plus populaires et analyser leurs performances globales.

## 8. Dépannage

- **Base de données non remplie** : Si l'application affiche des tableaux vides, assurez-vous d'avoir exécuté `populate_db.py` pour charger les données dans la base de données.
- **Dépendances manquantes** : Si vous rencontrez des erreurs de module manquant, exécutez à nouveau `pip install -r requirements.txt`.
- **Problèmes de format des années** : Assurez-vous que les années sont correctement formatées en tant qu'entiers dans `populate_db.py` pour éviter les problèmes de visualisation.

## 9. Améliorations futures

- **Analyse prédictive** : Introduire une fonctionnalité qui prédit les ventes futures des jeux basées sur les tendances historiques.
- **Filtres avancés** : Permettre aux utilisateurs de filtrer par attributs supplémentaires tels que l'éditeur, la plateforme ou le genre.
- **Graphiques interactifs** : Utiliser des bibliothèques comme **Plotly** pour une meilleure interaction avec les graphiques.

## 10. Collaborateurs

- [Mathieu Soussignan](https://www.mathieu-soussignan.com)
- [Ahmed Bahri](https://www.linkedin.com/in/bahri-amine/) <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Linkedin_icon.svg" alt="LinkedIn" width="20" height="20">
- [José Cardona](https://www.linkedin.com/in/jose-fabian-cardona-hernandez/) <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Linkedin_icon.svg" alt="LinkedIn" width="20" height="20">

## 11. Licence

Ce projet est sous licence MIT.

## 12. Contribution

Les contributions sont les bienvenues ! Veuillez forker le dépôt, créer une nouvelle branche pour votre fonctionnalité ou correction de bug, et soumettre une pull request.

---

Merci d'utiliser l'application **Analyse des Ventes de Jeux Vidéo** !

