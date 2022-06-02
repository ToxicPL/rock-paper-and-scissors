import random

print("Welcome to the Rock, Papers and Scissors game")
computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]
# rock: 0 Paper: 1 Scrissors: 2
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You have won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You have won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You have won!")
        user_wins += 1
        
    else:
        print("You have lost!")
        computer_wins += 1

print("--------------------Summary--------------------")
print("Your score is {}".format(user_wins))
print("Computer score is {}".format(computer_wins))
print("--------------------Thanks for playing the game--------------------")