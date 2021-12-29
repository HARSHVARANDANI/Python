import random
options = ["rock", "paper","scissors"]
computer_score = 0
user_score = 0
while True:
    user_input = input("Enter rock/paper/scissors or Q to quit. ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        print('Pkease enter a valid input.')
        continue
    rand_num = random.randint(0, 2)
    computer_input = options[rand_num]
    if user_input == "rock" and computer_input == "scissors":
        print("Computer's pick is", computer_input)
        print("You Won!")
        user_score += 1
    elif user_input == "paper" and computer_input == "rock":
        print("Computer's pick is", computer_input)
        print('You won!')
        user_score += 1
    elif user_input == "scisssor" and computer_input == "paper":
        print("Computer's pick is", computer_input)
        print('You won!')
        user_score += 1
    elif user_input==computer_input:
        print("The computer's pick is :", computer_input)
        print("Tie!!")
    else:
        print("Computer's pick is", computer_input)
        print('You lost!')
        computer_score += 1
print('Your score =', user_score)
print("Computer's score =", computer_score)
if user_score>computer_score:
    print('Congratulations! You Have Won The Game!')
elif user_score==computer_score:
    print('The Game Is A Tie!')
else:
    print('Sorry, You Lost The Game!')