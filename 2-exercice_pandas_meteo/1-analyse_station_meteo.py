"""
Ce script est une introduction a pandas
On peut voir le filtrage de champs afin de selectionner une station meteo
a Montreal qui nous permettra d'analyser des donnes de temperatures horaires
depuis 1973 et au moins jusqu'a 2023.
"""
import numpy as np
import pandas as pd


# On lit l'inventaire des stations meteo au Canada
download_url = (
    "https://collaboration.cmc.ec.gc.ca/cmc/climate/"
    "Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv"
)

# Le fichier est telecharge directement en memoire
inventory = pd.read_csv(download_url,skiprows=3)

# Affichage simplifie avec la methode 'head'
print(inventory.head())
print('\n') # C'est pour sauter la ligne dans la console


# Les titres des colonnes sont accessibles avec l'attribut 'columns'
print('Liste des champs:\n',list(inventory.columns))

# Exemple d'une aggregation et l'application de la methode 'count'
print('\n')
print('Nombre de station par province')
print(inventory.groupby('Province')['Name'].count())

"""
On cherche une station a MONTREAL qui fournit une info par heure depuis 1973 
"""
# Recherche du mot cle MONTREAL au QUEBEC
# on utilise la methode 'contains' disponible pour les champs de type str
mask_mtl = np.logical_and(inventory['Name'].str.contains("MONTREAL"),
                          inventory['Province'].str.contains("QUEBEC"))
df_montreal = inventory[mask_mtl]

print('\n')
print('Nombre de stations a MONTREAL:',df_montreal['Name'].count())

# Recherche des stations qui enregistrent les donnees horaires depuis 1973
mask_hly_1973 = df_montreal['HLY First Year'] <= 1973
mask_hly_2023 = df_montreal['HLY Last Year'] >= 2023
mask_hly_range = np.logical_or(mask_hly_1973, mask_hly_2023)

# Selection de champs
columns_interest = ('Name','Climate ID','Station ID','HLY First Year','HLY Last Year')

df_select = df_montreal[mask_hly_range].loc[:,columns_interest]

print('\n')
print("Stations de MONTREAL mesurant par heure depuis 1973 ou jusqu'en 2023")
print(df_select)

# Pour visualiser les dataframe dans pycharm :
# Mettez un breakpoint et utilisez le deboggeur
# Une fois au breakpoint, vous pouvez visualiser les dataframes avec 'View as DataFrame'


