import streamlit as st
from multiapp import MultiApp
from apps import Raura, Raura_dem

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Imagen Satelital", Raura.app)
apps.add_app("Modelo Digital de Elevación", Raura_dem.app)

# The main app
apps.run()
