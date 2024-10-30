from database.models import Genre,Editeur,Plateforme,AnneeDeSortie,Base

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
df = pd.read_csv('data/vgsales.csv')

genres = []
editeurs = []
plateformes = []
Annes = []

for i in df['Genre'].unique():
    genres.append(Genre(nom_genre = i))

for i in df[''].unique():
    editeurs.append(Editeur(nom_editeur = i))



for i in genres:
    session.add(i)
session.commit()