import random  # Importing the random module to generate the computer's move

# Multi-line strings to represent Rock, Paper, and Scissors with ASCII art
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

# Prompting the user to enter their move as 0 (Rock), 1 (Paper), or 2 (Scissors)
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Storing the choices in a list to access them by index
list_1 = [rock, paper, scissors]

# Validating the user's input
if a >= 0 and a <= 2:
    print(list_1[a])  # Show the player's chosen move using ASCII art
else:
    print("Invalid Move, You lost.")  # End the game if input is invalid
    exit()

# Generate a random move for the computer (0 to 2)
b = random.randint(0, 2)

# Display the computer's move
print("Computer chose:")
print(list_1[b])

# Compare player and computer moves to determine the result
if a == b:
    print("It's a draw.")
elif a == 0 and b == 1:
    print("You lost.")
elif a == 0 and b == 2:
    print("You won.")
elif a == 1 and b == 0:
    print("You won.")
elif a == 1 and b == 2:
    print("You lost.")
elif a == 2 and b == 0:
    print("You lost.")
elif a == 2 and b == 1:
    print("You won.")
