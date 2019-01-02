# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np;
import pandas as pd;
 # Choosing 
dataset = pd.read_csv('train.csv')
X = [dataset.iloc[:,2:3] , dataset.iloc[:,4:8] , dataset.iloc[:,9:10], dataset.iloc[:,-1]]
x_temp = pd.concat(X,axis = 1) # axis = 1 means column wise concatenation
Y = dataset.iloc[:,1:2]
x_final = x_temp.values
y = Y.values


"""
Missing data
"""
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy ="mean",axis =0)
imputer = imputer.fit(x_final[:,2:3])
x_final[:,2:3] = imputer.transform(x_final[:,2:3])

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
x_final[:,1] = labelencoder.fit_transform(x_final[:,1])

label = LabelEncoder()
x_final[:,-1] = label.fit_transform(x_final[:,-1])
'''
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
x_final = onehotencoder.fit_transform(x_final).toarray()
'''
#Feature scaling

from sklearn.preprocessing import StandardScaler
standard_x = StandardScaler()
x_final = standard_x.fit_transform(x_final)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_final,y, test_size = 0.2, random_state = 0)
from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=4)  
classifier.fit(x_train, y_train) 

y_pred = classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, y_pred))

'''
Finding of the actual test data 
'''
test_data = pd.read_csv('test.csv')
#test_data = test_data.fillna(lambda x: x.median())

test_data = test_data.fillna(method='ffill')
id_pas = test_data.iloc[:,0].values 
temp_test = [test_data.iloc[:,1] , test_data.iloc[:,3:7] , test_data.iloc[:,8], test_data.iloc[:,10]]
temp_test_x = pd.concat(temp_test,axis = 1) # axis = 1 means column wise concatenation

x_data = temp_test_x.values
'''
imputer1 = Imputer(missing_values="NaN",strategy ="mean",axis =0)
imputer1 = imputer1.fit(x_data[:,2:3])
x_data[:,2:3] = imputer1.transform(x_data[:,2:3])


labelencoder2 = LabelEncoder()
x_data[:,1] = labelencoder2.fit_transform(x_data[:,1])

label2 = LabelEncoder()
x_data[:,-1] = label2.fit_transform(x_data[:,-1])

standard_x2 = StandardScaler()
x_data = standard_x2.fit_transform(x_data)
'''
'''
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy ="mean",axis =0)
imputer = imputer.fit(x_data[:,2:3])
x_data[:,2:3] = imputer.transform(x_data[:,2:3])
'''
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
x_data[:,1] = labelencoder.fit_transform(x_data[:,1])

label = LabelEncoder()
x_data[:,-1] = label.fit_transform(x_data[:,-1])
'''
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
x_final = onehotencoder.fit_transform(x_final).toarray()
'''
#Feature scaling

from sklearn.preprocessing import StandardScaler
standard_x = StandardScaler()
x_data = standard_x.fit_transform(x_data)
pred_final = classifier.predict(x_data)
print(pred_final)

d = {'PassengerId' : pd.Series(id_pas),
      'Survived' : pd.Series(pred_final)}

df = pd.DataFrame(d)
df.to_csv('submit.csv', encoding='utf-8', index=False)



 
 







