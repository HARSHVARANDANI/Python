#Single Line Comments
#the first type of comments starts with 'hast tag' symbol like this one
# hash tag commnents are single line comments
#Multiple Line Comments
"""Second type of comments is between 3 double quotes
like this one
triple quote comments are multi line comments"""
#Declaring Variables
var1 = 12
#To declare a variable with value, write the variable name, then give equal to sign and assign its value
#If the value of the variable is of float or integer type then the data can be simply entered after the equal to sign
var2 = "Harsh"
var4 = 10
#Print Function
#If the value of the variable is string or character type, then the data has to be entered in double quotes.
#print function prints whatever is given in the bracket
print(0)
#For float/integer type data, the data is to be written simply inside the brackets
print("Harsh")
#For string/character data type, the data inside the brackets is to be written inside double quotes
print(var1)
#To print the value of a variable simply write the variable name in the brackets
print(var1 + var4)
#To print the sum multiplication division or subtraction of two variables, use the operator sign between variable names
#sign for addition is +, Subtraction is -, multiplication is *, division is /
x = 100
#here x is a variable whose value is 100
x += 5
#The above statement will first add 5 to the value of x which is 100 and then this new value will become the value of x
print(x)
#The above print function will return the value 105
#Type Function
#type() function returns the data type of the value or value of the variable mentioned inside the brackets
print(type(1))
#The above print function will return the value int
print(type(1.0))
#The above print function will return value float
print(type("Harsh"))
#The above print function will return value string
print(type(var1))
#The above print function will return the value int because the value of var1 is 12 which is interger data type
#Lists
var3 = [15,16,17,18,"Harsh"]
# A list is a variable whose value is mentioned inside square brackets
print(var3)
#the above print function will return the value [15,16,17,18]
#To print a particular value from the list, the syntax print(variable name[index number]) is used.
#Index number is the item number on the list variable
#Index number starts from0, 1, 2 .... and so on
#For example in var3, if we want the value 15, the index number will be 0, if we want the value 17, index number will be 2
print(var3[0])
#the above print function will return the value 15
#If for var3 we type index number 5 then the compiler will show 'list index out of range' error
# Note: A list can have duplicate values also
# Note: A list can contain multiple data types like integer, string, float etc.
#Tuples
Tuple = ("Harsh", 15, "Myself")
#Tuple variables are always declared in parenthesis and they can contain multiple data types.
#They can contain duplicate values and also have index number system
print(Tuple)
#The above print statement will print the tuple variable
#Sets
Set = {"Harsh", 15, "Myself"}
#The above variable is of set type and set is always declared in curly brackets
#They can contain duplicate values and they are not printed in order. they are always printed in random order
print(Set)
#The above print statement will print the set variable byt in random order every time it runs
#Dictionaries
Dictionary = {"key":"value","fruit":"mango","number":15}
#the above variable is dictionary type and it will print every key pair set
#Dictionary is always declared in curly brackets and it can not contain duplicate values
print(Dictionary)
#The above print statement will print the dictionary variable
#If else elif
a = 1000
b = 5000
c = 10000
if a>b and a>c:
    print("a is grater than b and c")
elif b>a and b>c:
    print("b is grater than a and c")
elif c>a and c>b:
    print("c is grater than a and b")
else:
    print("b is grater than a")
#For loop
for a in range (11):
    print(a)
    if a>5:
        print("I am greaater than 5")
        break
    else:
        print("I am smaller than 5")
        continue
#While Loop
x = 500
while x>100:
    print(x)
    print("I am greater than 100")
    x-=100
#Inbuilt Functions of Python
#Replace
var6 = "I like to eat Chocolates"
print(var6.replace("Chocolates","Jelly"))#Strip
var8 = "    I am learning Python Basics      "
print(var8.strip())
#Strip function will remove all the extra spaces fron the sides of the string
#Concantenation
var9 = "Ice"
var10 = " cream"
print(var9+ var10)
#Format
chocolates = 200
icecreams = 50
candies = 10
sweets = 100
statement = "I want to buy {0} chocolates, {2} ice creams and {1} candies."
print(statement.format(chocolates,candies,icecreams))
#Sorting
List = [chocolates,icecreams]
List.sort(reverse=True)
print(List)
#Adding items to  list
List.append(candies)
print(List)
#Inserting items to list
List.insert(2,sweets)
print(List)
#Copy a list
List2 = List.copy()
print(List2)
#Creating Functions
def addition(num1,num2): #def is short for define and it is used to declare/define a new function
    ans = int(num1) + int(num2)
    print(ans)
num1 = input("Please enter the first number")
num2 = input("Please enter the second number")
addition(num1,num2)
#File Handling
"""
r - read (0read is the default value for the mode in which you wish to open the file)
w - write
a - append
x - create
b - binary
t - text
"""
file = open("file1.txt","at")
file.write("Previous line is not deleted")
file = open("file1.txt")
print(file.read())
file.close()#This function will close the file
#Modules
#Modules are pre existing python file which already have  several pre defined functions
#modules can be imported to a pythin file by using import function
import os
#os.remove("file2.txt")
#This function will delete file2
#Creating modules
import mymodule as mm
a = input("Please enter the first number")
b = input("Please enter the second number")
mm.subtraction(a,b)
#Classes and Objects
class students:
    def __init__(self, name, age, standard):
        self.name = name
        self.age = age
        self.standard = standard
obj1 = students("Ram",12,"7th")
obj2 = students("Shyam",13,"8th")
print(obj1.age)
print(obj2.standard)
#Error Handling
try:
    print(undefined)
except NameError:
    print("The computer ran into some error :(")