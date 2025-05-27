"""
Ce script importe les données de météo canada pour l'aéroport de St Hubert
pour le mois de Mai 2025. Les moyennes horaires de température sont
sauvegardées dans un fichier texte pour un exercice sous numpy
"""

import numpy as np
import pandas as pd

fichier = 'fr_climat_horaires_QC_7027329_05-2025_P1H.csv'
# Seule la colonne de température est lue.
# Par défaut, les valeurs sont entre guillemets alors elles serait lues sous forme de str
# La colonne est convertie en valeur numérique en spécifiant le séparateur de décimale ","
df_temperature = pd.read_csv(fichier, usecols=['Temp (°C)',], dtype='float', decimal=',')

# La série est convertie en ndarray pour le besoin de l'exercice
temperature = np.asarray(df_temperature['Temp (°C)'])

# Les valeurs pour les jours à venir sont des NaN, ils sont ignorées.
vec_temperature = temperature[~np.isnan(temperature)]

# Export en fichier texte simple
np.savetxt('temperatures_horaire_Mai2025.txt', vec_temperature)