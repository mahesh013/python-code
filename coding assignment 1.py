#!/usr/bin/env python
# coding: utf-8

# # replace(old,new,count)

# In[13]:


# replace(old,new,count)
# Return a copy with all occurrences of substring old replaced by new.


#Which of the following is the output of the below Python code? & Why
str='Hello World'
print (str.count('o'))


# In[55]:


str="mahesh"
print(str.replace('h','k',2))


# # string slicing

# In[2]:


#Which of the following is the output of the below Python code?
str='Tech Pune'
print (str[4:9])


# # string operator

# In[ ]:


# we can not use "*" and "-" operator in string


# In[4]:


# # Which of the following operators can be used with Strings? cover example
# a) +
# b) *
# c) -
# d) in
a="mahesh"
b="kandekar"
c=a+b
c


# In[2]:


a="mahesh"
b="kandekar"
c=a[-1]
c


# In[1]:


a="mahesh"
b="kandekar"
c=a*3
c


# In[7]:


a="mahesh"
b="kandekar"
c=a in b
c


# # capitalize() function

# In[ ]:


# capitalize() capitalize only first letter of string 


# In[8]:


# What is the output when following statement is executed?
str='good-BYE'
print (str.capitalize())   #capitalize the first letter of string


# In[56]:


str="MAHESH"
print(str.capitalize())


# # center() function

# In[ ]:


# center( width,'fill charecter/default space') ---return the center string of length width


# In[64]:


# # Which of the following is the output of the below Python code?
# str='example'
# print (str.center(10,'*'))
# 1. *example *
# 2. *****example*****
# 3. **example*
# 4. *example**


str='example'
print (str.center(10,'*'))


# In[10]:


# # Which of the following is the output of the below Python code?
# str='python'
# print (str.center(15,'*'))
# 1. *****python****
# 2. ********python*******
# 3. ****python*****
# 4. ********python*******


# In[68]:


str='python'
print (str.center(15,'*'))


# In[12]:





# # join() method

# In[ ]:


#  "seperator".join()  method takes all items in iterable and joins them into one string


# In[81]:


identity = ['Python', 'Python questions', 'Python String', 'Python ML', 'Python DS']
print ("\n".join(identity))


# # encode() method

# In[97]:


# encode() method encode a string using the given encoding scheme
# if no parameter are specified,then it  use default value
# and the encoding parameters,the default value is utf8 and for the error parameter the default value is strict


# In[96]:


# # What is the default value of encoding in the string function encode()?
# 1. utf-8
# 2. utf-16
# 3. ascii
# 4. qwerty
a="mahesh"
# a.encode('utf8')
a.encode()



# # count() function

# In[ ]:


# count() method return the no of non overlapping occurence


# In[88]:


# # Which of the following is the output of the below Python code?
# str='abababadaadbbaccabc'
# print (str.count('ab',-17,-1))
# 1. 5
# 2. 4
# 3.3
# 4. 6


# In[18]:


str='abababadaadbbaccabc'
print (str.count('ab',-17,-1))


# In[99]:


# # Which of the following is the output of the below Python code?
# str='abbabadaadbbaccabc'
# print (str.count('ab',2))
# 1. 3
# 2. 2
# 3. 4
# 4. 5


# In[100]:


str='abbabadaadbbaccabc'
print (str.count('ab',2))


# # partitions() function

# In[19]:


# partitions() function partioning the string into three parts with given seperators


# In[ ]:


# # What is the output when following statement is executed?
# str='abcdefcdyz'
# print (str.partition('cd'))
# 1. ('ab','cd','efcdyz')
# 2. ('ab','cd','ef','cd','yz')
# 3. ('ab','ef','yz')
# 4. ('abcdef','cd','yz'


# In[20]:


str='abcdefcdyz'
print (str.partition('cd'))


# In[101]:


str="maheshrameshkandekar"
print(str.partition('ramesh'))


# # lower() function

# In[ ]:


# lower() function convert string into lowercase


# In[4]:


# # What is the output when following statement is executed?
# str='Hello@Python!!'
# print (str.lower())


# In[5]:


str='Hello@Python!!'
print (str.lower())


# In[4]:


str="MAHESH"
print(str.lower())


# # upper() function

# In[5]:


str="mahesh"
print(str.upper())


# # zfill() method

# In[ ]:


# zfill() method add zero at beggining of string until it reaches the specified length


# In[6]:


# # Which of the following is the output of the following Python instruction? & Why
# print ('am'.zfill(5))
# 1. 000am
# 2. am000
# 3. 00am0
# 4. 0am00


# In[7]:


print ('am'.zfill(5))


# In[103]:


print('mahesh'.zfill(30))


# In[ ]:


# # What is the output when the following instruction is executed?
# print ('+55'.zfill(5))
# 1. 00055
# 2. +++55
# 3. 00+55
# 4. +0055

