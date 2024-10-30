from database.models import Genre,Editeur,Plateforme,AnneeDeSortie,JeuVideo,Base

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

try:
    os.remove('database.sqlite') 
except:
    pass

# Déclaration du moteur de base de données
engine = create_engine('sqlite:///database.sqlite')

# Création de la base de données
Base.metadata.create_all(engine)

# Création d'une session
session = Session(bind=engine)

#Lecture du Data Frame
df = pd.read_csv('data/vgsales_cleaned.csv')

genres = []
editeurs = []
plateformes = []
Annes = []
jeux = []

for i in df['Genre'].unique():
    genres.append(Genre(nom_genre = i))

for i in df['Publisher'].unique():
    editeurs.append(Editeur(nom_editeur = i))

for i in df['Platform'].unique():
    plateformes.append(Plateforme(nom_plateforme = i))

for i in df['Year'].unique():
    Annes.append(AnneeDeSortie(date = i))






# for i in df['Name']:
#     jeux.append(JeuVideo(titre = i,))

    
    
    
#     # Clés étrangères vers d'autres tables
#     id_genre = Column(Integer, ForeignKey('genre.id_genre'))
#     id_editeur = Column(Integer, ForeignKey('editeur.id_editeur'))
#     id_plateforme = Column(Integer, ForeignKey('plateforme.id_plateforme'))
#     id_sortie = Column(Integer, ForeignKey('annee_de_sortie.id_sortie'))





for i in genres:
    session.add(i)
for i in editeurs:
    session.add(i)
for i in plateformes:
    session.add(i)
for i in Annes:
    session.add(i)
session.commit()