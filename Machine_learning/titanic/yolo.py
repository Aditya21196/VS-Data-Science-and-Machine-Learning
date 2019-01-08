#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:01:37 2019

@author: aditi
"""

import numpy as np;
import pandas as pd;

dataset = pd.read_csv('train.csv')
X = dataset.iloc[:,[2,4,5,6,7,9]]
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
'''
label = LabelEncoder()
x_final[:,-1] = label.fit_transform(x_final[:,-1])
# Encoder
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
x_final = onehotencoder.fit_transform(x_final).toarray()

x_final = x_final[:,1:]
'''
#Feature Scaling
from sklearn.preprocessing import StandardScaler
standard_x = StandardScaler()
x_final = standard_x.fit_transform(x_final)

#Train Test Split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_final,y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state =0)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
from sklearn.metrics import accuracy_score
print (accuracy_score(y_pred,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors = 5)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_pred,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_pred,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))


#Decision Trees
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_pred,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))


#Ensemble Learning 
#Random Forest 
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 15,random_state =0)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_pred,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))


#Voting Classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
svm_clf = SVC()
voting_clf = VotingClassifier(estimators=[('lr',log_clf),('rf',rnd_clf),('svc',svm_clf)],voting ='hard')
voting_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
for clf in (log_clf, rnd_clf, svm_clf , voting_clf):
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    print(clf.__class__.__name__,accuracy_score(y_test,y_pred))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))


#Soft Voting , all classifiers should estimate probabilities
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
knn_clf = KNeighborsClassifier()
voting_clf = VotingClassifier(estimators=[('lr',knn_clf),('rf',rnd_clf)],voting ='soft')
voting_clf.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
for clf in (knn_clf, rnd_clf , voting_clf):
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    print(clf.__class__.__name__,accuracy_score(y_test,y_pred))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
'''

#Bagging Classifier 
# This is same as Random Forest , Bagging of Decision trees    
from sklearn.ensemble import BaggingClassifier
bagging_clf = BaggingClassifier(DecisionTreeClassifier(),n_estimators = 400)
bagging_clf.fit(x_train,y_train)
y_pred = bagging_clf.predict(x_test)

print(accuracy_score(y_test,y_pred))    
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

from sklearn.ensemble import BaggingClassifier
bagging_clf = BaggingClassifier(LogisticRegression(),n_estimators = 100)
bagging_clf.fit(x_train,y_train)
y_pred = bagging_clf.predict(x_test)

print(accuracy_score(y_test,y_pred))    

from sklearn.ensemble import BaggingClassifier
#from sklearn.naive_bayes import GaussianNB
bagging_clf = BaggingClassifier(KNeighborsClassifier(),n_estimators = 100)
bagging_clf.fit(x_train,y_train)
y_pred = bagging_clf.predict(x_test)

print(accuracy_score(y_test,y_pred))    
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

# ADABOOST ALGORITHM
from sklearn.ensemble import AdaBoostClassifier
ada_clf = AdaBoostClassifier(DecisionTreeClassifier(),n_estimators = 100,algorithm ="SAMME.R",learning_rate=0.5)
ada_clf.fit(x_train,y_train)
y_pred = ada_clf.predict(x_test)
print(accuracy_score(y_pred,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
'''
test_data = pd.read_csv('test.csv')
#test_data = test_data.fillna(lambda x: x.median())

test_data = test_data.fillna(method='ffill')
id_pas = test_data.iloc[:,0].values 
temp_test = test_data.iloc[:,[1,3,4,5,6,8]]
#temp_test_x = pd.concat(temp_test,axis = 1) # axis = 1 means column wise concatenation

x_data = temp_test.values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
x_data[:,1] = labelencoder.fit_transform(x_data[:,1])
'''
label = LabelEncoder()
x_data[:,-1] = label.fit_transform(x_data[:,-1])
# Encoder
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
x_data = onehotencoder.fit_transform(x_data).toarray()

x_data = x_data[:,1:]
'''
from sklearn.preprocessing import StandardScaler
standard_x = StandardScaler()
x_data = standard_x.fit_transform(x_data)
y_pred = voting_clf.predict(x_data)
d = {'PassengerId' : pd.Series(id_pas),
      'Survived' : pd.Series(y_pred)}

df = pd.DataFrame(d)
df.to_csv('submit.csv', encoding='utf-8', index=False)


 
    