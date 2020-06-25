# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:45:23 2020

@author: Gizem ÇOBAN
"""
# Kullanılacak kütüphanelerin import edilmesi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data/data1.csv', encoding = 'iso-8859-9') 


dataset=dataset.fillna(method ='pad') # NaN olan dayayı bir önceki data ile günceller
dataset=dataset.fillna(method ='bfill') # NaN olan datayı bir sonraki data ile günceler

yeniData=np.empty([365, 12], dtype=object)

i=0


for i in range (365):
    yeniData[i][0] = dataset["Tarih"][i]
    yeniData[i][1] = (dataset["PM10"][i] + dataset["PM10.1"][i] + dataset["PM10.2"][i] + dataset["PM10.3"][i]+dataset["PM10.4"][i]+dataset["PM10.5"][i]+dataset["PM10.6"][i]+dataset["PM10.7"][i]+dataset["PM10.8"][i]+dataset["PM10.9"][i]+dataset["PM10.10"][i]+dataset["PM10.11"][i])/12
    yeniData[i][2]= (dataset["PM10Debi"][i] + dataset["PM10Debi.1"][i] + dataset["PM10Debi.2"][i] + dataset["PM10Debi.3"][i]+dataset["PM10Debi.4"][i]+dataset["PM10Debi.5"][i]+dataset["PM10Debi.6"][i]+dataset["PM10Debi.7"][i]+dataset["PM10Debi.8"][i]+dataset["PM10Debi.9"][i]+dataset["PM10Debi.10"][i])/11
    yeniData[i][3]= (dataset["SO2"][i] + dataset["SO2.1"][i] + dataset["SO2.2"][i]+dataset["SO2.4"][i]+dataset["SO2.5"][i]+dataset["SO2.6"][i]+dataset["SO2.7"][i]+dataset["SO2.8"][i]+dataset["SO2.9"][i])/9
    yeniData[i][4]= (dataset["NO2"][i] + dataset["NO2.1"][i] + dataset["NO2.2"][i] + dataset["NO2.3"][i]+dataset["NO2.4"][i]+dataset["NO2.5"][i]+dataset["NO2.6"][i]+dataset["NO2.7"][i]+dataset["NO2.8"][i]+dataset["NO2.9"][i]+dataset["NO2.10"][i]+dataset["NO2.11"][i]+dataset["NO2.12"][i])/13
    yeniData[i][5]= (dataset["NOX"][i] + dataset["NOX.1"][i] + dataset["NOX.2"][i] + dataset["NOX.3"][i]+dataset["NOX.4"][i]+dataset["NOX.5"][i]+dataset["NOX.6"][i]+dataset["NOX.7"][i]+dataset["NOX.8"][i]+dataset["NOX.9"][i]+dataset["NOX.10"][i]+dataset["NOX.11"][i]+dataset["NOX.12"][i])/13
    yeniData[i][6]= (dataset["NO"][i] + dataset["NO.1"][i] + dataset["NO.2"][i] + dataset["NO.3"][i]+dataset["NO.4"][i]+dataset["NO.5"][i]+dataset["NO.6"][i]+dataset["NO.7"][i]+dataset["NO.8"][i]+dataset["NO.9"][i]++dataset["NO.10"][i]+dataset["NO.11"][i]+dataset["NO.12"][i])/13
    yeniData[i][7]= (dataset["O3"][i] + dataset["O3.1"][i] + dataset["O3.2"][i] + dataset["O3.3"][i]+dataset["O3.4"][i]+dataset["O3.5"][i]+dataset["O3.6"][i]+dataset["O3.7"][i])/8
    yeniData[i][8]= (dataset["HavaSicakligi"][i] + dataset["HavaSicakligi.1"][i] + dataset["HavaSicakligi.2"][i] + dataset["HavaSicakligi.3"][i]+dataset["HavaSicakligi.4"][i]+dataset["HavaSicakligi.5"][i]+dataset["HavaSicakligi.6"][i]+dataset["HavaSicakligi.7"][i]+dataset["HavaSicakligi.8"][i]+dataset["HavaSicakligi.9"][i]+dataset["NOX.10"][i])/11
    yeniData[i][9]= (dataset["RuzgarHizi"][i] + dataset["RuzgarHizi.1"][i] + dataset["RuzgarHizi.2"][i] + dataset["RuzgarHizi.3"][i]+dataset["RuzgarHizi.4"][i]+dataset["RuzgarHizi.5"][i]+dataset["RuzgarHizi.6"][i]+dataset["RuzgarHizi.7"][i]+dataset["RuzgarHizi.8"][i]+dataset["RuzgarHizi.9"][i]+dataset["RuzgarHizi.10"][i])/11
    yeniData[i][10]= (dataset["BagilNem"][i] + dataset["BagilNem.1"][i] + dataset["BagilNem.2"][i] + dataset["BagilNem.3"][i]+dataset["BagilNem.4"][i]+dataset["BagilNem.5"][i]+dataset["BagilNem.6"][i]+dataset["BagilNem.7"][i]+dataset["BagilNem.8"][i]+dataset["BagilNem.9"][i])/10
    yeniData[i][11]= (dataset["HavaBasinc"][i] + dataset["HavaBasinc.1"][i] + dataset["HavaBasinc.2"][i] + dataset["HavaBasinc.3"][i]+dataset["HavaBasinc.4"][i]+dataset["HavaBasinc.5"][i]+dataset["HavaBasinc.6"][i]+dataset["HavaBasinc.7"][i]+dataset["HavaBasinc.8"][i]+dataset["HavaBasinc.9"][i]+dataset["HavaBasinc.10"][i])/11
    
datasetYeni = pd.DataFrame(yeniData,columns=["Tarih","PM10","PM10Debi","SO2","NO2","NOX","NO","O3","HavaSicakligi","RuzgarHizi","BagilNem","HavaBasinc"])
    
datasetYeni.to_csv(r'data/HavaKalitesi.csv', index = False)    
     
    
    
     
     
