#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 11:59:24 2018

@author: aditi
"""

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,0:1].values
Y = dataset.iloc[:,-1].values

#Train Test Split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree= 2)
x_poly = poly_reg.fit_transform(x_train)
from sklearn.linear_model import LinearRegression 
reg = LinearRegression()
reg.fit(x_poly,y_train)

#Prediction 
y_pred = reg.predict(poly_reg.fit_transform(x_test))
print (reg.score(poly_reg.fit_transform(x_test),y_test))
#Visualization
