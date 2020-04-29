#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('E:\python-ethans\Pandas-Practise\Weather_data.csv')
df


# In[10]:


group = df.groupby('city')
group1 = df.groupby('event')
group1
group


# In[21]:


min_wage = pd.DataFrame()
for name,group in df.groupby('city'):
    if min_wage.empty:
        min_wage = group.set_index('temp')[['event']].rename(columns={'event':name})
    else:
        min_wage = min_wage.join(group.set_index('temp')[['event']].rename(columns={'event':name}))
min_wage.head()
        


# In[6]:


for city,city_df in group:
    print(city)
    print(city_df)


# In[11]:


for event,event_df in group1:
    print(event)
    print(event_df)


# In[12]:


group.get_group('mumbai')


# In[13]:


group.max()


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
group1.plot()


# In[ ]:




