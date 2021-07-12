#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sb

fmri = sb.load_dataset('fmri')
fmri.head()


# In[15]:


fmri.info()


# In[25]:


sb.relplot(x='timepoint',y='signal',data=fmri.head(150),hue='subject',style='region')


# In[30]:


sb.catplot(x='timepoint',y='signal',data=fmri.head(150),hue='subject')


# In[31]:


sb.catplot(x='timepoint',y='signal',data=fmri.head(150),hue='subject',kind='swarm')


# In[32]:


sb.catplot(x='timepoint',y='signal',data=fmri.head(150),hue='subject',kind='strip')


# In[35]:


sb.catplot(x='timepoint',y='signal',data=fmri,hue='subject',kind='box')


# In[18]:


sb.catplot(x='timepoint',y='signal',data=fmri,hue='subject',kind='boxen')


# In[ ]:





# In[ ]:




