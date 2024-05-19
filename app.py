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

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Cancer du poumons',
                          
                          ['Introduction',
                           'Lung nodule Classification'],
                          icons=['activity','laptop computer','person'],
                          default_index=0)
    


    if (selected == 'Introduction'):
    
    # page title
     st.markdown("<h1 style='text-align: center; color: white;'>Introduction 💻📑</h1>", unsafe_allow_html=True)

     st.subheader("Laptop Price Predictor Introduction") 

     st.write('* <span style="font-size: 20px">Welcome </span>', unsafe_allow_html=True)
    
     st.write('* <span style="font-size: 20px">Using state-of-the-art machine learning </span>', unsafe_allow_html=True)
   
     st.write('* <span style="font-size: 20px">Whether you are a student,</span>', unsafe_allow_html=True)
    
     st.write('* <span style="font-size: 20px">In this project</span>', unsafe_allow_html=True)
    
     st.write('* <span style="font-size: 20px">This model is trained </span>', unsafe_allow_html=True)
   
     st.write('* <span style="font-size: 20px">The dataset contains  </span>', unsafe_allow_html=True)

     st.write('* <span style="font-size: 20px">Scikit-learn library .</span>', unsafe_allow_html=True)

     st.write('* <span style="font-size: 20px">Streamlit is used .</span>', unsafe_allow_html=True)
   
     st.write('* <span style="font-size: 20px">The predicted </span>', unsafe_allow_html=True)

     st.write('* <span style="font-size: 20px">This laptop price predictor</span>', unsafe_allow_html=True)

   
    if (selected == 'Lung nodule Classification'):

     st.set_page_config(page_title="Lung nodule Classification", page_icon="🫁", layout="wide")
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


      # Upload du fichier MHD
     uploaded_file = st.file_uploader("Upload an MHD file", type=["mhd"])

     if uploaded_file:
      st.session_state['mhd_file'] = uploaded_file
      st.success("File uploaded successfully")

     # Entrée des coordonnées
      st.markdown("<h2><span style='font-size: 24px;'>📍 Nodule Coordinates :</span></h2>", unsafe_allow_html=True)
      x = st.number_input("X Coordinate", format="%0.10f")
      y = st.number_input("Y Coordinate", format="%0.10f")
      z = st.number_input("Z Coordinate", format="%0.10f")


     st.markdown("<h2><span style='font-size: 24px;'>📊 Model Selection :</span></h2>", unsafe_allow_html=True)
     model_selection = st.multiselect("Select Models for Classification", ["Model 1", "Model 2", "Model 3"])

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


