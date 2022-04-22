list=[] #take an empty string

# how many element or number you want to enter ..
num=int(input("enter number of element in the list\n"))

# increase the user enter number by 1
for i in range(1,num + 1 ):
    
    ele=int(input("enter the elements\n"))
    # add user enter no in the list 
    list.append(ele)
print("your enter element is",list)
print("the grather number is",max(list))