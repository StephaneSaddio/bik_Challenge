
#%%
# Nous allons dans un premier temps importer les packages qu'il nous faudra.
# Puis dans un second temps impoter les données de totem montpellier
# Enfin faire une étude exploratoire des données et en faire une prédictoire.
# Assez parlez ! Le temps est à l'action, lançons nous!


#%% Importation des packages python
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy import stats as st
import matplotlib.pyplot as plt

#%% Importation des données de totem Montpellier

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv'
path_target = "Times_Velos.csv"
velo = pd.read_csv(url)
# %%

print(velo)

#%%
velo.columns=['Date','Hours','Total','Today_total', 'Unnamed','Remark']

velo.pop("Unnamed")
velo.pop("Remark")
velo.pop("Grandtotal")

velo.drop(0,0,inplace=True)
velo.drop(1,0,inplace=True)

# %%
from datetime import date
import datetime
import time
#%%

velo['Date'] = pd.to_datetime(data['Date'])

velo['Heure'].fillna(0, inplace = True)

velo.tail(70)

#%%

#On décortique la date
velo['Day of Week'] = data['Date'].apply(lambda time: time.dayofweek)
velo['Year'] = data['Date'].apply(lambda t: t.year)
velo.columns=['Date','Heure','Todaystotal','DayOfWeek','Year']

velo.tail(20)
# %%
