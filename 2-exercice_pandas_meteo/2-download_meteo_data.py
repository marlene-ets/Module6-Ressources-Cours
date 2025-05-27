"""
Ce script permet de telecharger des donnees meteo
"""
import requests
import pandas as pd
import os


# Ici on illustre l'utilisation du module requests pour telecharger des paquets de donnees d'une url

# Le site suivant permet de telecharger des donnees (open data) en utilisant une REST API.
url = "https://climate.weather.gc.ca/climate_data/bulk_data_e.html"
# Le detail de la commande a ete obtenu en lisant la documentation associee a ce site.
# En particulier la commande HLY ci-dessous permet de telecharger les donnees horaires (timeframe=1) par mois
# En particulier la commande DLY ci-dessous permet de telecharger les donnees journaliere (timeframe=2) par mois


# On doit fournir le numero de la station (champ 'Station ID') de la liste
# La station "MONTREAL/PIERRE ELLIOTT TRUDEAU INTL A" a ete renomme "MONTREAL INTL A" a partir de 2013
# Voir les donnees issues des filtres dans le script '1-analyse_station_meteo.py'
station_ID_olddata = 5415
station_ID_newdata = 51157

# L'utilisateur les format des donnees a telecharger
# (les donnees seront fournies au format CSV)
print('Format de donnees disponible:')
print('  DLY -> journalier')
print('  HLY -> horaire')
format_donnees = input("Selectionnez le format a telecharger pour l'aeroport YUL\n")

partname = input("Entrez le debut du nom de fichier pour les sauvegardes de donnees\n")

# On selectionne une plage d'annees
start_year = int(input("Selectionnez la premiere annee a telecharger\n"))
end_year = int(input("Selectionnez la derniere annee a telecharger\n"))

for year in range(start_year,end_year+1):
    if year < 2013:
        station_ID = station_ID_olddata
    else:
        station_ID = station_ID_newdata

    if format_donnees == 'DLY':
        timeframe = 2
        month = 1 # we get the full year
        options = (f"format=csv&stationID={station_ID}&Year={year}&Month={month}"
                   f"&Day=14&timeframe={timeframe}&submit= Download+Data")
        filename = f'{partname}_{format_donnees}_{year}.csv'
        with open(filename,'wb') as fcsv:
            r = requests.get(f'{url}?{options}')
            fcsv.write(r.content)
        
    elif format_donnees== 'HLY':
        timeframe = 1 # we get one month
        for month in range(1,13):
            options = (f"format=csv&stationID={station_ID}&Year={year}&Month={month}"
                       f"&Day=14&timeframe={timeframe}&submit= Download+Data")
            filename = f'{partname}_{format_donnees}_{year}_{month:02d}.csv'
            with open(filename,'wb') as fcsv:
                r = requests.get(f'{url}?{options}')
                fcsv.write(r.content)



# Une fois les donnees telechargees, les fichiers sont concatenees puis supprimes
# Les fonctions read_csv et concat sont employees

init = True  # Mode d'initialisation
df1 = None

if format_donnees== 'DLY':
    for year in range(start_year,end_year+1): 
        filename = f'{partname}_{format_donnees}_{year}.csv'
        if init:
            df1 = pd.read_csv(filename)
            init = False  # Fin de l'initialisation
        else:
            df2 = pd.read_csv(filename)
            df1 = pd.concat((df1, df2), join='inner')
        os.remove(filename)

elif format_donnees== 'HLY':
    for year in range(start_year,end_year+1): 
        for month in range(1,13):
            filename = f'{partname}_{format_donnees}_{year}_{month:02d}.csv'
            if init:
                df1 = pd.read_csv(filename)
                init = False  # Fin de l'initialisation
            else:
                df2 = pd.read_csv(filename)
                df1 = pd.concat((df1, df2), join='inner')
            os.remove(filename)

# Reset index and drop the one by month/year
df1.reset_index(inplace=True,drop=True)
df1.to_csv(f'{partname}_{format_donnees}_{start_year}_{end_year}.csv')
