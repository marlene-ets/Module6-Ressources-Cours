"""
Exercice pendant le cours du Module 6
Les instructions apparaissent dans les commentaires du script
"""

import numpy as np
import matplotlib.pyplot as plt

# Quelques paramètres pour les graphiques
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 14

# Lecture des données simplifiées (voir pré-traitement dans le script lecture_fichier_horaire.py)
# Utilisation de np.loadtxt
# les deux points dans le nom de fichiers servent à remonter d'un dossier
filename = '../ressources/temperatures_horaire_Mai2025.txt'
vec_temperature = np.loadtxt(filename)

# Tracez le tableau vec_temperature dans un graphique

"""
Le tableau contient des moyennes horaires de temperature relevées 
au cours des jours du mois de Mai 2025. Nous allons reformater le tableau pour
pouvoir l'utiliser de manière statistique
"""

# Redimensionnez le tableau pour avoir les 24h en colonnes
# arr_temperature =

# Calculez la moyenne par jour et identifiez le jour le plus chaud

# Calculez la moyenne horaire pour le mois de Mai 2025

# Superposez les données pour les différentes journées du mois de Mai 2025 en tracant les
# Affichez la moyenne horaire pour le mois de Mai 2025 en noir avec un trait plus épais
# Affichez la température minimale du mois de Mai avec un trait horizontal bleu (plt.axhline)
# Affichez la température maximale du mois de Mai avec un trait horizontal rouge (plt.axhline)
# Mettez une légende, des labels sur les axes, ajoutez une grillle et sauvegardez l'image



"""
Nous allons maintenant faire des sélections dans ces données
"""

# Identifiez les jours avec des températures de moins de 8°

# Identifiez les jours du mois de Mai où la température est restée au dessus de 21°C pendant au moins 7h.

# Comptez le nombre d'heures où la température est restée en dessous de 21°C et au dessus de 8°C

# Créer un filtre pour sélectionner les jours pairs
# Et calculez leur moyenne entre 12h et 14h