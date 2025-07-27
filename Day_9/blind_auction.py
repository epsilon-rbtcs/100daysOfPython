from auction_art import logo
print(logo)

# Dictionary to store each bidder's name and bid
system = {}

# Variables to track the highest bid and corresponding bidder
max_value = 0
bid_winner = ""

# Loop control flag
game_over = False

while not game_over:
    # Take user input for name and bid amount
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))

    # Store bid in dictionary
    system[name] = bid

    # Ask if more bidders are joining
    ques = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if ques == "no":
        game_over = True

        # Find the highest bid and corresponding winner
        for bidder in system:
            current_bid = system[bidder]
            if current_bid > max_value:
                max_value = current_bid
                bid_winner = bidder

        print(f"The winner is {bid_winner} with a bid of ${max_value}")

    elif ques == "yes":
        # Clears previous input visually (basic way)
        print("\n" * 20)
    else:
        print("Invalid choice entered. Session terminated.")
        game_over = True
