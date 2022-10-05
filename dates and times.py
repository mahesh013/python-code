#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
a


# In[2]:


a='2.4'


# In[5]:


b=float(a)


# # Dates and times

# In[6]:


from datetime import datetime,date,time


# In[7]:


dt=datetime(2011,10,29,20,30,21)


# In[8]:


type(dt)


# In[9]:


dt


# In[12]:


dt.date()


# In[13]:


dt.time()


# In[22]:


dt.month


# In[24]:


dt.ctime()


# In[27]:


dt.hour


# In[29]:


dt.strftime('%m/%d/%Y %H:%M')


# In[30]:


dt.strftime('%D %H:%M')


# In[32]:


dt.strptime('20091031','%Y%m%d')


# In[33]:


dt.replace(minute=0,second=0)


# In[8]:


from datetime import datetime,date,time
dt=datetime(2011,10,29,20,30,21)

dt2=datetime(2011, 11, 15, 22, 30)


# In[9]:


delta = dt2 - dt


# In[10]:


delta


# In[11]:


type(delta)


# In[12]:


dt


# In[13]:


dt+delta


# In[ ]:





# In[14]:


from datetime import datetime,date,time


# In[15]:


dt=datetime(2012,6,25,11,22,34)


# In[16]:


dt


# In[18]:


type(dt)


# In[20]:


dt.astimezone()


# In[25]:


dt.ctime()


# In[27]:


dt.date()


# In[28]:


dt.day


# In[33]:


dt.fold


# In[39]:


dt.hour


# In[41]:


dt.isocalendar()


# In[42]:


dt.isoformat()


# In[1]:


dt.strftime('%m/%d/%Y %H:%M')


# In[2]:


from datetime import datetime,date,time


# In[3]:


dt=datetime(2012,6,25,11,22,34)


# In[4]:


dt.strftime('%m/%d/%Y %H:%M')


# In[7]:


dt.strftime('%m/%d/%Y %I:%M:%S')


# In[ ]:




