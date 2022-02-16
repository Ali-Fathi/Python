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
user_choice = int(input("What do you choose? type 0 for the Rock, 1 for the Paper or 2 for Scissors.\n"))
print(f"You chose: {choices[user_choice]}")

# computer
computer_choice = random.randint(0, 2)
print(f"Computer chose: {choices[computer_choice]}")

# Logic 
# The game rules:
#     - Rock wins against scissors.
#     - Scissors win against paper.
#     - Paper wins against rock

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Its a draw")
else:
    print("You typed an invalid number!")
