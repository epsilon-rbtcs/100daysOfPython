# Day 7 - Hangman Game

import random
from hangman_words import word_list
from hangman_art import stages, logo

# Starting number of lives
lives = 6

# Display the game logo
print(logo)

# Randomly choose a word from the imported list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a placeholder string with underscores for each letter
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print("Word to guess :" + placeholder)

# List to store letters already guessed correctly
correct_letters = []

# Game status flag
game_over = False

# Game loop runs until win or lose
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""

    # Warn if user has already guessed the letter
    if guess in correct_letters:
        print(f"You already guessed {guess}")

    # Build the new placeholder string based on guessed letters
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess : " + display)

    # Deduct life if guess was wrong
    if guess not in chosen_word:
        lives -= 1
        print("Uh Oh. That letter is not in the word. You lost a life !!")

        # Game ends if lives run out
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}. YOU LOSE !!**********************")

    # Win condition: no more underscores in word
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Print hangman stage
    print(stages[lives])
