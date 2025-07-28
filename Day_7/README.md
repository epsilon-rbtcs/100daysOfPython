# Day 7 - Hangman Game 

This is a terminal-based Hangman game built in Python as part of Day 7 in the 100 Days of Python course. 

## How It Works

The game randomly selects a word, and the player must guess it letter by letter while avoiding losing all 6 lives.

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

## Output 

```
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    
Word to guess :_________
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess : ______a__

  +---+
  |   |
      |
      |
      |
      |
=========

****************************6/6 LIVES LEFT****************************
Guess a letter: v
Word to guess : ______a__
Uh Oh. That letter is not in the word. You lost a life !!

  +---+
  |   |
  O   |
      |
      |
      |
=========

****************************5/6 LIVES LEFT****************************
Guess a letter: e
Word to guess : e_____a_e

  +---+
  |   |
  O   |
      |
      |
      |
=========

****************************5/6 LIVES LEFT****************************
Guess a letter: c
Word to guess : e_____a_e
Uh Oh. That letter is not in the word. You lost a life !!

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: o
Word to guess : e___o_a_e

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: n
Word to guess : e___ona_e

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: g
Word to guess : e___onage

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: s
Word to guess : es__onage

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: p
Word to guess : esp_onage

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: i
Word to guess : espionage
****************************YOU WIN****************************

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
```