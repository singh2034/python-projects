import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        # use break instead of quit() because the function will stop here and we want to skip it.
        break

    if user_input not in options: 
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer Picks {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors" :
        print('You Won!')
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock" :
        print('Draw!')

    elif user_input == "scissors" and computer_pick == "scissors" :
        print('Draw!') 

    elif user_input == "paper" and computer_pick == "paper" :
        print('Draw!')

    elif user_input == "scissors" and computer_pick == "paper" :
        print('You Won!')
        user_wins += 1

    else :
        print("You Lost!")
        computer_wins += 1
    
    print(f"You won {user_wins} times.")
    print(f"The Computer won {computer_wins} times.")

print("Goodbye!")