letter=''' dear <|NAME|>,
you are selected IN XYZ COMP!
congratulations!!!

date:<|DATE|>
'''
name=input("enter a name\n")    
date=input("enter a date\n")    
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
