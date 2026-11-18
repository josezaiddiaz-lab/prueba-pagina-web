import streamlit as st
import random

# 1. Configuración inicial de la página (siempre debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="Simulador de Dado Online - Prueba Web",
    page_icon="🎲"
)

# 2. Encabezados descriptivos y palabras clave
st.title("🎲 Simulador de Dado Virtual Online")
st.header("Lanza un dado gratis y obtén resultados al instante")
st.write(
    "Bienvenido a esta aplicación web interactiva. Utiliza nuestro generador de números "
    "aleatorios para lanzar un dado de 6 caras en línea de forma rápida y sencilla."
)

# 3. Funcionalidad principal del dado
if st.button("Lanzar dado"):
    resultado = random.randint(1, 6)
    st.success(f"¡El código funciona! Has sacado un: {resultado}")
