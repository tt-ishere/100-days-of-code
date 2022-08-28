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

rps = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissor game!!!")
user_choice = int(input("Type 0 for rock, 1 for paper and 2 for scissors\n"))
if user_choice < 0 or user_choice > 2:
    print("You have entered an invalid number, try again")
    user_choice = int(input("Type 0 for rock, 1 for paper and 2 for scissors\n"))
    
computer_choice = random.randint(0, 2) #random figures using the 1st and last index of the rps list

print(f"You chose:\n {rps[user_choice]}")   
print(f"Computer chose:\n {rps[computer_choice]}")

if user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == computer_choice:
    print("That's a draw!")
else:
    print("You lose!")

