#!/usr/bin/env python
# coding: utf-8
#Which of the following is the output of the below Python code? & Why
str='Hello World'
print (str.replace('l','n',2))#Which of the following is the output of the below Python code?
str='Tech Pune'
print (str[4:9])# Which of the following operators can be used with Strings? cover example
a) +
b) *
c) -
d) in# What is the output when following statement is executed?
str='good-BYE'
print (str.capitalize())# Which of the following is the output of the below Python code?
str='example'
print (str.center(10,'*'))
1. *example *
2. *****example*****
3. **example*
4. *example**# Which of the following is the output of the below Python code?
str='python'
print (str.center(15,'*'))
1. *****python****
2. ********python*******
3. ****python*****
4. ********python*******# Which of the following print statements will print all the names in the list on a separate line?
identity = ['Python', 'Python questions', 'Python String', 'Python ML', 'Python DS']
1. print ("\n".join(identity))
2. print (identity.concatenate("\n") )
3. print (identity.join("\n") )
4. print (identity.join("%s\n", names))# What is the default value of encoding in the string function encode()?
1. utf-8
2. utf-16
3. ascii
4. qwerty# Which of the following is the output of the below Python code?
str='abababadaadbbaccabc'
print (str.count('ab',-17,-1))
1. 5
2. 4# What is the output when following statement is executed?
str='abcdefcdyz'
print (str.partition('cd'))
1. ('ab','cd','efcdyz')
2. ('ab','cd','ef','cd','yz')
3. ('ab','ef','yz')
4. ('abcdef','cd','yz')# Which of the following is the output of the below Python code
str='abcdefcdyzcd'
print (str.split('cd',2))
1. ['abcdef','yzcd']
2. ['ab','ef','yzcd']
3. ['ab','efcdyzcd']
4. ['ab','ef','yz']# Which of the following is the output of the below Python code?
str='abbabadaadbbaccabc'
print (str.count('ab',2))
1. 3
2. 2
3. 4
4. 5# What is the output when following statement is executed?
str='Hello@Python!!'
print (str.lower())# Which of the following is the output of the following Python instruction? & Why
print ('am'.zfill(5))
1. 000am
2. am000
3. 00am0
4. 0am00# Which of the following is the output of the below Python code snippet?
str='PYTHON\nString\nConcepts'
print (str.splitlines())
1. ['PYTHON', '\nString', '\nConcepts']
2. ['PYTHON', 'String', 'Concepts']
3. ['PYTHON\n', 'String\n', 'Concepts']
4. ['PYTHON\n', 'String\n', 'Concepts\n']# What is the output when the following instruction is executed?
print ('+55'.zfill(5))
1. 00055
2. +++55
3. 00+55
4. +0055

print ('+55'.zfill(5))
1. 00055
2. +++55
3. 00+55
4. +0055# Which of the following is the output of the below Python code?
str='Welcome\tTo\tPython\tProgramming'
print (str.expandtabs(4))
1. Welcome To Python Programming
2. Welcome To Python Programming
3. Welcome To Python Programming
4. WelcomeToPythonProgramming# Which of the following is the output of the below Python code?
str='PYTHON string concepts'
print (str.title())#
#Example
test_str = 'Programming '
# The trailing whitespaces are excluded
print(test_str.rstrip())# Split function
#Example
str = 'pdf csv json'
print(str.split(" "))
print(str.split())# Say test_list is [3, 4, 5, 20, 5, 25, 1, 3] then what would be the value of test_list after test_list1. [3, 4, 5, 20, 5, 25, 1, 3]
2. [1, 3, 4, 5, 20, 5, 25]
3. [1, 3, 3, 4, 5, 5, 20, 25]
4. [3, 1, 25, 5, 20, 5, 4]
5. [3, 5, 20, 5, 25, 1, 3]# Which of the following is the output of the below Python code?
test_list = [1,2,3,None,(),[],]
print(len(test_list))
1. 6
2. syntax error
3. 4
4. 5
5. 7  # What is the output of the following code snippet?
print type([1,2])# Which of the following is the output of the below Python code?
def f(value, values):
v = 1
values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
1. 3 44
2. 3 1
3. 1 1
4. None
5. 1 44# The x % y operator can be used to check for even or odd numbers.
# Here, we need to verify an even number so complete the below condition?
if _______:
print("x is an even number")
1. X % 1 == 2
2. X % 2 == 1
3. X % 2 == 0
4. X % "even" == True
5. X % x == 0# Given a string strtext = “Welcome”, which of the following statement would yield TypeError?
1. print (strtext[0])
2. strtext[1]= ‘r’
3. None of these
4. print (strtext.lower())
5. print(strtext.strip())# What is the output of the below code fragment?
print type(1/2)
1. <type 'double'>
2. <type 'int'>
3. <type 'number'>
4. <type 'float'>
5. <type 'tuple'>