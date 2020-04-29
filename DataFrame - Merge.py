#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

df1 = pd.DataFrame({
    'city' : ['pune','mumbai','amravati','delhi'],
    'temp' : [35,40,45,20]
})
df1


# In[28]:


df2 = pd.DataFrame({
    'city' : ['pune','mumbai','amravati','bombay'],
    'humidity' : [5,4,1,7]
})
df2


# In[31]:


df3=pd.merge(df1,df2,on='city',how='outer',indicator='True')
df3


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




