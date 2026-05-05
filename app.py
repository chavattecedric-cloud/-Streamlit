import streamlit as st
import pandas as pd
from datetime import date
from datetime import time
taxis="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
dftaxis=pd.read_csv(taxis)


# Titre principal de l'application (affiché en haut de la page)
st.title("Bienvenue sur le site de CEDRIC")

#selectionné arrondissement
choix_arrond = st.selectbox(label="indiquez votre arrondissement",options = dftaxis['pickup_borough'].unique())


# Affiche une ligne de texte simple (sans mise en forme particulière)
st.text(f"Tu as choisi : {choix_arrond}")

if choix_arrond == 'Manhattan':
    st.image("https://www.new-york-city.fr/wp-content/uploads/2020/11/Manahttan_principale.jpg")
elif choix_arrond == 'Queens':
    st.image("https://static-cms.routard.com/web-routard/uploads/large_pont-de-queensboro-entre-manhattan-et-long-island-city.1614508_7ae8b5f078.jpg")
elif pd.isna(choix_arrond):
    st.image("https://thumbs.dreamstime.com/z/marque-de-question-et-%C3%A9pingle-d-emplacement-comme-illustration-vectorielle-en-tant-qu-ic%C3%B4ne-163462882.jpg")
elif choix_arrond =='Bronx':
    st.image("https://cdn.sanity.io/images/nxpteyfv/goguides/60568b46498809d98c4a354cb6bb88f49dd53547-1600x1067.jpg")
elif choix_arrond =='Brooklyn':
    st.image("https://www.nyc.fr/wp-content/uploads/2024/09/quartier_de_brooklyn-scaled.jpg")






