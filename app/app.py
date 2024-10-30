import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database.database import create_session
from database.models import Ventes, Jeuvideo

st.title("Analyse des Ventes de Jeux Vidéo")

session = create_session()

def load_data():
    data = session.query(Ventes).all()
    df = pd.DataFrame()

    return df

df = load_data()

st.header("Explorer les données")
st.write(df.head())

st.header("Explorer les données")
st.write(df.head())

st.header("Ventes globales par région")
sales_by_region = df[[]].sum()
st.bar_chart(sales_by_region)

st.header('Distribution des ventes par région')
fig, ax = plt.subplots()
sns.boxplot(data=df[[]], ax=ax)
st.pyplot(fig)
