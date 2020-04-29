#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_excel('E:\python-ethans\Pandas-Practise\survey.xls')
df


# In[3]:


pd.crosstab(df.Nationality,df.Handedness)


# In[7]:


pd.crosstab(df.Handedness,df.Sex,margins=True) #margins will give you total


# In[9]:


pd.crosstab(df.Handedness,[df.Sex,df.Nationality],margins=True)# you can pass mutiple rows/columns by making array


# In[10]:


import numpy as np

pd.crosstab(df.Handedness,df.Sex,values=df.Age,aggfunc=np.average) #to get avergae age of male anf female with left and right


# In[11]:


pd.crosstab(df.Handedness,df.Sex,normalize='index') #to get average of male n female


# In[ ]:





# In[ ]:





# In[ ]:




