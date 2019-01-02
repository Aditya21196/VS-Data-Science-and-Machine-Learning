#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 11:54:15 2018

@author: aditi
"""
import numpy as np;
import pandas as pd;

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,0:1].values
Y = dataset.iloc[:,-1].values

#Train Test Split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

# Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)
print(regressor.score(x_test,y_test))
