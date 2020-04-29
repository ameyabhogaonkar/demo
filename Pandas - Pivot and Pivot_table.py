#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

df = pd.read_csv('E:\python-ethans\Pandas-Practise\Weather_data.csv')
df


# In[8]:


df.pivot(index='date',columns = 'city',values='event')


# In[9]:


df1 = pd.read_csv('E:\python-ethans\Pandas-Practise\Weather_data2.csv')
df1


# In[11]:


df1.pivot_table(index = 'city',columns = 'date')


# In[14]:


type(df1['date'][0])


# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


df1['date']=pd.to_datetime(df1['date'])
df1


# In[17]:


type(df1['date'][0])


# In[18]:


df1.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')

