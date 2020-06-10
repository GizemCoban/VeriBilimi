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
#x=veri.drop(["Tarih","HKI"], axis=1)
x=veri.drop(["PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"], axis=1)
y=labels

#kategorik verilerin kodlanması
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#sayısal verilere dönüştürür.
labelencoder_X = LabelEncoder()
x['Tarih'] = labelencoder_X.fit_transform(x['Tarih'])


# sayısal verilere dönüştürür.
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

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
model.add(Dense(16,input_dim=1,activation="relu"))
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

score = model.evaluate(x_test, y_test, verbose=0)


#Modeli Kaydetme
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
#ağırlıkları HDF5'e seri hale getirme
model.save_weights("model.h5")
print("Model kaydedildi")









