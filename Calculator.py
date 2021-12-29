def addition(first_number,second_number):
    ans = int(first_number)+int(second_number)
    print("The answer is: " + str(ans))
def subtraction(first_number,second_number):
    ans = int(first_number)-int(second_number)
    print("The answer is: "+str(ans))
def multiplication(first_number,second_number):
    ans = int(first_number)*int(second_number)
    print("The answer is: " + str(ans))

def division(first_number,second_number):
    ans = int(first_number)/int(second_number)
    print("the answer is: " + str(ans))

print("Welcome to The Calculator")
operation = input("Please enter the operation that you wish to perform: ")

if operation.lower() == "addition":
    x = input("Please enter the first number: ")
    y = input("Please enter the second number: ")
    addition(x,y)
elif operation.lower() == "subtraction":
    x = input("Please enter the first number: ")
    y = input("Please enter the second number: ")
    subtraction(x,y)
elif operation.lower() == "multiplication":
    x = input("Please enter the first number: ")
    y = input("Please enter the second number: ")
    multiplication(x,y)
elif operation.lower() == "Division":
    x = input("Please enter the first number: ")
    y = input("Please enter the second number: ")
    try:
        division(x, y)
    except ZeroDivisionError:
        print("The division of any number by 0 is not possible.")
else:
    print("Please enter a valid operation")