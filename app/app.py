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
    df = pd.DataFrame([(d.id_ventes, d.id_jeu, d.na_sales, d.eu_sales, d.jp_sales, d.other_sales, d.global_sales) for d in data],
                      columns=['ID_Ventes', 'ID_Jeu', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'])
    return df

df = load_data()

st.header("Explorer les données")
st.write(df.head())

st.header("Explorer les données")
st.write(df.head())

st.header("Ventes globales par région")
sales_by_region = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
st.bar_chart(sales_by_region)

st.header('Distribution des ventes par région')
fig, ax = plt.subplots()
sns.boxplot(data=df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']], ax=ax)
st.pyplot(fig)