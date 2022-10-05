#!/usr/bin/env python
# coding: utf-8

# In[40]:


# 1:python program to add two number 
# 2:calculate area of trangle
# 3:program to find out square root
# 4:swap two variables
# 5:program to find out largest among three numbers
# 6:program to give fibonacci sequence
# 7:display the multiplication table
# 8:find a number is divisible by another number
# 9:check whther given string is plindrom or not
# 10:remove all the funtuation given string


# In[11]:


# write a program to print 100 prime number starting from 1


# In[30]:


num=100
for i in range(1,num):
    if i%i==0


# In[4]:


# 1:python program to add two number 

a=int(input("Enter a no first:"))
b=int(input("Enter a no first:"))
c=a+b
print(c)


# In[27]:


# 2:calculate area of trangle
b=int(input("Enter a breadth of triangle:"))
h=float(input("Enter a height of triangle: "))
area=1/2*(b*h)
print("Area of trangle is:",area)


# In[10]:


# 3:program to find out square root
a=int(input("Enter a number you want to find out square root:"))
b=a**2
c=b/2
print("Square root of given number is:",c)


# In[11]:


# 4:swap two variables
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
def fun(a,b):
    return b,a
fun(a,b)


# In[12]:


# 5:find out largest among three numbers

a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
c=int(input("Enter a third number:"))
if a>b and a>c:
    print("The greatest number is:",a)
elif b>a and b>c:
    print("The greatest number is:",b) 
else:
    print("The greatest number is:",c)    


# In[16]:


# 6:program to give fibonacci sequence
a,b=0,1
for i in range(1,10):
    print(b)
    a,b=b,a+b


# In[31]:


# 7:display the multiplication table
a=int(input("Enter a number you want to print multiplication table"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)
    i+1


# In[2]:


# 9:check whther given string is plindrom or not
a=input("Enter a string:")
if b==a[::-1]:
    print("string is plindrom")
else:
    print("String is not plindrom")


# In[6]:


# 10:remove all the funtuation given string
a=input("Enter a string:")
a.replace("!","")
# a.replace(",","")
# a.replace("?","")


# In[1]:


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))


# In[11]:


9 and 5


# In[14]:


True greather than True


# In[ ]:





# In[ ]:




