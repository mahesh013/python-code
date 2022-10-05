#!/usr/bin/env python
# coding: utf-8

# # Numpy-

# In[5]:


# Stands for Numerical python and is the core of library for numeric
# and scientific computing


# In[ ]:





# In[4]:


import numpy as np
a=np.array([1,2,3])


# In[5]:


a


# In[6]:


type(a)


# In[7]:


b=np.array((4,5,6))


# In[8]:


b


# In[ ]:





# In[9]:


type(b)


# # Initializing Numpy Array with zero

# In[10]:


x=np.zeros((3,4))


# In[11]:


x


# In[12]:


x=np.zeros((4,4))


# In[13]:


x


# In[14]:


x=np.ones((3,4),dtype=int)


# In[15]:


x


# In[16]:


x=np.ones((3,4))


# In[17]:


x


# In[18]:


x=np.full((3,4),0.11)


# In[19]:


x


# In[20]:


x=np.arange(10,30,5)


# In[21]:


x


# In[22]:


x=np.linspace(0,5/3,6)


# In[23]:


x


# In[24]:


x=np.linspace(1,6,6)


# In[25]:


x


# In[26]:


x=np.random.rand(2,3)


# In[27]:


x


# In[28]:


x=np.empty((2,3))


# In[29]:


x


# In[30]:


a.ndim


# In[31]:


a.size


# In[32]:


x.size


# In[33]:


x.shape


# In[34]:


x.dtype


# In[35]:


a.dtype


# In[36]:


a=np.arange(6)
print(a)


# In[37]:


b=a.reshape(2,3)


# In[38]:


print(b)


# In[39]:


b=a.reshape(1,6)


# In[40]:


print(b)


# In[41]:


a=np.array([1,5,3,19,13,7,3])


# In[42]:


a[3]


# In[43]:


a[2:5]


# In[44]:


a[2::2]


# In[45]:


a[::-1]


# In[46]:


a=np.array([1,2,5,7,8])
a[1:3]=-1


# In[47]:


a


# In[48]:


a=[1,2,5,7,8]


# In[49]:


a[1:3]=-1


# In[50]:


a=np.array([1,2,5,7,8])
a_slice=a[1:5]
a_slice[1]=1000


# In[51]:


a


# In[52]:


another_slice=a[2:6].copy


# In[53]:


a=np.array([1,2,5,7,8])
another_slice=a[2:6].copy
a_slice[1]=1000


# In[54]:


a


# In[59]:


a=np.arange(12).reshape(3,4)
rows_on=np.array([True,False,True])
a[rows_on , :]


# In[62]:


cols_on=[True,False,True,False]


# In[63]:


a[:,cols_on]


# In[64]:


import numpy as np


# In[65]:


a=np.array([10,20,30,40])


# In[66]:


b=np.arange(4)


# In[67]:


a


# In[68]:


b


# # addition

# In[69]:


c=a+b


# In[70]:


c


# # substraction

# In[71]:


d=a-b


# In[72]:


d


# # multiplication

# In[73]:


e=a*b


# In[74]:


e


# # brodcasting

# In[75]:


h=np.arange(5).reshape(1,1,5)


# In[76]:


h


# In[77]:


h.ndim


# In[78]:


h+[10,20,30,40,50]


# In[ ]:


# 2 rule


# In[79]:


np.arange(3)


# In[80]:


np.arange(3)+5


# In[84]:


np.ones((3,3))


# In[86]:


np.ones((3,3))+np.arange(3)


# In[87]:


np.ones((3,3))+np.arange(9).reshape(3,3)


# In[90]:


np.arange(9)


# In[91]:


np.arange(9).reshape(3,3)


# In[92]:


np.ones((3,3))+np.arange(9).reshape(3,3)


# In[93]:


np.arange(3).reshape(3,1)


# In[94]:


np.arange(3).reshape(3,1)+np.arange(3)


# In[95]:


k=np.arange(6).reshape(2,3)


# In[96]:


k


# In[98]:


k+[100,200,300]


# # some other

# In[101]:


a=np.array([10,20,30,40])


# In[102]:


a


# In[103]:


a.tolist()


# # Flatten

# In[104]:


# flattern from higher to lower diamension


# In[105]:


a=np.array(range(6),float).reshape((2,3))


# In[106]:


a


# In[107]:


a.flatten()


# # CONCAT

# In[111]:


a=np.array([1,2],float)
b=np.array([3,4,5],float)
c=np.array([6,7,8],float)


# In[112]:


np.concatenate((a,b,c))


# In[113]:


np.concatenate([a,b,c])


# In[114]:


a=np.array([[1,2],[3,4]],float)
b=np.array([[5,6],[7,8]],float)




# In[115]:


a


# In[116]:


b


# In[117]:


np.concatenate((a,b))


# In[118]:


