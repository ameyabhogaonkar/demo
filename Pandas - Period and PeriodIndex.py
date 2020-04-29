#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

year = pd.Period('2016')
year
month = pd.Period('2016-1',freq='M')
month


# In[2]:


dir(year)


# In[7]:


year.start_time
year.end_time


# In[11]:


month + 1


# In[12]:


year + 1


# In[13]:


hour =pd.Period('2016-1-31 22:00:00',freq='H')
hour


# In[15]:


hour - 1
hour + 1


# In[21]:


quarter = pd.Period('2017Q1')
quarter1 = pd.Period('2017Q1',freq = 'Q-JAN') #For fiscal year when it start at different month

quarter1


# In[22]:


quarter + 1
quarter1.start_time


# In[25]:


quarter.asfreq('M',how='end')


# In[30]:


idx = pd.period_range('2011','2017',freq='Q-Jan')
idx


# In[32]:


idx[0].start_time


# In[34]:


idx1 = pd.period_range('2011',periods=5,freq='Q-Jan')
idx1


# In[42]:


import pandas as pd

df = pd.read_csv('E:\python-ethans\Pandas-Practise\wallmart.csv')
df


# In[56]:


df = pd.reset_index(drop=True)
df


# In[50]:


df.index


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




