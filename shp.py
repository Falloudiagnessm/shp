import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
st.set_option('deprecation.showPyplotGlobalUse', False)
#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
# Chargement du fichier Shapefile avec GeoPandas
@st.cache_data
def load_shapefile(shapefile_path):
    return gpd.read_file(shapefile_path)

shapefile_path = "gadm36_SEN_1.shx"
gdf = load_shapefile(shapefile_path)

# Liste des arrondissements uniques dans le jeu de données de Thies
#thies_arrondissements = gdf[gdf['NAME_1'] == 'Thiès']['NAME_3'].unique()
st.write(gdf) 

# Création de la carte avec GeoPandas
st.title("Carte  Senegal")
fig, ax = plt.subplots()
gdf.plot(ax=ax, color='gray')  # Rendre les autres arrondissements en gris pr défaut

fig1, ax = plt.subplots()

gdf[gdf['NAME_1'] == 'Dakar'].plot(ax=ax, color='gray') 

fig2, ax = plt.subplots()

gdf[gdf['NAME_1'] == 'Diourbel'].plot(ax=ax, color='gray') 
 
st.pyplot(fig)
st.title("Carte  dakar")
st.pyplot(fig1)
st.title("Carte  Diourbel")
st.pyplot(fig2)
