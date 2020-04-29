#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df = pd.read_excel('E:\python-ethans\Pandas-Practise\stocks.xlsx',header=[0,1],)
df


# In[18]:


df1=df.stack
df1


# In[8]:


df2 = df.stack(level=0)
df2


# In[22]:


df3=df1.unstack()
df3

