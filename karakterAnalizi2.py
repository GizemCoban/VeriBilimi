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
import datetime
import random


def HKICalculate (SO2, NO2, O3, PM10):
    seviyeSO2=0
    seviyeNO2=0
    seviyeO3=0
    seviyePM10=0
    hki = 0
    
    if SO2 <93:
        seviyeSO2 = 1
    elif SO2 <200:
        seviyeSO2 = 2
    elif SO2 <493:
        seviyeSO2 = 3
    elif SO2 <810:
        seviyeSO2 = 4
    elif SO2 <1609:
        seviyeSO2 = 5
    elif SO2 <2674:
        seviyeSO2 = 6
        
    if NO2 <102:
        seviyeNO2 = 1
    elif NO2 <192:
        seviyeNO2 = 2
    elif NO2 <689:
        seviyeNO2 = 3
    elif NO2 <1242:
        seviyeNO2 = 4
    elif NO2 <2380:
        seviyeNO2 = 5
    elif NO2 <3910:
        seviyeNO2 = 6
    
    if O3 <108:
        seviyeO3 = 1
    elif O3 <248:
        seviyeO3 = 2
    elif O3 <328:
        seviyeO3 = 3
    elif O3 <408:
        seviyeO3 = 4
    elif O3 <808:
        seviyeO3 = 5
    elif O3 <1208:
        seviyeO3 = 6
    
    if PM10 <54:
        seviyePM10 = 1
    elif PM10 <154:
        seviyePM10 = 2
    elif PM10 <254:
        seviyePM10 = 3
    elif PM10 <354:
        seviyePM10 = 4
    elif PM10 <424:
        seviyePM10 = 5
    elif PM10 <604:
        seviyePM10 = 6
        
    seviye = max(seviyePM10, seviyeO3, seviyeNO2, seviyeSO2 )
    

    
    return seviye

dataset = pd.read_csv('HavaKalitesi.csv', encoding = 'iso-8859-9') 

# Veriler farklı dataframelere bölündü
haftaIci = pd.DataFrame(columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"])
haftaSonu = pd.DataFrame(columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"])
yaz = pd.DataFrame(columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"])
kis = pd.DataFrame(columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"])
sonbahar = pd.DataFrame(columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"])
ilkbahar = pd.DataFrame(columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc","HKI"])

for i in range(len(dataset)):
    tarih = dataset["Tarih"][i].split("/")
    tarihNo= datetime.datetime(int(tarih[2]), int(tarih[0]), int(tarih[1])).weekday()
    #HKİ Sonucu
    hki=HKICalculate( dataset.iloc[i]["SO2"], dataset.iloc[i]["NO2"], dataset.iloc[i]["O3"], dataset.iloc[i]["PM10"])
    
    # Haftaiçi Haftasonu Kontrolü
    if(tarihNo<5):
        haftaIci.loc[dataset.index[i]] = dataset.iloc[i]
        haftaIci["HKI"][i] = hki
    else :
        haftaSonu.loc[dataset.index[i]] = dataset.iloc[i]
        haftaSonu["HKI"][i] = hki
    # Yaz Kış İlkbahar Sonbahar Kontrolü
    if(int(tarih[0]) in [12,1,2]):
        kis.loc[dataset.index[i]] = dataset.iloc[i]
        kis["HKI"][i] = hki
    elif(int(tarih[0]) in [3,4,5]):
        ilkbahar.loc[dataset.index[i]] = dataset.iloc[i]
        ilkbahar["HKI"][i] = hki
    elif(int(tarih[0]) in [6,7,8]):
        yaz.loc[dataset.index[i]] = dataset.iloc[i]
        yaz["HKI"][i] = hki
    else:
        sonbahar.loc[dataset.index[i]] = dataset.iloc[i]
        sonbahar["HKI"][i] = hki

#Hafta içi HKİ Grafiği
plt.figure(figsize= (25,5))
# Çizgi grafiği çizdirelim.
haftaIci.plot(kind='line',x='Tarih',y='HKI')#plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi Seviyesi')
plt.xlabel('Tarih')
plt.title('Haftaiçi HKİ Grafik Değişimi')
plt.show()


#Hafta sonu HKİ Grafiği
plt.figure(figsize= (25,5))
# Çizgi grafiği çizdirelim.
haftaSonu.plot(kind='line',x='Tarih',y='HKI')#plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi Seviyesi')
plt.xlabel('Tarih')
plt.title('Haftasonu HKİ Grafik Değişimi')
plt.show()


#yaz HKİ Grafiği
plt.figure(figsize= (25,5))
# Çizgi grafiği çizdirelim.
yaz.plot(kind='line',x='Tarih',y='HKI')#plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi Seviyesi')
plt.xlabel('Tarih')
plt.title('Yaz HKİ Grafik Değişimi')
plt.show()


#Kış HKİ Grafiği
plt.figure(figsize= (25,5))
# Çizgi grafiği çizdirelim.
kis.plot(kind='line',x='Tarih',y='HKI')#plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi Seviyesi')
plt.xlabel('Tarih')
plt.title('Kış HKİ Grafik Değişimi')
plt.show()


#Sonbahar HKİ Grafiği
plt.figure(figsize= (25,5))
# Çizgi grafiği çizdirelim.
sonbahar.plot(kind='line',x='Tarih',y='HKI')#plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi Seviyesi')
plt.xlabel('Tarih')
plt.title('Sonbahar HKİ Grafik Değişimi')
plt.show()

#İlkbahar HKİ Grafiği
plt.figure(figsize= (25,5))
# Çizgi grafiği çizdirelim.
ilkbahar.plot(kind='line',x='Tarih',y='HKI')#plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi Seviyesi')
plt.xlabel('Tarih')
plt.title('İlkbahar HKİ Grafik Değişimi')
plt.show()