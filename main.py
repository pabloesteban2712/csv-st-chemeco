# Chem ECO
import streamlit as st
import pandas as pd

st.title ("ChemECO - CSV Visuals")

uploaded_file = st.file_uploader("chemeco.csv", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8', sep=None, engine='python')
        st.write("Datos cargados:", df)

        if st.checkbox("Mostrar estadísticas descriptivas"):
            st.write(df.describe())

    except Exception as e:
        st.error(f"Error al leer el archivo CSV: {e}")
    

    
