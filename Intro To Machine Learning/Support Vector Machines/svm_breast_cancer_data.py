import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

mpl.rcParams['patch.force_edgecolor'] = True
sns.set()
sns.set_style('whitegrid')
cancer = load_breast_cancer()
#print(cancer['DESCR'])
#we are trying to predict if the cancer is malignant of beningn 
df_feat = pd.DataFrame(cancer['data'], columns = cancer['feature_names'])
print(df_feat.head())
x = df_feat
y = cancer['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 101)
model = SVC()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(classification_report(y_test, predictions)) 
print('\n')
print(confusion_matrix(y_test, predictions)) 

param_grid = {'C': [0.1, 1,10,100,1000], 'gamma': [1,0.1,0.01,0.001,0.0001]}
grid = GridSearchCV(SVC(), param_grid, verbose = 3)
grid.fit(x_train, y_train)
print(grid.best_params_)
print(grid.best_estimator_)