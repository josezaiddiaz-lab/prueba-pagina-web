import streamlit as st
import random

st.title("🎲 Prueba de funcionamiento")
st.write("Si puedes leer esto, tu aplicación en Streamlit ya está conectada y funcionando.")

if st.button("Lanzar dado"):
    resultado = random.randint(1, 6)
    st.success(f"¡Has sacado un {resultado}!")
