#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup=(1,4,5)
tup


# In[4]:


nested_tup=(2,3,4),(7,8,9)
nested_tup


# In[5]:


tup=tuple("mahesh")
tup


# In[2]:


tup=(1,4,4,2,5,7,8)
tup.count(4)


# In[19]:


list=['mahesh','raj',1]
list


# In[10]:


list.append('shivam')
list


# In[20]:


list.insert(1,'sanket')
list


# In[21]:


list.pop(1)


# In[22]:


list


# In[23]:


list.append('sarthak')


# In[24]:


list


# In[25]:


list.remove('sarthak')


# In[26]:


list


# In[28]:


'mahesh' in list


# In[31]:


a=[9,6,8,5,2,1,3]
a.sort()
a


# In[32]:


b=['mahesh','ab','bcdddd','alki']
b.sort(key=len)
b


# In[12]:


import bisect


# In[42]:


d=[1,2,4,5,6,78,99]


# In[43]:


bisect.bisect(d,2)
d


# In[44]:


bisect.insort(d,6)
d


# In[5]:


sorted([9,7,4,6,1,2,3])


# In[7]:


sorted('mahesh kandekar')


# In[6]:


a=('a','b','c')
b=('apple','boll','cat')
zipped=zip(a,b)
print(zipped)


# In[7]:


import bisect
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
c=zip(seq1, seq2)
print(c)


# # list method

# In[2]:


a=[2,7,9,6,5,4]


# In[6]:


a.count(2)


# In[3]:


a.insert(1,10)
a


# In[6]:


a.reverse()
a


# In[12]:


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


# In[13]:


filtered_data


# In[17]:


import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'


# # Reading or writing file

# In[22]:


f=open('work','w')
"hello"


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




