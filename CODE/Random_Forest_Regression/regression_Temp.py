# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt


# Importing the dataset
dataset = pd.read_csv('Temp.csv')
#dataset['Date'] = pd.to_datetime(dataset['Date'])
#dataset['Date'] = dataset['Date'].map(dt.datetime.toordinal)

X = dataset.iloc[:, 4:7].values
y = dataset.iloc[:, 1:4].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting the Regression Model to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 500, random_state = 0)
regressor.fit(X_train,y_train)
# Predicting a new result
y_pred = regressor.predict([[20,4,2019],[21,4,2019],[22,4,2019],[31,12,2019]])

y_pred = regressor.predict(X_test)
y_pred = np.reshape(y_pred, (366, 1))
y_diff = y_pred - y_test
y_diff_max_0 = y_diff[:,0]
y_diff_max_0 = max(y_diff_max_0[0])
y_diff_max_1 = max(y_diff[1])
y_diff_max_2 = max(y_diff[2])
y_diff_st_0 = np.std(y_diff[:,0])



Prediction = pd.read_csv('Pred.csv')
X_prediction = Prediction.iloc[0:305, 1:4].values
y_prediction = regressor.predict(X_prediction)


import numpy
a = numpy.asarray(y_prediction)
numpy.savetxt("preiction_system.csv", a, delimiter=",")



