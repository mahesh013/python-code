a=input("Enter a string\n")
print(a)
char=a[0]
a=a.replace(char,'$')
a=char+a[1:]
print(a)