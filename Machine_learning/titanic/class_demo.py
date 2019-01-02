#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 11:00:57 2018

@author: aditi
"""

import numpy as np;
import pandas as pd;

dataset = pd.read_csv('train.csv')
X = dataset.iloc[:,[2,4,5,6,7,9,11]]
Y = dataset.iloc[:,1]
x_final = X.values
y = Y.values
# Missing Values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy ="mean",axis =0)
imputer = imputer.fit(x_final[:,2:3])
x_final[:,2:3] = imputer.transform(x_final[:,2:3])

#Categorical Values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
x_final[:,1] = labelencoder.fit_transform(x_final[:,1])

label = LabelEncoder()
x_final[:,-1] = label.fit_transform(x_final[:,-1])
# Encoder
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
x_final = onehotencoder.fit_transform(x_final).toarray()

x_final = x_final[:,1:]
#Feature Scaling
from sklearn.preprocessing import StandardScaler
standard_x = StandardScaler()
x_final = standard_x.fit_transform(x_final)

#Train Test Split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_final,y, test_size = 0.2, random_state = 0)


from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=4)  
classifier.fit(x_train, y_train) 

print(sklearn.__version__)