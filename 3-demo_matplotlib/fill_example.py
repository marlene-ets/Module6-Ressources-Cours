import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

data = pd.read_pickle('../ressources/meteo_YUL_WKY_1973_2023.pkl')

left = dt.date(2019, 5, 15)
right = dt.date(2023, 5, 15)

plt.figure(figsize=(8,5))
plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(data.index,data['mean_temp'],label='Moyenne',color='green',linewidth=3.0)
plt.plot(data.index,data['min_temp'],label='Min',color='blue',linewidth=0.5)
plt.plot(data.index,data['max_temp'],label='Max',color='red',linewidth=0.5)
plt.title('Moyenne Hebdomadaire à YUL')
plt.xlim(left,right)
plt.xlabel('Date')
plt.ylabel('Température [°C]')
plt.grid()
plt.legend()
plt.savefig('../images/shaded_area.pdf')
plt.show()

plt.figure(figsize=(8,5))
plt.fill_between(data.index,data['min_temp'],data['max_temp'],color='lightgray',hatch='///',edgecolor='black')
plt.plot(data.index,data['mean_temp'],label='Moyenne',color='green',linewidth=3.0)
plt.plot(data.index,data['min_temp'],label='Min',color='blue',linewidth=0.5)
plt.plot(data.index,data['max_temp'],label='Max',color='red',linewidth=0.5)
plt.title('Moyenne Hebdomadaire à YUL')
plt.xlim(left,right)
plt.xlabel('Date')
plt.ylabel('Température [°C]')
plt.grid()
plt.legend()
plt.savefig('../images/hached_area.pdf')
plt.show()