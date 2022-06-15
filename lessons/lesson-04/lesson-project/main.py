# TODO 1: import random module
import random

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

# TODO 2: Generator random from the list
user_choice = random.choice(art)

# print(f"you choice {choice_of_art} {user_choice}")