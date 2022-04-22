# dictionary of hindi words
dec={
    "kitab":"book",
    "pankh":"fan",
    "ghata":"loss",
    "juggad":"arrangement" 
   
}
print("dictionary of hindi words and their meaning\n",dec)
a=input("enter the words you are looking in the dictionary\n")
print("eng meaning of your hindi words is\n",dec.get(a))