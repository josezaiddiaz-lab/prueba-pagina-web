import streamlit as st
import random

# 1. Configuración inicial de la página
st.set_page_config(
    page_title="Simulador de Dado Online - Prueba Web",
    page_icon="🎲"
)

# 2. Código de Google Analytics dividido para evitar recortes
url_ga = "https://googletagmanager.com" + "/gtag/js?id=G-6TDRW374MN"

codigo_google = f"""
<script async src="{url_ga}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-6TDRW374MN');
</script>
"""
st.markdown(codigo_google, unsafe_allow_html=True)

# 3. Encabezados descriptivos y palabras clave
st.title("🎲 Simulador de Dado Virtual Online")
st.header("Lanza un dado gratis y obtén resultados al instante")
st.write(
    "Bienvenido a esta aplicación web interactiva. Utiliza nuestro generador de números "
    "aleatorios para lanzar un dado de 6 caras en línea de forma rápida y sencilla."
)

# 4. Funcionalidad principal del dado
if st.button("Lanzar dado"):
    resultado = random.randint(1, 6)
    st.success(f"Has sacado un: {resultado}")
