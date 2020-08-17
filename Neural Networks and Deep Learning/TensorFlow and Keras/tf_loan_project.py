import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

mpl.rcParams['patch.force_edgecolor'] = True
sns.set()
sns.set_style('whitegrid')
data_info = pd.read_csv('DATA/lending_club_info.csv', index_col='LoanStatNew')

def feat_info(col_name):
    print(data_info.loc[col_name]['Description'])
print(feat_info('mort_acc'))

df = pd.read_csv('DATA/lending_club_loan_two.csv')
print(df.describe().transpose())
sns.countplot(x='loan_status', data= df)
plt.show()
sns.distplot(df['loan_amnt'], bins = 30, kde=False)
plt.show()
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap= 'viridis')
plt.show()
feat_info('installment')
sns.scatterplot(x='installment', y = 'loan_amnt', data=df, alpha =0.6, palette='RdYlGn')
plt.show()
