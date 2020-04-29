#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

india =pd.DataFrame({
    "city" : ['pune','mumbai','delhi','chennai'],
    "temp" : [40,45,30,35],
    "humidity" : [20,23,30,35]
})
india


# In[22]:


import pandas as pd

usa =pd.DataFrame({
    "city" : ['newyork','washington','lasvegas','penny','pune'],
    "temp" : [22,31,29,35,40],
    "humidity" : [20,10,30,35,20]
})
usa


# In[30]:


df = pd.concat([india,usa],ignore_index=True)
df


# In[29]:


df = pd.concat([india,usa],ignore_index =True).drop_duplicates().reset_index(drop=True)
df


# In[11]:


df = pd.concat([india,usa], keys=['ind','us'])
df


# In[12]:


df.loc['us']


# In[18]:


wind_df =pd.DataFrame({
    "city" : ['mumbai','pune','delhi','chennai'],
    "wind" : [4,8,1,7]
},index=[1,0,2,3])  #we can use index in case of mismatch of index
wind_df


# In[19]:


df = pd.concat([india,wind_df],axis = 1)
df


# In[20]:


s = pd.Series(['humid','rainy','sunny','winter'],name= 'event')
s


# In[21]:


df = pd.concat([india,s],axis=1)
df


# In[ ]:




