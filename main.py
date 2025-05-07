# Chem ECO
import streamlit as st
import pandas as pd

st.title("ChemECO - CSV Visuals")

uploaded_file = st.file_uploader("Sube el archivo chemeco.csv", type="csv")

if uploaded_file is not None:
    try:
        # Leer el CSV
        df = pd.read_csv(uploaded_file, encoding='utf-8', sep=None, engine='python')
        st.write("Datos cargados:", df)

        # Mostrar estadísticas
        if st.checkbox("Mostrar estadísticas descriptivas"):
            st.write(df.describe())

        # Mostrar gráfico de línea
        if st.checkbox("Mostrar gráfico de línea"):
            columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()

            if columnas_numericas:
                columna_seleccionada = st.selectbox("Selecciona una columna numérica para graficar", columnas_numericas)
                st.line_chart(df[columna_seleccionada])
            else:
                st.warning("No hay columnas numéricas para graficar.")

    except Exception as e:
        st.error(f"Error al leer el archivo CSV: {e}")
