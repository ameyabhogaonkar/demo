#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
df = pd.read_csv('E:\python-ethans\Pandas-Practise\BSE-BOM504067.csv')
print(df.head(5))


# In[17]:


import pandas as pd
df = pd.read_csv('E:\python-ethans\Pandas-Practise\BSE-BOM504067.csv')
#print(df.head(5))
print(df.head(5)['High'].min())


# In[12]:


df.head(5)['Date'][df['No. of Shares'] < 1000]


# In[14]:


df.head(5)['Total Turnover'].mean()


# In[52]:


import pandas as pd
df = pd.read_excel('E:\python-ethans\Pandas-Practise\emp.xlsx',names =['name','city','sal','age','dept'],index ={'a','b','c','d','e'})
print(df)


# In[32]:


df = pd.read_excel('E:\python-ethans\Pandas-Practise\emp.xlsx',nrows=2,names =['name','city','sal','age','dept'])
print(df)


# In[47]:


df.to_csv('E:\python-ethans\Pandas-Practise\BSE.csv',header=True)


# In[43]:


df.columns


# In[45]:


print(df)


# In[ ]:




