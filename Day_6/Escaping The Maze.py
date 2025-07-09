# Day 6 of 100 Days of Python - Escaping The Maze in Reeborg's World

# Define a helper function to simulate turning right
# Reeborg environment only provides turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward as long as there are no walls ahead
while front_is_clear():
    move()

# Turn left to face the inner maze
turn_left()

# Use the right-hand rule to find the goal(as mentioned in instructions)
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

#Note - To run this code you have to write this code in python code area in Reeborg's World.