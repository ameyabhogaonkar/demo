#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('E:\python-ethans\Pandas-Practise\Weather_data3.csv')
df


# In[5]:


df1=pd.melt(df, id_vars=['day'])
df1


# In[10]:


df1=pd.melt(df,id_vars=['day'],var_name='city',value_name='temp')
df1[df1['variable']=='paris']  #we can filter on specific name


# In[11]:


df1=pd.melt(df,id_vars=['day'],var_name='city',value_name='temp')
df1


# In[ ]:




