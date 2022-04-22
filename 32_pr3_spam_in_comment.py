# text=input("enter your text\n")
# spam=["make a lot money","buy now","subscribe this","click this"]
text=input("enter your text\n")

# if spam in text:
#     print("this is spam messege")


if "make a lot money" in text:
    print("this is spam messege")
elif "buy now" in text:
    print("this is spam messege")
elif "subscribe this" in text:
    print("this is spam messege")
elif "click this"in text:   
    print("this is spam messege")

else:
    print("this is not spam messege")

