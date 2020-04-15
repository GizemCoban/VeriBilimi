# -*- coding: utf-8 -*-
# Kullanılacak kütüphanelerin import edilmesi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data/HavaKalitesi.csv', encoding = 'iso-8859-9') 

plt.figure(figsize= (10,5))
# Çizgi grafiği çizdirelim.
dataset.plot(kind = 'line', xticks=np.arange(0,12), rot =45)
plt.ylabel('Hava Kalitesi')
plt.show()
