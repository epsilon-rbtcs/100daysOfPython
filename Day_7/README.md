# Day 7 - Hangman Game 

This is a terminal-based Hangman game built in Python as part of Day 7 in the 100 Days of Python course. The game randomly selects a word, and the player must guess it letter by letter while avoiding losing all 6 lives.

---

## Features

- Random word selection from an external list
- ASCII art-based visual stages (imported from external file)
- User input and validation
- Tracks guessed letters to avoid penalties for repeats
- Win/loss detection with custom messages

---

## Topics Covered

- Importing from external files/modules (`hangman_words`, `hangman_art`)
- Using `random.choice()` for word selection
- Loops and conditionals to control game flow
- String manipulation and dynamic updates of the word
- List usage for tracking previously guessed letters
- Game state management using flags and counters
- ASCII art visuals to enhance gameplay

---

## Files Used

- `Hangman Game.py` — the game logic (this file)
- `hangman_words.py` — contains the word list
- `hangman_art.py` — contains hangman stages and logo ASCII art

---

## Example Run
 
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
Word to guess :______
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess : _a____

  +---+
  |   |
      |
      |
      |
      |
=========

****************************6/6 LIVES LEFT****************************
Guess a letter:


