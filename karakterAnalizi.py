# -*- coding: utf-8 -*-

"""Veri seti içerisinde yer alan özelliklerin 
    alt/üst aralıkları, 
    kritik seviyelerin neler olabileceği,
    tatil günlerine göre veya mevsimsel olarak nasıl bir değişime sahip olduğu
    ayrıca özelliklerin birbirleri arasındaki ilişkilerin olup olmadığının analizi beklenmektedir."""
    
    
# Kullanılacak kütüphanelerin import edilmesi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('HavaKalitesi.csv', encoding = 'iso-8859-9') 

#alt/üst aralıkları

print("PM10 Değeri için min:",dataset["PM10"].min())
print("PM10 Değeri için max:",dataset["PM10"].max())


print("PM10Debi Değeri için min:",dataset["PM10Debi"].min())
print("PM10Debi Değeri için max:",dataset["PM10Debi"].max())

print("SO2 Değeri için min:",dataset["SO2"].min())
print("SO2 Değeri için max:",dataset["SO2"].max())

print("NO2 Değeri için min:",dataset["NO2"].min())
print("NO2 Değeri için max:",dataset["NO2"].max())

print("NOX Değeri için min:",dataset["NOX"].min())
print("NOX Değeri için max:",dataset["NOX"].max())


print("NO Değeri için min:",dataset["NO"].min())
print("NO Değeri için max:",dataset["NO"].max())


print("O3 Değeri için min:",dataset["O3"].min())
print("O3 Değeri için max:",dataset["O3"].max())

print("HavaSicakligi Değeri için min:",dataset["HavaSicakligi"].min())
print("HavaSicakligi Değeri için max:",dataset["HavaSicakligi"].max())

print("RuzgarHizi Değeri için min:",dataset["RuzgarHizi"].min())
print("RuzgarHizi Değeri için max:",dataset["RuzgarHizi"].max())

print("BagilNem Değeri için min:",dataset["BagilNem"].min())
print("BagilNem Değeri için max:",dataset["BagilNem"].max())


print("HavaBasinc Değeri için min:",dataset["HavaBasinc"].min())
print("HavaBasinc Değeri için max:",dataset["HavaBasinc"].max())




