import streamlit as st
import geemap.foliumap as geemap
import os
import ee

def app():
    st.title("DEM Raura")

    dem = ee.Image('USGS/SRTMGL1_003')
    table = ee.FeatureCollection("users/davidroncal123/AEA_RAURA")

    Map = geemap.Map(center=[-10.53,-76.7519], zoom=11)
    Map.add_basemap('HYBRID')
    
    # Set the region of interest by simply drawing a polygon on the map
    
    region = ee.Geometry.Polygon(
        [[[-77.25522258180023, -10.001142906420185],
          [-77.25522258180023, -11.006411564927092],
          [-76.21323802369476, -11.006411564927092],
          [-76.21323802369476, -10.001142906420185]]])



    # Set the date range

    vis_params = {
    "min": 4149.245450898364,
    "max": 5257.294794667802
    }

    Map.addLayer(dem.clip(table), vis_params, 'STRM DEM', True, 1)
    Map

    # Add Earth Engine layers to Map
    Map.to_streamlit(height=650)