np.concatenate((a,b),axis=0)


# In[119]:


np.concatenate((a,b),axis=1)


# In[123]:


# NEW AXIS


# In[130]:


a=np.array((1,2,3))


# In[131]:


a[:,np.newaxis]


# In[132]:


a[:,np.newaxis].shape


# In[133]:


a.shape


# In[134]:


b


# In[135]:


b.flatten()[:,np.newaxis]


# # zeros_like and onces_like

# In[1]:


import numpy as np


# In[2]:


a=np.array([[1,2,3],[4,5,6]],float)


# In[3]:


a


# In[4]:


np.zeros_like(a)


# In[6]:


np.ones_like(a)


# In[7]:


np.identity(4,dtype=float)


# In[8]:


np.eye(4,k=1,dtype=float)


# In[9]:


np.eye(4,k=2,dtype=float)


# In[12]:


a=np.array([1,4,9],float)


# In[13]:


np.sqrt(a)


# In[15]:


a=np.array([1.1,1.5,1.9],float)


# In[16]:


np.floor(a)


# In[17]:


np.ceil(a)


# In[18]:


np.rint(a)


# In[19]:


np.pi


# In[20]:


np.e


# In[21]:


a=np.array([[1,2],[3,4],[5,6]],float)


# In[23]:


for i in a:
    print(i)


# In[26]:


a=np.array([2,4,3],float)


# In[27]:


a.sum()


# In[28]:


np.sum(a)


# In[29]:


np.prod(a)


# In[30]:


np.subtract(a,a)


# In[31]:


a.mean()


# In[32]:


np.mean(a)


# In[33]:


a.var()


# In[34]:


a.std()


# In[35]:


a.min()


# In[38]:


a.max()


# In[40]:


a.argmin()


# In[42]:


a.argmax()


# In[44]:


a=np.array([[0,2],[3,-1],[3,5]],float)


# In[45]:


a


# In[46]:


a.mean()


# In[47]:


a.mean(axis=1)


# In[48]:


a.mean(axis=0)


# In[50]:


a.max(axis=0)


# In[54]:


a=np.array([1,1,4,5,5,5,7],float)


# In[55]:


a


# In[56]:


np.unique(a)


# In[60]:


a=np.array([[1,2],[3,4]],float)


# In[61]:


a.diagonal()


# In[63]:


a=np.array([1,3,0],float)
b=np.array([0,3,2],float)


# In[64]:


a>b


# In[65]:


a==b


# In[66]:


a<=b


# In[67]:


a>=b


# In[68]:


a>b


# In[79]:


a=np.array([True,False,False],bool)
b=np.array([True,False,True],bool)
c=np.array([False,True,False],bool)


# In[80]:


any(a)


# In[81]:


all(a)


# In[82]:


a=np.array([1,3,0],float)


# In[83]:


np.logical_and(a>0,a<3)


# In[84]:


np.logical_not(b)


# In[85]:


np.logical_or(b,c)


# In[86]:


a=np.array([1,3,0],float)


# In[87]:


np.where(a>0,3,2) #


# In[88]:


a=np.array([[0,1],[3,0]],float)


# In[89]:


a


# In[90]:


a.nonzero()


# In[91]:


a=np.array([1,np.NaN,np.Inf],float)


# In[92]:


a


# In[93]:


np.isnan(a)


# In[94]:


np.isfinite(a)


# In[95]:


a=np.array([[6,4],[5,9]],float)


# In[96]:


a>=6


# In[97]:


a[a>=6]


# In[98]:


a=np.array([[6,4],[5,9]],float)


# In[99]:


sel=(a>=6)


# In[100]:


a[sel]


# In[101]:


a[np.logical_and(a>5,a<9)]


# In[106]:


a=np.array([2,4,6,8],float)
b=np.array([0,0,1,3,2,1],int)


# In[107]:


a[b]


# In[111]:


a=np.array([[1,4],[9,6]],float)
b=np.array([0,0,1,1,0],int)
c=np.array([0,1,1,1,1],int)


# In[112]:


a


# In[113]:


a[b,c]


# In[115]:


a=np.array([2,4,6,8],float)
b=np.array([0,0,1,3,2,1],int)


# In[116]:


a.take(b)


# In[117]:


a=np.array([[0,1],[2,3]],float)


# In[118]:


a


# In[119]:


b=np.array([0,0,1],int)


# In[120]:


b


# In[121]:


a.take(b,axis=0)


# In[122]:


a.take(b,axis=1)


# In[123]:


a=np.array([0,1,2,3,4,5],float)


# In[124]:


b=np.array([9,8,7],float)


# In[125]:


a.put([0,3],b)


# In[126]:


a


# In[127]:


a=np.array([0,1,2,3,4,5],float)


# In[128]:


a.put([0,3],5)


# In[129]:


a


# In[ ]:




