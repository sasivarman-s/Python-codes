#This program reads all the data that user gives and return which data is larger!
n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))
n3=int(input("Enter the 3rd number: "))
if(n1>n2)and (n1>n3):
    print(n1,"is the largest")
elif(n2>n1)and (n2>n3):
    print(n2,"is the largest value")
else: print(n3,"is the largest value")        
