import numpy as np;
import pandas as pd;

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,0:4]
Y = dataset.iloc[:,-1]

x_val = X.values
y_val = Y.values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_x = LabelEncoder()
x_val[:,3] = label_x.fit_transform(x_val[:,3])

onehotencoder = OneHotEncoder(categorical_features=[3])
x_val = onehotencoder.fit_transform(x_val).toarray()

#For dummy Variable Trap, use 1 less
x_val = x_val[:,1:]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_val,y_val,test_size = 0.2,random_state =0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)
print(regressor.score(x_test,y_test))

#Backward Elimination, Feature selection 

import statsmodels.formula.api as sm
x_val = np.append ( arr = np.ones([50,1]).astype(int), values = x_val, axis = 1)

x_opt = x_val[:,[0,1,2,3,4,5]]
#Ordinary Least Squares
#endog is dependent varaible and exog is indepenedent matrix
regressor_ols = sm.OLS(endog = y_val, exog = x_opt)
regressor_ols = regressor_ols.fit()
regressor_ols.summary()

#1
x_opt = x_val[:,[0,2,3,4,5]]
#Ordinary Least Squares
#endog is dependent varaible and exog is indepenedent matrix
regressor_ols = sm.OLS(endog = y_val, exog = x_opt)
regressor_ols = regressor_ols.fit()
regressor_ols.summary()
#2
x_opt = x_val[:,[0,3,4,5]]
#Ordinary Least Squares
#endog is dependent varaible and exog is indepenedent matrix
regressor_ols = sm.OLS(endog = y_val, exog = x_opt)
regressor_ols = regressor_ols.fit()
regressor_ols.summary()
#3
x_opt = x_val[:,[0,3,5]]
#Ordinary Least Squares
#endog is dependent varaible and exog is indepenedent matrix
regressor_ols = sm.OLS(endog = y_val, exog = x_opt)
regressor_ols = regressor_ols.fit()
regressor_ols.summary()

#Final Predictions 
regressor.fit(x_train[:,[2,4]],y_train)
y_pred = regressor.predict(x_test[:,[2,4]])

