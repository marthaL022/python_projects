# number = int(input("Enter a number:"))
userInput = input("Enter a number:")
number = 0

if not isinstance(userInput, int):
    number = int(input("Enter a valid number:"))

if number >= 90:
    print("grade A")
elif number >=60:
    print ("grade B")
else:
    print("grade C")

