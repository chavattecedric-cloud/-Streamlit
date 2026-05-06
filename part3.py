import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from streamlit_authenticator import Authenticate

compte=pd.read_csv('compte.csv')

dico={'usernames':{}}

for index, ligne in compte.iterrows():
    dico['usernames'][ligne['name']] = {
        'name': ligne['name'],
        'password': ligne['password'],
        'email': ligne['email'],
        'failed_login_attemps': ligne['failed_login_attemps'],
        'logged_in': ligne['logged_in'],
        'role': ligne['role']
    }

authenticator = Authenticate(
    dico,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# 1. Définir les fonctions de pages (EN DEHORS du if)
def accueil():
    st.title("Bienvenue !")

def album():
    st.title("Mes photos ratées ... Sisi")
    col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne : 
    with col1:
        st.header("moi qui transforme les donnéees")
        st.image("https://www.mba-esg.com/sites/default/files/images/hot-content-news/desktop/devenir-data-analyst-mba-esg.jpg", width=350)

    # Contenu de la deuxième colonne :
    with col2:
        st.header("Moi qui Analyse les données")
        st.image("https://www.esiea.fr/wp-content/uploads/2025/01/data-scientist.png", width=350)

    # Contenu de la troisième colonne : 
    with col3:
        st.header("Moi qui présente mon dashboard")
        st.image("https://bunny-wp-pullzone-3xue3q6yzy.b-cdn.net/wp-content/uploads/2024/11/EM-BLOG-data-analytics-vs-data-science-1351962914.png", width=350)

# 2. Login
authenticator.login()

# 3. Gérer l'authentification
if st.session_state["authentication_status"]:
    # Menu dans la sidebar
    with st.sidebar:
        selection = option_menu(menu_title=None, options=["Accueil", "Album photo"])
    # Afficher la bonne page
    if selection == "Accueil":
        accueil()
    elif selection == "Album photo":
        album()
    authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("Username ou password incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Remplis les champs username et mot de passe")