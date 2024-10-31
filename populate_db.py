import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Base, Genre, Editeur, Plateforme, AnneeDeSortie, JeuVideo, Ventes

# Connexion à la base de données SQLite
engine = create_engine('sqlite:///database/vgsale.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Charger le fichier CSV
df = pd.read_csv('./data/vgsales.csv')

# Dictionnaires pour stocker les objets déjà insérés, évitant les doublons
genres = {}
editeurs = {}
plateformes = {}
annees = {}

# Boucle sur chaque ligne du fichier CSV
for index, row in df.iterrows():
    # Gestion de l’entité `Genre`
    genre_name = row['Genre']
    if genre_name not in genres:
        genre = Genre(nom_genre=genre_name)
        session.add(genre)
        session.flush()
        genres[genre_name] = genre.id_genre
    id_genre = genres[genre_name]

    # Gestion de l’entité `Editeur`
    editeur_name = row['Publisher']
    if editeur_name not in editeurs:
        editeur = Editeur(nom_editeur=editeur_name)
        session.add(editeur)
        session.flush()
        editeurs[editeur_name] = editeur.id_editeur
    id_editeur = editeurs[editeur_name]

    # Gestion de l’entité `Plateforme`
    plateforme_name = row['Platform']
    if plateforme_name not in plateformes:
        plateforme = Plateforme(nom_plateforme=plateforme_name)
        session.add(plateforme)
        session.flush()
        plateformes[plateforme_name] = plateforme.id_plateforme
    id_plateforme = plateformes[plateforme_name]

    # Gestion de l’entité `AnneeDeSortie`
    annee_date = row['Year']
    if annee_date not in annees:
        annee = AnneeDeSortie(date=annee_date)
        session.add(annee)
        session.flush()
        annees[annee_date] = annee.id_sortie
    id_sortie = annees[annee_date]

    # Ajouter un nouveau jeu vidéo
    jeu = JeuVideo(
        titre=row['Name'],
        id_genre=id_genre,
        id_editeur=id_editeur,
        id_plateforme=id_plateforme,
        id_sortie=id_sortie
    )
    session.add(jeu)
    session.flush()

    # Ajouter les ventes du jeu
    ventes = Ventes(
        id_jeu=jeu.id_jeu,
        na_sales=row['NA_Sales'],
        eu_sales=row['EU_Sales'],
        jp_sales=row['JP_Sales'],
        other_sales=row['Other_Sales'],
        global_sales=row['NA_Sales'] + row['EU_Sales'] + row['JP_Sales'] + row['Other_Sales']
    )
    session.add(ventes)

# Commit final pour enregistrer toutes les données
session.commit()
session.close()
print("Données insérées avec succès dans la base de données.")