import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from utils import load_mhd_file, process_coordinates_and_file

# Fonction fictive de prétraitement des données
def preprocess_data(mhd_file, x, y, z):
    # Cette fonction est vide pour l'instant
    # Tu devras implémenter le vrai prétraitement des données ici
    pass

# Fonction fictive pour le traitement des coordonnées et du fichier
def process_coordinates_and_file(mhd_file, x, y, z, selected_model):
    # Charger le modèle correspondant
    if selected_model == "GLCM":
        model = 0
    elif selected_model == "Local Binary Pattern":
        model = 0
    elif selected_model == "Histogram of gradients":
        model = 0
    elif selected_model == "Gabor et Hu Moments":
        model = 0
    elif selected_model == "CNN3D":
        model = 0

    # Exemple de prétraitement des données mhd_file et des coordonnées (à remplacer par ton propre prétraitement)
    processed_data = preprocess_data(mhd_file, x, y, z)

    # Faire la prédiction
    prediction = model.predict(processed_data)

    
    return prediction

import numpy as np
import streamlit as st


# Utility functions from utils.py
from utils import load_mhd_file, process_coordinates_and_file


def main():
    st.set_page_config(page_title="Lung Module Classification", page_icon="🫁", layout="wide")
    # Display the logo
    # Center and enlarge the logo using columns
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")
    with col2:
        st.image("logo.PNG", width=500)
    with col3:
        st.write("")

    st.markdown('<h1 style="color: #1212a1; ">Upload MHD File</h1>', unsafe_allow_html=True)

    # Upload MHD file
    uploaded_file = st.file_uploader("Upload an MHD file", type=["mhd"])

    if uploaded_file:
        st.session_state['mhd_file'] = uploaded_file
        st.success("File uploaded successfully")

    # Input coordinates

      # Entrée des coordonnées
    st.markdown("<h2><span style='font-size: 24px;'>📍 Nodule Coordinates :</span></h2>", unsafe_allow_html=True)
    x = st.number_input("X Coordinate", format="%0.10f")
    y = st.number_input("Y Coordinate", format="%0.10f")
    z = st.number_input("Z Coordinate", format="%0.10f")

    st.markdown("<h2><span style='font-size: 24px;'>📊 Model Selection :</span></h2>", unsafe_allow_html=True)
    models = ["GLCM", "Local Binary Pattern", "Histogram of gradients", "Gabor et Hu Moments", "CNN3D"]
    selected_model = st.selectbox("Select a Model for Classification", models)

    # Bouton pour lancer le traitement du modèle
    if st.button("Process"):
      if 'mhd_file' not in st.session_state:
        st.error("Please upload an MHD file first")
      else:
        # Process the input and file
        score = process_coordinates_and_file(st.session_state['mhd_file'], x, y, z, selected_model)
        st.success(f"Processing complete! Score for {selected_model}: {score}")
    
        # Display the results
        st.subheader("Scores")
        for i, (accuracy, precision) in enumerate(scores):
           st.write(f"Model {i + 1}: Accuracy = {accuracy:.2f}, Precision = {precision:.2f}")



    if __name__ == "__main__":
        main()
