# Print an introductory ASCII art banner
print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|====.'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`       
''')

# Intro message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision: left or right
a = input('You\'re at a cross road. Where do you want to go\n   '
          'Type "left" or "right".\n').lower()

if a == "left":
    # Second decision: wait or swim
    b = input('You\'ve come to a lake. There is an island in the middle of the lake. '
              'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    
    if b == "wait":
        # Final decision: door color
        c = input("You arrive at the island unharmed. There is a house with 3 doors. "
                  "One red, one yellow and one blue. Which colour do you choose?\n").lower()
        
        if c == "yellow":
            print("You found the treasure! You Win!")
        elif c == "blue":
            print("You enter a room of beasts. Game Over.")
        elif c == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("Invalid Option. Game Over.")
    
    elif b == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid Option. Game Over.")

elif a == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Invalid Option. Game Over.")
