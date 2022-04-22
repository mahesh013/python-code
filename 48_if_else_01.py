# company decided to give bonus of 5% to employee if his/her year of service more than 5 years    .ask user for their salary and year of service and print the net bonus amount
salary=int(input("enter  your salary\n"))
yos=int(input("\nenter your year of service\n"))
if yos>5:
    print("Bonus is",.05*salary)
else:
    print("No Bonus")