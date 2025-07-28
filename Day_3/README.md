# Treasure Island - Adventure Game

This is a simple text-based adventure game built on Day 3 of the 100 Days of Python course.

## What It Does

- Displays ASCII art to welcome the player.
- Asks the player to make decisions through a series of inputs.
- Based on the choices, the player either finds the treasure or faces various "Game Over" scenarios.

## Concepts Used

- Multi-line strings (`'''` for ASCII art)
- `print()` statements
- `input()` for user interaction
- `if/elif/else` conditional logic
- `.lower()` to handle user input case-insensitively
- String comparison

## Sample Output

```
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

Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go
   Type "left" or "right".
left
You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
red
It's a room full of fire. Game Over.
```