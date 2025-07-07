#  PyPassword Generator — Day 5 Project

This project includes two versions of a **random password generator** written in Python as part of **Day 5** of the 100 Days Of Python course.

## What It Does

The program allows users to define how many **letters**, **symbols**, and **numbers** they want in their password, then generates it accordingly.

---

##  Concepts Used

- Python lists and list operations
- `for` loops and `range()`
- `random.choice()` and `random.shuffle()`
- String concatenation and `.append()`
- User input and formatting

---

##  Features

###  Easy Version (`Easy Password Generator.py`)

- Generates a password with all **letters first**, followed by **symbols**, then **numbers** in sequence
- Example Output:

Welcome to the PyPassword Generator!
How many letters would you like in your password?
7
How many symbols would you like?
4
How many numbers would you like?
3
Your password is : thYyaNp$!#+278

### Hard Version (`Hard Password Generator.py`)

- Generates a password with the selected number of letter, symbols and numbers but this time all characters are randomly shuffled instead of being placed in a determined sequence makng harder to guess than the easy one.

-Example Output:

Welcome to the PyPassword Generator!
How many letters would you like in your password?
7
How many symbols would you like?
5
How many numbers would you like?
4
['g', 'c', 'U', 'R', 'a', 'H', 'C', '&', '#', '!', '(', '$', '3', '6', '4', '7']
['!', 'c', '4', 'C', '6', 'g', '(', '&', 'U', 'a', '7', '3', '$', 'R', 'H', '#']
Your password is : !c4C6g(&Ua73$RH#
