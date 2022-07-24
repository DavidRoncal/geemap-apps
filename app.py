import streamlit as st
from multiapp import MultiApp
from apps import Raura

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Raura Imagen Satelital", Raura.app)

# The main app
apps.run()
