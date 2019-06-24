# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:39:03 2019

@author: Yadav
"""

from sklearn import tree
from sklearn import svm
from sklearn import naive_bayes
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
model=tree.DecisionTreeClassifier()
model1=svm.SVC()
model2=naive_bayes.GaussianNB()
model.fit(X,Y)
model1.fit(X,Y)
model2.fit(X,Y)
prediction = model.predict([[190, 70, 43]])
prediction1=model1.predict([[190, 70, 43]])
prediction2=model2.predict([[190, 70, 43]])
print("The output by decision tree is")
print(prediction)
print("The output by SVM is")
print(prediction1)
print("The output by Naive bayes is")
print(prediction2)

