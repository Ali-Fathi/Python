# TODO 1: import random module
import random
from secrets import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

art = [rock, paper, scissors]
art_len = len(art)
# TODO 2: Generator random from the list
user_choice = int(input("What do you choice? Type 0 for Rock, 1 for Paper, and 2 for Scissor.\n"))
computer_choice = random.choice(art)
user_choice_of_art = art[user_choice]
# TODO 3: Output what user and computer chose to test
print(f"You chose:\n {user_choice_of_art}")
print(f"Computer chose:\n {computer_choice}")

# Game 

if computer_choice == user_choice_of_art:
    print(f"You chose:\n {user_choice_of_art}")
    print(f"Computer chose:\n {computer_choice}")
    print(f"\n\n Its a draw!")

    

