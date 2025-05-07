# Chem ECO
import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("chemeco.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Loaded data: ", df)

    if st.checkbox  ("Show described stats"):
        st.write(df.describe())


    

    
