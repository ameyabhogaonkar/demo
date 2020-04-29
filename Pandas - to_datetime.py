#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

dates = ['2017-01-05', '5 jan 2017','2017/01/05','05 jan 2017','2017.01.05']

pd.to_datetime(dates)


# In[5]:


pd.to_datetime('5/1/2017',dayfirst=True) #to handle europe date we need argument daytrue=True


# In[9]:


pd.to_datetime('5$1$2017',format='%d$%m$%Y')


# In[11]:


dates = ['2017-01-05', '5 jan 2017','2017/01/05','05 jan 2017','2017.01.05','abc']

pd.to_datetime(dates,errors='ignore') #'ignore' will ignore error but also not perform the conversion


# In[12]:


dates = ['2017-01-05', '5 jan 2017','2017/01/05','05 jan 2017','2017.01.05','abc']

pd.to_datetime(dates,errors='coerce') #'coerce' will make invalid string to NaT(not a timestamp) and perform conversion


# In[19]:


t = 1058694752   
dt = pd.to_datetime([t],unit='s') #Epoch time converter
dt


# In[17]:


dt.view('int64')

