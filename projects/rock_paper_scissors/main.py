import imp


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

choices = [rock, paper, scissors]

# program greetings
print("Welcome to the")
# display choice for the user
user_choice = int(input("What do you choose? type 0 for the Rock, 1 for the Paper or 2 for Scissors. "))
print(f"You chose: {choices[user_choice]}")

# computer
computer_chose = random.choice(choices)
print(f"Computer choice: {computer_chose}")