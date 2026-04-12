#This program prints that the user is eligible to vote if they are 18 or older, and not eligible if they are younger than 18.
print("Welcome to the voting eligibility checker!")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    print("You are under 18 years old.")
    print("You will be eligible to vote in", 18 - age, "years.")