# %% [markdown]
# # Data Manipulation

# %%
import pandas as pd

# %%
data = pd.read_csv('vehicles.csv')
data.head()

# %%
data.shape

# %%
# delete columns without data
data = data.dropna(axis=1)

# %%
# delete rows without data
data = data.dropna()

# %%
data.columns

# %%
# rename columns names
data = data.rename(columns={'Make': 'Manufacturer',
                            'Engine Displacement':'Displacement'})

# %%
column_order = ['Year', 'Displacement', 'Cylinders','Manufacturer', 'Model', 
       'Transmission', 'Drivetrain', 'Vehicle Class', 'Fuel Type',
       'Fuel Barrels/Year', 'City MPG', 'Highway MPG', 'Combined MPG',
       'CO2 Emission Grams/Mile', 'Fuel Cost/Year']
data = data[column_order]       
data.head()
# %% [markdown]
# ## filtering records

# %%
data = data.rename(columns={'Manufacturer':'Make',
                            'Displacement':'Engine Displacement'})

# %%
data.columns

# %%
filtered = data[(data['Make'] == 'Ford')]
filtered.head()

# %%
filtered = data[(data['Make'] == 'Ford') & 
                (data['Cylinders']==6)]
filtered.head()

# %%
mpg_labels = ['very low','low','moderate','high','very higy']
data['bins'] = pd.cut(data['Combined MPG'],5, labels=mpg_labels)
data[['Combined MPG','bins']].tail(20)
# %%
data['binsq'] = pd.qcut(data['Combined MPG'],5, labels=mpg_labels)
data[['Combined MPG','bins','binsq']].head(30)

# %%
cutoffs = [7,14,21,23,30,40]
data['binsc'] = pd.cut(data['Combined MPG'],cutoffs, labels=mpg_labels)
data[['Combined MPG','bins','binsq','binsc']].head(30)

# %% [markdown]
# ## Categorias Condicionales

# %%
print(data['Transmission'].unique())

# %%
data.loc[data['Transmission'].str.startswith('A'), 'TransType'] = 'Automatic'
data.loc[data['Transmission'].str.startswith('M'), 'TransType'] = 'Manual'
# %%
print(data['TransType'].unique())

# %% [markdown]
# ## Variables categóricas de codificación en caliente

# %%
data['Drivetrain'].unique()

# %%
drivetrain = pd.get_dummies(data['Drivetrain'])
drivetrain.head()
# %% [markdown]
# ## Combinando tramas de datos

# %%
avg_mpg = data.groupby('Make', as_index=False).agg({'Combined MPG':'mean'})
avg_mpg.columns = ['Make', 'Avg_MPG']
avg_mpg.head()

# %%
data = pd.merge(data, avg_mpg, on='Make')
data.head()

# %%
data = pd.concat([data, drivetrain], axis=1)
data.head()
# %%
lexus = data[data['Make']=='Lexus']
type(lexus)
# audi = data[data['Make']=='Audi']
# lexus_audi = pd.concat([lexus, audi], axis=0)
# lexus_audi.head()
# lexus_audi.tail()
# %%
melted = pd.melt(data, id_vars=['Year','Make','Model'],
              value_vars=['City MPG','Highway MPG', 'Combined MPG'])
print(melted.head())
print(melted.tail())


# %% [markdown]
# # Cálculos de Dataframe

# %%
import pandas as pd
import numpy as np

# %%
# External data
data['MPG'] = data['Combined MPG'] * 1.5
data[['Combined MPG', 'MPG']].head()

# %%
# two or more columns
data['MPG'] = (data['City MPG'] + data['Highway MPG']) / 2
data[['Combined MPG', 'MPG']].head()

# %% [markdown]
# # la función np.where es un if

# %%
# Conditionals
data['MPG'] = np.where((data['City MPG'] + data['Highway MPG'])/2 == data['Combined MPG'],0, (data['City MPG'] + data['Highway MPG']) / 2)
data[['Combined MPG', 'MPG']].head()

# %% [markdown]
# ## Cálculos con funciones

# %%
data['Avg'] = data.sum(axis=1)
data.head()

# %% [markdown]
# # Agrupamientos

# %%
data.columns

# %%
data.groupby(['Transmission'])

# %%
# agreregate 3 differents columns and cumpute their mean
data.groupby(['Transmission'])['Highway MPG', 'City MPG', 'Combined MPG'].mean()
# %%
# aggregate based on twho columns and compute the meadian
data.groupby(['Fuel Type', 'Cylinders'])['CO2 Emission Grams/Mile'].median()

# %%
# compute mean, median and standard deviation
data.groupby(['Fuel Type'])['Combined MPG'].agg(['mean','median', 'std'])


# %% [markdown]
# # Funciones de agregación personalizadas

# %%
from scipy import stats

def agg_mode(x):
       return(stats.mode(x)[0])

# %%
data.groupby(['Transmission'])['Vehicle Class'].agg(agg_mode)

# %%
data.columns

# %%
