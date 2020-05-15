# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:45:23 2020

@author: Gizem ÇOBAN
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#verisetinin yüklenmesi
veri=pd.read_csv("hki.csv")
#sınıf sayısını belirle
label_encoder=LabelEncoder().fit(veri.HKI)
labels=label_encoder.transform(veri.HKI)
classes=list(label_encoder.classes_)

x=veri.drop(["Tarih","HKI"], axis=1)
y=labels

#verilerin standartlaştırılması
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)

#eğitim ve test verilerinin hazırlanması
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3) #%20sini testte kullanma


#çıktı değerlerinin kategorileştirilmesi
from tensorflow.keras.utils import to_categorical
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)


#YSA Modelinin oluşturulması
from tensorflow.keras.models import Sequential

#Dense ysa oluşturacağımız kısımdır.
from tensorflow.keras.layers import Dense

#16 tane nöron olsun. 20 tane alanımız bulunmakta. activasyonumuzda relu olsun
model=Sequential()
#girdi katmanı
model.add(Dense(16,input_dim=11,activation="relu"))
#ara katmanlar 3 tane eklendi
model.add(Dense(12,activation="relu"))
model.add(Dense(14,activation="relu"))
model.add(Dense(10,activation="relu"))
#çıktı katmanı
#çıktı sayısı kaçsa o kadar nöron olmak zorunda. 
#activasyonu softmax olmak zorunda çünkü sınıflandırma yapılmaktadır.
model.add(Dense(2,activation="softmax"))
model.summary()


#Modelin Derlenmesi
model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])

#modelin eğitilmesi epochs süresi40 verildi
model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=30)


#gerekli değerlerin gösterilmesi
print ("Ortalama Eğitim Kaybı:",np.mean(model.history.history["loss"]))
print ("Ortalama Eğitim Başarımı:",np.mean(model.history.history["accuracy"]))
print ("Ortalama Doğrulama Kaybı:",np.mean(model.history.history["val_loss"]))
print ("Ortalama Doğrulama Başarımı:",np.mean(model.history.history["val_accuracy"]))

#Eğitim ve Doğrulama Başarımlarının Gösterilmesi
import matplotlib.pyplot as plt
plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Başarımı")
plt.ylabel("Başarım")
plt.xlabel("Epak")
plt.legend(["Eğitim","Test"],loc="upper left")
plt.show


#Eğitim ve Doğrulama Kayıplarının Gösterilmesi
import matplotlib.pyplot as plt
plt.plot(model.history.history["loss"])
plt.plot(model.history.history["val_loss"])
plt.title("Model Kaybı")
plt.ylabel("Kayıp")
plt.xlabel("Epak")
plt.legend(["Eğitim","Test"],loc="upper left")
plt.show





