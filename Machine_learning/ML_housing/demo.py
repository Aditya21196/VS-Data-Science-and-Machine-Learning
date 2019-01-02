#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 21:45:45 2018

@author: aditi
"""

import pandas as pd
import numpy as np

dataset = pd.read_excel('estate.xlxs')
x= dataset.iloc[:,1:7].values
y = dataset.iloc[:,-1].values

#Feature Scaling 
from sklearn.preprocessing import StandardScaler
standard_x = StandardScaler()
x = standard_x.fit_transform(x)

#train-test split 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)

#Multiple Regression 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)
print(regressor.score(x_test,y_test))

#backward Elimination
import statsmodels.formula.api as sm
x = np.append ( arr = np.ones([414,1]).astype(int), values = x, axis = 1)

x_opt = x[:,[0,1,2,3,4,5,6]]
regressor_ols = sm.OLS(endog = y, exog = x_opt)
regressor_ols = regressor_ols.fit()
regressor_ols.summary()

x_opt = x[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt)
regressor_ols = regressor_ols.fit()
regressor_ols.summary()


#Decision Tree
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state =0)
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

print(regressor.score(x_test,y_test))

#Random Forest 
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 12, random_state = 1)
regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)

print(regressor.score(x_test,y_test))

#Gradient Boosting 
from sklearn.ensemble import GradientBoostingRegressor
gbrt = GradientBoostingRegressor(max_depth = 5, n_estimators = 15,learning_rate = 0.1)
gbrt.fit(x_train,y_train)

print(gbrt.score(x_test,y_test))