import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Manipulation de données et création de graphiques")

dataset = st.selectbox(label="Quel dataset souhaite-tu utiliser ?", options = ['flights','iris', 'taxis'])

if dataset =="flights":
    df=sns.load_dataset('flights')
elif dataset == "iris":
    df=sns.load_dataset('iris')
elif dataset == "taxis":
    df=sns.load_dataset('taxis')

st.dataframe(df)

x= st.selectbox(label= "selectionne ta colonne X", options = df.columns)

y= st.selectbox(label= "selectionne ta colonne Y", options = df.columns)


graph=st.selectbox(label = "quel graphique veut-tu utiliser ?", options = ["scatter_chart", "line_chart", "bar_chart"])

if graph == "scatter_chart":
    st.scatter_chart(df,x=x,y=y)
elif graph == "line_chart":
    st.line_chart(df,x=x, y=y)
elif graph == 'bar_chart' :
    st.bar_chart(df,x=x, y=y)
    
if st.checkbox(label="Afficher la matrice de corrélation") is True:
    sns.heatmap(df.corr(numeric_only=True))
    st.pyplot(plt.gcf())