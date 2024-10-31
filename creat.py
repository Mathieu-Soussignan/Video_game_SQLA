from database.models import Genre,Editeur,Plateforme,AnneeDeSortie,JeuVideo,Ventes,Base

import numpy as np
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



uniqueGenre = df['Genre'].unique()
uniquePublisher = df['Publisher'].unique()
uniquePlateforme = df['Platform'].unique()
uniqueYear = df['Year'].unique()

for i in uniqueGenre:
    session.add(Genre(nom_genre = i))

for i in uniquePublisher:
    session.add(Editeur(nom_editeur = i))

for i in uniquePlateforme:
    session.add(Plateforme(nom_plateforme = i))

for i in uniqueYear:
    session.add(AnneeDeSortie(date = int(i)))




for i in range(len(df)):
    nom = df["Name"].loc[i]
    indGenr = np.where(uniqueGenre == df["Genre"].loc[i])[0][0]+1
    indPub = np.where(uniquePublisher == df["Publisher"].loc[i])[0][0]+1
    indPlat = np.where(uniquePlateforme == df["Platform"].loc[i])[0][0]+1
    indYear = np.where(uniqueYear==df["Year"].loc[i])[0][0]+1
    session.add(JeuVideo(titre = nom, id_genre = int(indGenr), id_editeur = int(indPub), id_plateforme = int(indPlat), id_sortie = int(indYear)))


for i in range(len(df)):
    session.add(Ventes(id_jeu = i+1,na_sales = df['NA_Sales'].loc[i],
                       eu_sales = df['EU_Sales'].loc[i],
                       jp_sales = df['JP_Sales'].loc[i],
                       other_sales = df['Other_Sales'].loc[i],
                       global_sales = df['Global_Sales'].loc[i]))

session.commit()