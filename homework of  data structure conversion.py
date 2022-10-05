#!/usr/bin/env python
# coding: utf-8

# In[5]:


# list of list
a=[['mahesh','kandekar'],['shivam','amit']]
a
# list of tuple
b=[(2,3,4,5)]
b
# list of dict

# tuple of list
c=(['a','b','c'])
c
# tuple of tuple
d=((1,2,3,4,5,6))
d
# tuple of dict
data=({1:'mahesh',2:'sanket',
      3:'shubham',4:'harshad'})
data


f
# dict of list
# dict of tuple


# In[2]:


# create a list using a dictionary
# create a dictionary using list
data=[{1:'mahesh',2:'sanket',
      3:'shubham',4:'harshad'}]
data


# In[4]:


# create a dictionary using list
dict={}
dict['mahesh']=[1,2]
dict['sanket']=[3,4,5]
dict


# In[4]:


# find out regular expreesion  for email id ,phone no,zip codes,dates,dbirth


# In[5]:


import re
str='Hello my name is mahesh kandekar and my email address is kandekarmahesh6@gmail.com and my phone number is 8080810575 and birth date is 13/05/2001 and zip code is 422611'


# In[7]:


email=re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",str)
for mail in email:
    print(mail)


# In[2]:


a={'apple':1,"mango":2}
b={'orange':3}
e={a,b}


# In[5]:


# tuple of list
a=[1,2,3]
b=[4,5,6]
c=([1,2,3],[4,5,6])
c


# In[6]:


# list of list
a=[1,2,3]
b=[4,5,6]
c=[[1,2,3],[4,5,6]]
c


# In[8]:


# tuple of tuple
a=(1,2,3)
b=(4,5,6)
c=((1,2,3),(4,5,6))
c


# In[4]:


# tuple of dictionary
# d1={'k':1,2,3}
# d2={'k2':4,5,6}
d=({'k1':1},{'k2':4})
d


# In[ ]:





# In[9]:


# dictionary of dictionary
d1={'k1':1}
d2={'k2':4}
{'a':d1,'b':d2 }


# In[ ]:




