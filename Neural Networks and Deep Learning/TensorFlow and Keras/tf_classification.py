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

df = pd.read_csv('DATA/cancer_classification.csv')
# print(df.describe().transpose())

#for classificatoin tasks, use a countplot of the label to see the number of instances per label to see if it's well balanced
sns.countplot(x='benign_0__mal_1', data = df)
plt.show() #seems to be pretty well balanced, no extreme difference 
df.corr()['benign_0__mal_1'][:-1].sort_values().plot(kind='bar')
plt.show()
X = df.drop('benign_0__mal_1', axis = 1).values
y = df['benign_0__mal_1'].values 
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=101)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#model = Sequential()
#model.add(Dense(30, activation='relu'))
#model.add(Dense(15, activation='relu'))
#model.add(Dense(1, activation='sigmoid')) #because this is a binary classification problem 
#model.compile(optimizer='adam', loss= 'binary_crossentropy')
#model.fit(x=X_train, y = y_train, epochs=600, validation_data =(X_test, y_test)) #this large number of epochs would probably overfit 
#loss_df = pd.DataFrame(model.history.history)
#loss_df.plot()
#plt.show() 

# ^ the validation and training loss both decrease, but then after a few epochs, the validation loss starts to increase, 
# so we're training with too many epochs
# we need to stop the training before it gets out of hand 
model = Sequential()
model.add(Dense(30, activation='relu'))
model.add(Dropout(0.5)) #half of the neurons will be turned off randomly 
model.add(Dense(15, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss= 'binary_crossentropy')
early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose = 1 ,patience=25) 
#mode is basically what you're trying to do, so minimize the thing you're monitoring or maximize it 
model.fit(x=X_train, y = y_train, epochs=600, validation_data =(X_test, y_test), callbacks=[early_stop]) #so now we know 600 was wayy too much 
loss_df = pd.DataFrame(model.history.history)
loss_df.plot()
plt.show() #we get flattening out which is good 

#with the Dropout, the loss graph is improved 

predictions = model.predict_classes(X_test)

print(classification_report(y_test, predictions)) 
print(confusion_matrix(y_test, predictions)) 









