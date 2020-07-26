import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV


mpl.rcParams['patch.force_edgecolor'] = True
sns.set()
sns.set_style('whitegrid')
iris = sns.load_dataset('iris')

#sns.pairplot(iris, hue = "species") 
#plt.show() 
#^ the setosa species seems to be the most seperable 
setosa = iris[iris['species']=='setosa']
sns.kdeplot(setosa['sepal_width'], setosa['sepal_length'],cmap="plasma", shade=True, shade_lowest=False)
plt.show()

x = iris.drop('species', axis = 1)
y = iris['species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = SVC()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(classification_report(y_test, predictions)) 
print('\n')
print(confusion_matrix(y_test, predictions)) 

