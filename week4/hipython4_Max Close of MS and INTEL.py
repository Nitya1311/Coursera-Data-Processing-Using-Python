# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:12:38 2017

@author: Xinyu Li
"""

import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
start = datetime(2014,1,1)
end = datetime(2014,12,31)
quotesMSFT = quotes_historical_yaho_ochl('MSFT', start, end)
quotesINTC = quotes_historical_yahoo_ochl('INTC', start, end)
fields = ['date','open','close','high','low','volume']
#quotesdf = pd.DataFrame(quotes, columns = fields)
#quotesdf = pd.DataFrame(quotes, index = range(1,len(quotes)+1),columns = fields)
list1 = []
for i in range(0,len(quotesMSFT)):
    x = date.fromordinal(int(quotesMSFT[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
#print list1
list2 = []
for i in range(0,len(quotesINTC)):
    x = date.fromordinal(int(quotesINTC[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list2.append(y)
quotesmsftdf = pd.DataFrame(quotesMSFT, index = list1, columns = fields)
quotesmsftdf = quotesmsftdf.drop(['date'], axis = 1)
#print quotesdf
quotesintcdf = pd.DataFrame(quotesINTC, index = list1, columns = fields)
quotesintcdf = quotesintcdf.drop(['date'], axis = 1)
listtemp1 = []
for i in range(0,len(quotesmsftdf)):
    temp = time.strptime(quotesmsftdf.index[i],"%Y-%m-%d")
    listtemp1.append(temp.tm_mon)
listtemp2 = []
for i in range(0,len(quotesintcdf)):
    temp = time.strptime(quotesintcdf.index[i],"%Y-%m-%d")
    listtemp2.append(temp.tm_mon)
tempmsftdf = quotesmsftdf.copy()
tempmsftdf['month'] = listtemp1
closemaxMSFT = tempmsftdf.groupby('month').max().close
listMSFT = []
for i in range(1,13):
    listMSFT.append(closemaxMSFT[i])
listMSFTIndex = closemaxMSFT.index    
tempintcdf = quotesintcdf.copy()
tempintcdf['month'] = listtemp2
closemaxINTC = tempintcdf.groupby('month').max().close
listINTC = []
for i in range(1,13):
    listINTC.append(closemaxINTC[i])
listINTCIndex = closemaxINTC.index 
pl.subplot(211)
plt.plot(listMSFTIndex,listMSFT,color='r',marker='o')
pl.subplot(212)
plt.plot(listINTCIndex,listINTC,color='green',marker='o')