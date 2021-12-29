import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "{}[]()!@#$%^&*-_=+"
numbers = "0123456789"
all = lower + upper + symbols + numbers
length = input("Please enter the required length of the password: ")
password = "".join(random.sample(all,int(length)))
print(password)