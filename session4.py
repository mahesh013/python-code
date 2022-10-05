#!/usr/bin/env python
# coding: utf-8

# # bool

# In[1]:


True and True


# In[2]:


False and True


# In[3]:


bool(1)


# In[4]:


bool(4)


# In[5]:


bool(0)


# In[6]:


bool('mahesh')


# In[7]:


bool('')


# In[8]:


bool([])


# In[10]:


bool([1,2,3])


# # None

# In[12]:


a=None
a is None


# In[13]:


b=5
b is not None


# In[14]:


def sum(a,b):
    c=a+b
    print(c)
sum(2,5)


# In[14]:


def add_and_maybe_multiply(a,b,c=None):
        result=a+b
        if c is not None:
            result=result*c
        
        return result

add_and_maybe_multiply(5,10,10)


# # Type casting

# In[24]:


s='3.14'


# In[32]:


type(s)


# In[33]:


b=float(s)


# In[35]:


print(b)


# In[27]:


type(b)


# In[37]:


i=int(b)


# In[3]:


print(i)


# In[40]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