# print ('+55'.zfill(5))
# 1. 00055
# 2. +++55
# 3. 00+55
# 4. +0055


# In[108]:


print ('+55'.zfill(5))


# # splitlines() function

# In[8]:


# splitlines() function return a list of the lines in the string, breaking at line boundaries.


# In[ ]:


# # Which of the following is the output of the below Python code snippet?
# str='PYTHON\nString\nConcepts'
# print (str.splitlines())
# 1. ['PYTHON', '\nString', '\nConcepts']
# 2. ['PYTHON', 'String', 'Concepts']
# 3. ['PYTHON\n', 'String\n', 'Concepts']
# 4. ['PYTHON\n', 'String\n', 'Concepts\n']


# In[9]:


str='PYTHON\nString\nConcepts'
print (str.splitlines())


# In[107]:


str='mahesh\nkandekar'
print (str.splitlines())


# # expandtabs() function

# In[10]:


# expandtabs() Return a copy where all tab characters are expanded using spaces.


# In[13]:


# # Which of the following is the output of the below Python code?
# str='Welcome\tTo\tPython\tProgramming'
# print (str.expandtabs(4))
# 1. Welcome To Python Programming
# 2. Welcome To Python Programming
# 3. Welcome To Python Programming
# 4. WelcomeToPythonProgramming


# In[14]:


str='Welcome\tTo\tPython\tProgramming'
print (str.expandtabs(4))


# # title() function

# In[109]:


# title() function Return a version of the string where each word is titlecased.


# In[15]:


# Which of the following is the output of the below Python code?
str='PYTHON string concepts'
print (str.title())


# In[110]:


str="mahesh kandekar"
print(str.title())


# # rstrip() function

# In[112]:


# rstrip() function Return a copy of the string with trailing whitespace removed.


# In[16]:


#
#Example
test_str = 'Programming '
# The trailing whitespaces are excluded
print(test_str.rstrip())


# In[22]:


str=   "mahesh "
print(str.rstrip())
# print(str)


# # split() function

# In[ ]:


# split() function Return a list of the words in the string, using seperator as the delimiter string.


# In[17]:


# Split function
#Example
str = 'pdf csv json'
print(str.split(" "))
print(str.split())


# # len() function

# In[ ]:


# len() function use to calculate length of string


# In[ ]:


# # Say test_list is [3, 4, 5, 20, 5, 25, 1, 3] then what would be the value of test_list after test_list1.
# 1. [3, 4, 5, 20, 5, 25, 1, 3]
# 2. [1, 3, 4, 5, 20, 5, 25]
# 3. [1, 3, 3, 4, 5, 5, 20, 25]
# 4. [3, 1, 25, 5, 20, 5, 4]
# 5. [3, 5, 20, 5, 25, 1, 3]


# In[18]:


# # Which of the following is the output of the below Python code?
# test_list = [1,2,3,None,(),[],]
# print(len(test_list))
# 1. 6
# 2. syntax error
# 3. 4
# 4. 5
# 5. 7


# In[19]:


test_list = [1,2,3,None,(),[],]
print(len(test_list))


# In[ ]:





# In[25]:


# # Which of the following is the output of the below Python code?
# def f(value, values):
# v = 1
# values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])
# 1. 3 44
# 2. 3 1
# 3. 1 1
# 4. None
# 5. 1 44


# In[31]:


def f(value, values):
    v = 1
    values[0] = 44
#     values=v nd t=value
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])


# In[32]:


def f(value, values):
    v = 1
#     values[0] = 44 
#     values=v nd t=value
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v)


# In[25]:


def sum(a,b):
    sum=a+b
    return sum
sum(10,30)


# In[26]:


result=sum(10,30)
result


# In[32]:


# # The x % y operator can be used to check for even or odd numbers.
# # Here, we need to verify an even number so complete the below condition?
# if _______:
# print("x is an even number")
# 1. X % 1 == 2
# 2. X % 2 == 1
# 3. X % 2 == 0
# 4. X % "even" == True
# 5. X % x == 0


# In[38]:


x=6
if x % 2 == 0:
    print("x is an even number")


# In[39]:


# # Given a string strtext = “Welcome”, which of the following statement would yield TypeError?
# 1. print (strtext[0])
# 2. strtext[1]= ‘r’
# 3. None of these
# 4. print (strtext.lower())
# 5. print(strtext.strip())


# In[34]:


strtext = "Welcome"

strtext[1]= 'r'
# print (strtext[0])


# # type() function

# In[ ]:


# # What is the output of the below code fragment?
# print type(1/2)
# 1. <type 'double'>
# 2. <type 'int'>
# 3. <type 'number'>
# 4. <type 'float'>
# 5. <type 'tuple'>


# In[53]:


print(type(1/2))


# In[1]:


# What is the output of the following code snippet?
print(type([1,2]))


# In[ ]:




