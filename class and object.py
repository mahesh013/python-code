#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MyClass():
    variable="Hello"
    def function(self):
        print("message")


# In[2]:


a=MyClass()


# In[4]:


a.variable


# In[5]:


a.function()


# In[6]:


class pet:
    category="In House"
    def typeofpet(self):
        print("Furry")


# In[7]:


tommy=pet()


# In[8]:


tommy.category


# In[9]:


tommy.typeofpet()


# In[1]:


class ExampleClass(object):
    class_attr=0
    def __init__(self,instance_attr):#default value assign by using init        
        self.instance_attr=instance_attr


# In[5]:


foo=ExampleClass(4)


# In[6]:


foo.class_attr


# In[7]:


foo.instance_attr


# In[8]:


class pet(object):
    category="In House"
    def __init__(self,species):
        self.species=species


# In[15]:


bozo=pet('dog')


# In[16]:


bozo.category


# In[17]:


bozo.species


# In[23]:


class vehicle:
    def __init__(self,color):
        self.colour=color
    def start(self):
        print('starting engin')
    def showcolor(self):
        print(f"I am {self.color}")
        


# In[24]:


car=vehicle('black')


# In[25]:


car.start()


# In[27]:


car.showcolor()


# In[6]:


num=10


# In[7]:


num+5


# In[8]:


num.__add__(5)


# In[9]:


int.__str__(num)


# In[10]:


str(num)


# In[11]:


int.__str__(12)


# In[ ]:




