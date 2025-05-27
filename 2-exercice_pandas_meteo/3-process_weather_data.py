"""
Ce script demontre l'usage de pandas pour du nettoyage de donnees,
des traces et des statistiques
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Quelques parametres pour les graphiques
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 16


# Fichier obtenu a l'aide du pretraitement du script '2-download_meteo_data.py'
# filename = '<specifiez-moi>'

# Fichier dans le dossier de ressources
filename = '../ressources/meteo_YUL_DLY_1972_2022.csv'

# Lecture des donnees
# Si l'index des colonne est fourni dans le fichier, il est possible de fournir
# le numero de sa colonne pour eviter d'avoir un nouvel indice
df_meteo = pd.read_csv(filename,index_col=0)
# Quelques info sur les donnees et les tableaux
# Utilisez le debogger et 'View as DataFrame'
print(df_meteo.head())
print(df_meteo.shape)
print('Liste des champs:\n',list(df_meteo.columns))
print('\n')

# L'argument 'inplace' permet de modifier la dataframe courante.
# Sinon par defaut c'est la dataframe de sortie de la methode qui porte la modification

# On renomme les colonnes pour faciliter les appels
# Le dictionnaire associe le nom courant avec le nom souhaite
current_names = ['Date/Time', 'Mean Temp (°C)', 'Min Temp (°C)', 'Max Temp (°C)', 'Total Precip (mm)']
simplified_names = ['time', 'mean_temp', 'min_temp', 'max_temp', 'precip']
dict_renaming =dict(zip(current_names, simplified_names))
df_meteo.rename(columns= dict_renaming, inplace=True)

# On ne garde que les colonnes qui nous interessent (celles avec des valeurs numeriques)
# On cherche donc les noms de colonnes qui ne sont pas dans notre short-list
mask_columns = np.isin(df_meteo.columns, simplified_names)

# On supprime les colonnes identifiees
columns_to_drop = df_meteo.columns[~mask_columns]
df_meteo.drop(columns=columns_to_drop,inplace=True)

# On supprime les colonnes qui ne contiendraient que des NaN
# (argument all comme pour les fonctions numpy) avec la methode 'dropna'
df_meteo.dropna(axis=1, how='all', inplace=True)

# On supprime les lignes dont les valeurs de temperatures sont des NaN
# (par exemple pour les mois dans le futur)
df_meteo.dropna(subset='mean_temp', axis=0, how='any', inplace=True)

# On convertit la date (chaine de caractere) en timestamp 
df_meteo.time = pd.to_datetime(df_meteo.time.values)
# On utilise cette colonne comme indice cela va permettre les manipulations suivantes.
df_meteo.set_index('time', inplace=True)

print('Liste des champs:\n',list(df_meteo.columns))
print('\n')

# Ici le trace des temperatures journalieres
df_meteo.plot(y=['min_temp','mean_temp','max_temp'])
plt.show()

# On peut realiser des reechantillonnages temporels tres facilement
# Voir https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
df_year = df_meteo.resample('YS').mean()  # Moyenne annuelle
df_month = df_meteo.resample('MS').mean() # Moyenne mensuelle
df_week = df_meteo.resample('7D').mean() # Moyenne hebdomadaire

# Pour tracer des donnees de plusieurs dataframe il faut specifier les axes
# que l'on recupere du premier graphique
ax = df_meteo.plot(y=['mean_temp',], label=['daily average',])
df_month.plot(ax=ax, y=['mean_temp',], label=['monthly average',])
df_year.plot(ax=ax, y=['mean_temp',], label=['yearly average',],
             linewidth=3.0, color='black')
plt.show()

# On peut faire une moyenne glissante
# Cela conserve le meme echantillonnage que les donnes de debut
# Mais c'est consistant avec la moyenne hebdomadaire vue precedemment
# Mais il y a un delai
df_7days = df_meteo.rolling(7).mean()
df_week['time_shift'] = df_week.index + pd.Timedelta("7 day")
ax = df_meteo.plot(y=['mean_temp',], label=['daily',])
df_7days.plot(ax=ax, y=['mean_temp',], label=['sliding 7 days average',])
df_week.plot(ax=ax, x='time_shift', y=['mean_temp',], label=['weekly',])
plt.show()

# On peut sauvegarder en format binare la base de donne traitee
df_week.to_pickle('meteo_YUL_WKY_1972_2022.pkl')