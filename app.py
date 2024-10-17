# app.py
import streamlit as st
from prediction import predict

# Titre et description
st.title("Prédiction de l'espèce de fleur Iris")
st.write("Entrez les caractéristiques des fleurs pour prédire leur espèce.")

# Créer des sliders pour les caractéristiques
st.sidebar.header("Caractéristiques de la fleur")
sepal_length = st.sidebar.slider("Longueur du sépale (cm)", 4.0, 8.0, 5.0)
sepal_width = st.sidebar.slider("Largeur du sépale (cm)", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Longueur du pétale (cm)", 1.0, 7.0, 1.5)
petal_width = st.sidebar.slider("Largeur du pétale (cm)", 0.1, 2.5, 0.2)

# Créer un bouton pour lancer la prédiction
if st.sidebar.button("Prédire"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict(features)  # Cela retourne le nom de l'espèce
    st.write(f"L'espèce prédite est : {prediction}")  # Afficher directement le nom
