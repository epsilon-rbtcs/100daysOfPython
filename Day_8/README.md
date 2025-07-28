# Caesar Cipher Encoder/Decoder 

This is a simple Caesar Cipher program written in Python. This project is part of Day 8 of 100 Days of Python.

## How It Works

The Caesar cipher shifts each letter of the input by a specified amount in the alphabet. It allows you to **encode** or **decode** a message by shifting the letters of the alphabet.

## Concepts Used
- Functions and Function Parameters – Reusable logic for encryption/decryption
- Loops – for to iterate text, while to restart the program
- Conditionals – Handle encode/decode and non-letter characters
- Lists & Indexing – Alphabet list and character shifting
- Modulo Arithmetic – Wrap around alphabet using %
- User Input & Output – Interactive and dynamic behavior
- Boolean Flags – Control program flow (game_over)
- External Module – Imported ASCII logo from art.py

## Features

- Encode a message by shifting letters forward
- Decode a message by shifting letters backward
- Preserves non-alphabet characters like spaces, symbols, and numbers
- Allows repeated runs until the user quits
- Clean, beginner-friendly structure with helpful comments

## Output

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
damn bro
Type the shift number:
9
Here is the encoded result: mjvw kax
Type 'yes' if you want to go again. Otherwise, type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjvw kax
Type the shift number:
9
Here is the decoded result: damn bro
Type 'yes' if you want to go again. Otherwise, type 'no'.
no
Goodbye
```