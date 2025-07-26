# Importing the logo from art.py
from art import logo

# Display the logo when the program starts
print(logo)

# Defining the alphabet for Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Game loop control variable
game_over = False

# Caesar cipher function: handles both encoding and decoding
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each character in the input text
    for letter in original_text:
        if letter in alphabet:
            
            # Shift the letter and wrap around using modulo
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            # If the character is not in the alphabet (e.g., space, number, symbol), add it as is
            output_text += letter

    # Print the final encoded or decoded result
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main game loop
while not game_over:

    # User input for direction, message, and shift amount
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to restart the program
    ques = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if ques != "yes":
        print("Goodbye")
        game_over = True
