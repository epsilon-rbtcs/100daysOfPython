# Day 9 - Blind Auction Project 

This is a Python console-based project simulating a **Blind Auction**. This project is a part of Day 9 of 100 Days of Python.

## How It Works

It asks for name and bid of the user and if there are any other bidders, on selecting yes, it skips 100 lines hiding the prevoius bid and hence again asks for name and bid, on selecting no, it loops through all the bids, and declare the one with the highest bid as winner. 

## Features

- Collects name and bid amount from each participant.
- Uses a dictionary to store and manage bids.
- Determines the winner by comparing all bids.
- Simple "screen clearing" effect to hide previous entries (for fairness).

## Concepts Used

- Python dictionaries
- While and for loops and conditionals
- User input and typecasting
- Function scope variables
- Basic string formatting and logic

## How to Run

1. Make sure you have `auction_art.py` in the same directory with a `logo` variable defined.
2. Run `blind_auction.py` in any Python environment.
3. Follow on-screen instructions to simulate an auction.

## Output

```text
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name? : eps
What is your bid? : $98
Are there any other bidders? Type 'yes' or 'no'.
yes





















What is your name? : yuj
What is your bid? : $100
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is yuj with a bid of $100 


