import streamlit as st
import geemap.foliumap as geemap
import os
import ee

def app():
    st.title("Imágen Satelital Raura")

    keys = list(geemap.basemaps.keys())[1:]

    basemap = st.selectbox("Seleccionar un mapa base", keys)
    table = ee.FeatureCollection("users/davidroncal123/AEA_RAURA")
    
    
    Map = geemap.Map(center=[-10.53,-76.7519], zoom=11)
    Map.add_basemap(basemap)
    # Add Earth Engine dataset
    Raura_RGB = ee.Image('users/davidroncal123/Imagen_truecolor_geo')
    Raura_INF = ee.Image('users/davidroncal123/Imagen_infrarojo_geo')

    # Set visualization parameters.
    vis_params = {
        'min': 117.93390786749023,
        'max': 1526.5943326709896,
        'bands':['b1','b2','b3'],
        'gamma':1.6
    }
    vis_params2 = {
      'min': 0,
      'max': 4000,
      'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}


    # Add Earth Engine layers to Map
 
    Map.addLayer(Raura_RGB.clip(table), vis_params, 'Raura RGB')
    Map.addLayer(Raura_INF.clip(table), vis_params, 'Raura Infrarojo')
    Map.to_streamlit(height=650)
