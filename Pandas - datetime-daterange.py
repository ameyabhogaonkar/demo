#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df = pd.read_csv('E:\python-ethans\Pandas-Practise\BSE-BOM504067.csv',parse_dates=['Date'],index_col= 'Date')
df.head(5)


# In[9]:


df.index


# In[12]:


df['2020']


# In[14]:


df['2020'].Close.mean()  #if we want average of Close prices for year 2020


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('M').mean()


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
df['2019'].Close.resample('Q').mean().plot(kind='bar')


# In[31]:


import pandas as pd

df= pd.read_csv("E:\python-ethans\Pandas-Practise\BSE.csv")
df


# In[37]:


dg = pd.date_range(start ='4/1/2020',end='4/15/2020',freq='B')
dg


# In[38]:


df.set_index(dg,inplace=True)
df


# In[40]:


df.asfreq('D',method='pad') #'pad' padding method will give you data for weekend and it take data from last working day


# In[ ]:





# In[ ]:





# In[ ]:




