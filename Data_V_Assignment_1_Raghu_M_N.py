#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


# Assignment
x=np.arange(0,10)
y=x*x
plt.title('Explonation',color='b')
plt.plot(x,y,'r--')
plt.xlabel('X-axis',color='g')
plt.ylabel('Y-axis',color='g')


# In[8]:


days = [1,2,3,4,5,6,7] # number of days
sales = [160,150,140,145,175,165,180] #sales of arcessponding day
plt.plot(days,sales,'g*--')
plt.title('Sales Line graph of store x',color='c')
plt.xlabel('Days',color='b')
plt.ylabel('Sales',color='b')


# In[9]:


days = [1,2,3,4,5,6,7] # number of days
sales_1 = [160,150,140,145,175,165,180] #sales of company 1
sales_2 = [70,90,160,150,140,145,175]

plt.subplot(1,3,1)
plt.plot(days,sales_1,'ko--')
plt.title('Line graph of company1',color='g')
plt.xlabel('Days',color='m')
plt.ylabel('Sales@1',color='m')

plt.subplot(1,3,3)
plt.plot(days,sales_2,'r*--')
plt.title('Line graph of company2',color='b')
plt.xlabel('Days',color='m')
plt.ylabel('Sales@2',color='m')


# In[ ]:




