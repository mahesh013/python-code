#!/usr/bin/env python
# coding: utf-8

# # for loop

# In[6]:


words=['cat','window','defenestrate']

for w in words:
    print(w,len(w))


# In[7]:


for w in words[:]:
    if len(w)>6:
        words.insert(0,w)
words
        


# # while loop

# In[8]:


x=1
while x<11:
    print(x)
    x=x+1


# In[2]:



x=256
total=0
while x>0:
    print(x,total)
    if total>500:
        break
    total+=x
    x=x//2


# In[6]:


a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b


# # break

# In[12]:


for i in range(1,11):
    if i==5:
        break
    print(i)


# # continue

# In[11]:


for i in range(1,11):
    if i==5:
        continue
    print(i)


# # pass

# In[18]:


x=-1
if x<0:
    print("negative")
elif x>0:
    pass
else:
    print("no is positive")


# In[17]:


def add(a,b):
    pass


# # range() function

# In[19]:


a=['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])


# In[20]:


10*(1/0)


# In[21]:


4+spam*3


# In[22]:


'2'+2


# In[23]:


int('2')+2


# # try and except

# In[24]:


def attempt_float(x):
    try:
        print("try")
        return float(x)
    except:
        print("except")
        return x


# In[25]:


# attempt_float(2.444)


# In[28]:


attempt_float('something')


# In[29]:


def attempt_float(x):
    try:
        print("try")
        return float(x)
    except:
        print("except")
        return x
    finally:
        print("finally")


# In[30]:


attempt_float(2.444)


# In[31]:


attempt_float('something')


# In[32]:


float((1,2))


# In[33]:


attempt_float((1,2))


# In[1]:


def attempt_float(x):
    try:
        print("try")
        return float(x)
    except ValueError:
        print("except")
        return x
    finally:
        print("finally")


# In[2]:


attempt_float((1,2))


# In[3]:


f=open(path,'w')
try:
    write_to_file(f)
finally:
    f.close()


# In[4]:


def attempt_float(x):
    try:
        print("try")
        return float(x)
    except (TypeError,ValueError):
        print("except")
        return x
    finally:
        print("finally")


# In[5]:


attempt_float((1,2))


# In[ ]:


# sagarchovdhan1007@gmail.com

