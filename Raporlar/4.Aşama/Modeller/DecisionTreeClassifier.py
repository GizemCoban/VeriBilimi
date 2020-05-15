# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:11:23 2020

@author: Gizem Çoban

"""

# DecisionTreeClassifier

# Kütüphanelerin import edilmesi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Veri setinin okunması ve bağımsız-bağımlı değişkenlerin ayrılması
dataset = pd.read_csv('hki.csv')


X=dataset.drop(["Tarih","HKI"], axis=1)
y=dataset["HKI"]
# Feature Scaling (Özellik ölçekleme)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
# Veri setinin eğitim ve test olarak ayrılması
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Eğitim veri setine Decision Tree sınıflandırıcısının uygulanması
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)


# Test verileri ile tahmin yapılması
y_pred = classifier.predict(X_test)


# Confusion matrisinin oluşturulması
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#Accuracy (sınıflandırma için başarım metriği) ölçülmesi
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)
print("Accuracy", acc)


#f1_score (sınıflandırma için başarım metriği) ölçülmesi
from sklearn.metrics import  f1_score
f1_score = f1_score(y_test, y_pred)
print("f1 score", f1_score)

 



 

