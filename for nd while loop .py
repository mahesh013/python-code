#!/usr/bin/env python
# coding: utf-8

# In[1]:


# while loop:
# It is use to repet the set of statements until its true.


# In[ ]:


# how to print pattern:
#     first outer loop is used to print number of rows
#     nd inner loop used to print number of column
    


# In[1]:


# print the pattern
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()


# In[2]:


a="mahesh"
x=0
for i in a:
    x=x+1
    print(a[0:x])
for i in a:
    x=x-1
    print(a[0:x])


# In[5]:


# print value upto 100 with 10th difference
for i in range(10,101,10):
    print(i)


# In[2]:


# Number of rows
n=int(input("Enter the no of rows you want to print"))
# outer loop
for i in range(n):
#     inner loop
    for j in range(i+1):
        print("*",end=" ")
    print() 


# In[6]:


# number of rows
n=3
# outer loop executing in reveresed order handling rows
for i in range(n):
#     inner loop handling colums
    for j in range(i,n):
        print("*",end=" ")
    print()


# In[3]:


# print 1-100 using while loop
n=1
while n<=100:
    print(n)
    n=n+1


# In[1]:


# print the odd number using while loop
n=1
while n<=20:
    print(n)
    n=n+2


# In[3]:


# print the even number using while loop
n=2
while n<=20:
    print(n)
    n=n+2


# In[7]:


for i in range(1,20,2):
    print(i)


# In[8]:


for i in range(2,20,2):
    print(i)


# In[7]:


n=int(input("Enter a no of rows"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()


# In[9]:


for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()


# In[11]:


# break staement
for val in "marshian":
    if val=="i":
        break
    print(val)
        


# In[36]:


# continue statement
for val in "mahesh":
    if val==h:
        continue
print(val) 
        


# In[ ]:


# append is used to add certain item in coolection


# In[14]:


# without list compression
fruits=["banana","orange","apple","dates"]
a=[]
for x in fruits:
    if "n" in x:
        a.append(x)
print(a)


# In[2]:


# list compression
fruits=["banana","orange","apple","dates"]
a=[x for x in fruits if "n" in x]
a


# In[16]:


a=[x for x in fruits if x!="apple"]
a


# In[17]:


a=[]
for x in "mahesh":
    a.append(x)
print(a)


# In[18]:


d={x:x*2 for x in [2,3,4,5]}
d


# In[22]:


key=["a","b","c"]
value=[1,2,3]
a={b:c for (b,c)in zip(key,value)}
a


# In[23]:


value=[1,2,3]
key=["a","b","c"]
# value=[1,2,3]
a={b:c for (b,c)in zip(key,value)}
a


# In[32]:


di={x:x.upper() for x in "mahesh"}
di


# In[ ]:


key={"a","b"}

