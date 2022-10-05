#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# syntax:
#     1:operators
#         =:assignment operator
        


# # variable

# In[ ]:


# variable:


# In[2]:


a="mahesh"
type(a)


# In[3]:


b=123
type(b)


# In[4]:


c=12.5
type(c)


# In[7]:


d=True
type(d)


# # operation

# In[8]:


3+2


# In[9]:


5-3


# In[10]:


4+5*11


# In[11]:


8/5


# In[12]:


8//5


# In[13]:


8%5


# In[14]:


17//3


# In[15]:


17%3


# In[16]:


111*6//9


# In[20]:


(60+3)/4


# In[21]:


22**9


# In[22]:


22//9


# In[23]:


-3**2


# In[24]:


(-3)**2


# In[25]:


width=20
height=5*9
width*height


# In[26]:


a


# In[27]:


tax=12.5/100
price=100.5
price*tax


# In[28]:


# "_" previous value
price+_


# In[29]:


round(_,2)


# In[4]:


a=int(input("enter a number"))
b=int(input("enter a number"))
c=(a**2)+(2*a*b)+(b**2)
print(c)


# # string

# In[5]:


'spam eggs'


# In[6]:


"spam eggs"


# In[7]:


""" spam eggs"""


# In[11]:


"dosen't"


# In[12]:


'dosen\'t'


# In[27]:


"\"yes\",he said"


# In[35]:


print('"Isn\'t",she said')


# In[38]:


s="first line\nsecond line"
s


# In[37]:


print(s)


# In[39]:


# \--escape
# \n--new line
# r--raw string


# In[40]:


# use /n
print("c:\somefolder\name")


# In[41]:


# use escape sequence
print("c:\somefolder\\name")


# In[42]:


# using r ie raw
print(r"c:\somefolder\name")


# # operation over string

# In[43]:


'um'*3


# In[44]:


'py''thon'


# In[49]:


pre ='py'
pre+'thon'


# In[50]:


'um'*3+'ium'


# # indexing

# In[52]:


word="python"
word


# In[53]:


word[0]


# In[54]:


word[5]


# In[55]:


word[6]


# In[56]:


word[-1]


# In[57]:


word[-6]


# # slicing

# In[58]:


word="python"
word[0:2]


# In[59]:


word[0:3]


# In[60]:


word[4:6]


# In[63]:


word[:4]


# In[64]:


word[3:]


# In[65]:


word[6:]


# In[66]:


word[42]


# In[67]:


word[:42]


# In[68]:


word[42:]


# In[69]:


word[-2:-1]


# In[70]:


word[-6:-3]


# In[71]:


word[0]="j"


# In[73]:


word[0]+'ython'


# In[74]:


# mutable--chngeble
# unmutable--dose not change
# string are immutable


# # len() function

# In[75]:


# len()--calculate the string


# In[76]:


m='mahesh'
len(m)


# In[5]:


if __name__ == '__main__':

    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
   
    for i in range(len(arr)):
        if arr[i]!=arr[i+1]:
            break
        else:
            continue
    print(arr[i+1])


# In[ ]:


# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
#     order their names alphabetically and print each name on a new line.


# In[2]:


Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)


# In[ ]:





# In[ ]:




