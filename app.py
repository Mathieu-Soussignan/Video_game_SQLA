import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database.database import Session
from database.models import Ventes, JeuVideo, Name, Genre, Editeur, AnneeDeSortie, Plateforme

# Titre de l'application
st.title("Analyse des Ventes de Jeux Vidéo")
st.image("./assets/one_piece.jpg", caption="Bienvenue !", use_column_width=True)

# Connexion à la base de données
session = Session()

# Charger les données de ventes et de jeux vidéo
data = session.query(Ventes).all()
df_ventes = pd.DataFrame([(d.id_ventes, d.id_jeu, d.na_sales, d.eu_sales, d.jp_sales, d.other_sales, d.global_sales)
                          for d in data],
                         columns=['ID_Ventes', 'ID_Jeu', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'])

# Charger les titres de jeux vidéo
title_data = session.query(Name).all()
df_title = pd.DataFrame([(t.id_title,t.title) for t in title_data],columns=['ID_titre','Titre'])

# Charger les noms des jeux
jeux_data = session.query(JeuVideo).all()
df_jeux = pd.DataFrame([(j.id_jeu, j.id_title) for j in jeux_data], columns=['ID_Jeu', 'ID_titre'])

df_jeux_titre = pd.merge(df_jeux,df_title,on='ID_titre',how = 'left') 
# Joindre les tables pour avoir les titres et les ventes dans un même DataFrame
df = pd.merge(df_jeux_titre,df_ventes,on='ID_Jeu', how='left')

# Fermeture de la session
session.close()

# Afficher un aperçu des données
st.header("Explorer les données")
st.write(df.head())

# Comparaison des Jeux Vidéo
st.header("Tableau de Bord Comparatif")

# Sélectionner les jeux à comparer
selected_games = st.multiselect("Sélectionnez les jeux à comparer", options=df['Titre'].unique())

# Filtrer les données en fonction des jeux sélectionnés
if selected_games:
    df_selected = df[df['Titre'].isin(selected_games)]

    # Afficher le tableau comparatif des ventes par région
    st.subheader("Comparaison des Ventes par Région")
    st.write(df_selected[['Titre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']])

    # Visualisation des ventes par région pour chaque jeu
    st.subheader("Ventes par Région pour les Jeux Sélectionnés")

    # Créer un graphique de ventes par région pour chaque jeu sélectionné
    fig, ax = plt.subplots()
    for titre in selected_games:
        ventes = df_selected[df_selected['Titre'] == titre]
        ax.bar(ventes['Titre'], ventes['NA_Sales'], label=f"{titre} - NA Sales")
        ax.bar(ventes['Titre'], ventes['EU_Sales'], label=f"{titre} - EU Sales", bottom=ventes['NA_Sales'])
        ax.bar(ventes['Titre'], ventes['JP_Sales'], label=f"{titre} - JP Sales",
               bottom=ventes['NA_Sales'] + ventes['EU_Sales'])
        ax.bar(ventes['Titre'], ventes['Other_Sales'], label=f"{titre} - Other Sales",
               bottom=ventes['NA_Sales'] + ventes['EU_Sales'] + ventes['JP_Sales'])

    ax.set_xlabel("Jeux Vidéo")
    ax.set_ylabel("Ventes (en millions)")
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Sélectionnez au moins un jeu pour voir la comparaison.")