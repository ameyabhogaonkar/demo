#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
weather_data ={
    'day' : ['1/1/2001','1/1/2002','1/1/2003','1/1/2004','1/1/2005'],
    'temp' : [22,54,44,78,33],
    'windspeed': [4,6,7,1,2],
    'event' : ['rainy','summer','rainy','winter','rainy']
}
index = {'a','b','c','d','e'}
df = pd.DataFrame(weather_data,index)
df


# In[2]:


df.shape


# In[4]:


df.head(2)


# In[5]:


df[1:4]


# In[6]:


df[:3]


# In[7]:


df.columns


# In[9]:


df.row


# In[11]:


df['day']


# In[12]:


type(df['day'])


# In[13]:


df[['day','temp']]


# In[14]:


df['temp'].max()


# In[15]:


df.describe()


# In[16]:


df[df.temp>50]


# In[17]:


df['day'][df.temp>50]


# In[18]:


df.count()


# df1 = df.set_index('day')

# In[23]:


df.set_index('day')


# In[31]:


df


# In[42]:


import pandas as pd
def convert(cell):
    if cell=="HR":
        return 'BDE'
    return cell
df = pd.read_csv('E:\python-ethans\Pandas-Practise\BSE.csv',converters = {
    'dept': convert
})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




