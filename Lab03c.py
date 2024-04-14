"""
Author: Myles Amos 
Course:  CSC 121
Assignment: Lab03C:  eCommerce Shopping
Description: Ask the user how many of each of these things they want to buy:  t-shirt, video game, Book
If the user enters a negative number, or goes above the maximum for a particular item, 
the program should continue to ask the user to enter a number until it is valid (use a validation loop pattern).
"""
# This is the total amount of tshirts,video games, and books each person can get. 
max_tshirts = 8
max_video_games = 2
max_books = 3

# These are the prices of the items
tshirt_price = 8.50
video_game_price = 20.00
book_price = 12.95

# Put this function to a validate user input.
def validate_input(prompt, max_quantity):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity < 0 or quantity > max_quantity:
                print(f"Invalid input. You must choose a number between 0 and {max_quantity}.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Ask the user for quantities
tshirts = validate_input("How many t-shirts would you like to purchase? ", max_tshirts)
video_games = validate_input("How many video games would you like to purchase? ", max_video_games)
books = validate_input("How many books would you like to purchase? ", max_books)

# Calculate total cost
total_cost = (tshirts * tshirt_price) + (video_games * video_game_price) + (books * book_price)

# Give out the purchase details, add all the items.
print(f"You purchased: {tshirts} t-shirts, {video_games} video games, and {books} book.")
print(f"Your total purchase is: ${total_cost:.2f} before tax.")
