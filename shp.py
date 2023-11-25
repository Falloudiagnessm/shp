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

shapefile_path1 = "gadm36_SEN_1.shx"
gdf1 = load_shapefile(shapefile_path1)
shapefile_path2 = "praguefile_5.shp"
gdf2 = load_shapefile(shapefile_path2)
# Liste des arrondissements uniques dans le jeu de données de Thies
#thies_arrondissements = gdf[gdf['NAME_1'] == 'Thiès']['NAME_3'].unique()
#st.write(gdf1) 
st.write(gdf2) 
# Création de la carte avec GeoPandas
st.title("Carte  Senegal")
fig, ax = plt.subplots()
gdf1.plot(ax=ax, color='gray')  # Rendre les autres arrondissements en gris pr défaut

fig1, ax = plt.subplots()

gdf1[gdf1['NAME_1'] == 'Thies'].plot(ax=ax, color='gray') 

fig2, ax = plt.subplots()

gdf1[gdf1['NAME_1'] == 'Diourbel'].plot(ax=ax, color='gray') 
 
st.pyplot(fig)
st.title("Carte  De la region de Thies")
st.pyplot(fig1)
#st.title("Carte  Diourbel")
#st.pyplot(fig2)

#demarche
#git clone https://github.com/Falloudiagnessm/shp.git
#cd shp
#git commit -m "moncommit"
#git add .
#git push -u origin main
#mot de pass

#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
#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
