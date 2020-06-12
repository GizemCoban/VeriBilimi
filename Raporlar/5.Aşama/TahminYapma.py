# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:07:36 2020

@author: Gizem Çoban
"""

from flask import Flask,render_template,redirect,url_for,request
from gevent.pywsgi import WSGIServer
import tensorflow.keras
from tensorflow.keras.models import model_from_json
import pandas as pd
import datetime
import random
import numpy as np
import json
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
MODEL_PATH='model.h5'

#kaydedilmiş modeli yükle
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(MODEL_PATH)

print("Model Yüklendi")

def model_predict(model):
   
    preds=model.predict_classes([[14]])#predict([[0,0,0,0,0,0,0,0,0,0,0]])
    print(preds)
    return str(preds[0])

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
    
@app.route ('/',methods=['GET'])
def index():

   return "Hello Word" 


   
@app.route ('/analiz',methods=['GET'])
def analiz():
    
    yazOrt = yaz.mean().to_json()
    kisOrt=kis.mean().to_json()
    ilkOrt=ilkbahar.mean().to_json()
    sonOrt=sonbahar.mean().to_json()
    haftaiciOrt=haftaIci.mean().to_json()
    haftasonuOrt=haftaSonu.mean().to_json()        
    res = {"yaz":yazOrt,"kis":kisOrt, "ilkbahar":ilkOrt,"sonbahar":sonOrt, "haftasonu":haftasonuOrt,"haftaici":haftaiciOrt}
    return res 
@app.route ('/test',methods=['GET'])
def test():
    preds=model_predict(loaded_model)
    return preds
    
if __name__=='__main__':
    app.run()
    http_server=WSGIServer(('',5000),app)
    http_server.serve_forever()