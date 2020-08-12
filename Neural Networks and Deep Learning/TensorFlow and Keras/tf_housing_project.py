import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
import tensorflow as tf 
mpl.rcParams['patch.force_edgecolor'] = True
sns.set()
sns.set_style('whitegrid')

#real world data

df = pd.read_csv('DATA/kc_house_data.csv')
print(df.head())
#print(df.isnull().sum()) #no missing data! 
#print(df.describe().transpose())
plt.figure(figsize = (10,6))
sns.distplot(df['price'])
plt.show()
sns.countplot(df['bedrooms'])
plt.show()
print(df.corr()['price'].sort_values()) # - checking for correlations
plt.figure(figsize = (10,6))
sns.scatterplot(x = 'price', y = 'sqft_living', data = df )
plt.show()
plt.figure(figsize = (10,6))
sns.boxplot(x='bedrooms', y = 'price', data=df)
plt.show()





