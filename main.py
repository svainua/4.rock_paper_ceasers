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

# Write your code below this line 👇


my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice >= 3 or my_choice < 0:
    print(" You typed the invalid number")
else:

    if my_choice == 0:
        print(f" Your choice is {rock}")
    elif my_choice == 1:
        print(f" Your choice is {paper}")
    elif my_choice == 2:
        print(f" Your choice is {scissors}")

    comp_choice = random.randint(0, 2)
    if comp_choice == 0:
        print(f" Computer choice is {rock}")
    elif comp_choice == 1:
        print(f" Computer choice is {paper}")
    elif comp_choice == 2:
        print(f" Computer choice is {scissors}")

    if my_choice == comp_choice:
        print("Draw")
    elif (my_choice == 0) and (comp_choice == 1):
        print("Comp wins")
    elif (my_choice == 0) and (comp_choice == 2):
        print("You win")
    elif (my_choice == 1) and (comp_choice == 0):
        print("You win")
    elif (my_choice == 1) and (comp_choice == 2):
        print("Comp wins")
    elif (my_choice == 2) and (comp_choice == 0):
        print("Comp wins")
    elif (my_choice == 2) and (comp_choice == 1):
        print("You win")

ИЛИ

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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

##Debugging challenge:
# Try running this code and type 5.
# It will give you an IndexError and point to line 32 as the issue.
# But on line 38 we are trying to prevent a crash by detecting
# any numbers great than or equal to 3 or less than 0.
# So what's going on?
# Can you debug the code and fix it?
# Solution:
