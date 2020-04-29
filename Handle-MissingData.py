#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
df = pd.read_excel('E:\python-ethans\Pandas-Practise\missing.xlsx')

index = {0,1,2,3,4,}

df=pd.DataFrame(df,index)
df


# In[24]:


new_df = df.fillna(0)
new_df


# In[26]:


new_df = df.fillna({
    'city': 'No city',
    'age': 0
})
new_df


# In[27]:


new_df = df.interpolate()
new_df


# In[34]:



import numpy as np
new_df = df.replace('IT',np.NaN)
new_df


# In[35]:


new_df = df.replace(['amt','london','tokyo'],['pune','mumbai','delhi'])
new_df


# In[36]:


df = pd.DataFrame({
    'score' : ['good','better','good','best'],
    'strudents' : ['rob','mack','peter','paul']
})
df


# In[38]:


new = df.replace(['good','better','good','best'],[2,4,2,5])
new

