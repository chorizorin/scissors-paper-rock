import random


user_action = input ("Enter a choice: (rock, paper, scissors): ")
possible_action = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_action)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. TIE.")
elif user_action == "rock":
    if computer_action == "scissors":
     print("Rock smashes scissors. WIN!")
    else:
        print("Paper covers rock. LOSE!")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! WIN!")
    else:
        print("Scissors cut paper. LOSE!")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper. WIN!")
    else:
        print("Rock smashes scissors. LOSE!")
play_again = input("Play again? (y/n): ")
if play_again.lower() != "y":
    breakpoint