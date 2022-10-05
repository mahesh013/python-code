#!/usr/bin/env python
# coding: utf-8

# In[1]:


# group of statement performing spesific task


# In[ ]:





# In[6]:


def substraction(a,b):
#     substraction of two
    
    c=a-b
    return c
d=substraction(9,7)
print(d)
e=substraction(10,20)
print(e)
print(substraction.__doc__)


# In[12]:


# print even or odd of user enter number
def fun(c):
    if (c%2==0):
        print("no is even")
    else:
        print("no is odd")
    
#     return(c)
c=int(input("enter a number:"))
fun(c)


# In[ ]:


# accept name and gender(M,F) and prefix with mr and mrs accordingly
# accept 2 no ,if n1<n2 then swap the number else return the same order
# maximum of three number
# accept in lower case and return in lower case
# accept radius and print area


# In[18]:


# accept name and gender(M,F) and prefix with mr and mrs accordingly
a=input("Enter the name:")
b=input("Enter the gender:")

def fun(a,b):
    if b=="M"or b=="m":
        print("Hello mr",a)
    elif b=="F"or b=="f":
         print("Hello mrs",a)
fun(a,b)


# In[3]:


# accept 2 no ,if n1<n2 then swap the number else return the same order
a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
def swap(a,b):
    if a<b:
        print(b)
        print(a)
    else:
        print(a)
        print(b)
swap(a,b)


# In[5]:


# maximum of three number
l=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
n=int(input("Enter the third number:"))
def greather(a,b,c):
    if (a>b) and (a>c):
        print("a is greather ",a)
    elif(b>a)and(b>c):
        print("b is greather ",b)
    else:
        print("c is greather ",c)
greather(l,m,n)


# In[9]:


# accept in lower case and return in upper case
a=input("Enter a string in lower case:")
def upper(a):
    b=a.upper()
    print(b)
upper(a)


# In[3]:


# accept radius and print area of circle
r=int(input("Enter the radius of circle:"))
def area(c):
    a=3.14*r**2
    print("Area of circle is:",a)
area(r)


# In[2]:


def average(a, b, c):
    return (a + b + c) / 3

l=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
n=int(input("Enter the Third number:"))

    
avg = average(l, m, n)
print(avg)


# In[9]:


# recurssion
'''
factorial(n) = n * factorial(n-1)
factorial(0) = 1 (By definition)
factorial(4) = 4 X 3 X 2 X 1
factorial(3) = 3 X 2 X 1
factorial(13) = 13 X 12 X 11 X 10 X 9 X 8 X 7 X 6 X 5 X 4 X 3 X 2 X 1
'''

def factorial(n):
    # Base condition 
    if(n ==0 or n==1):
        return 1
    return n * factorial(n - 1) 

a = fac(6)
print(a)


# In[2]:


# Sum(8) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
# Sum(n) = Sum(n-1) + n 
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) +n

a = sum(6)
print(a)


# In[11]:


def printPattern(n):
    for i in range(n): 
        print("*"*(n+i)) 

printPattern(3) 


# In[12]:


def process(l, word):
    word = word.strip()
    if word in l:
        l.remove(word) 
    return l1

l1 = ['harry', 'rohan', 'akash', 'shubham', 'lovish']
l1 = process(l1, '   rohan   ')
print(l1)


# In[ ]:




