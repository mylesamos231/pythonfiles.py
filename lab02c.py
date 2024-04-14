"""
Name:Myles Amos
Date:02/01/2024
Description:Write a program that asks the user to enter the number of strokes and the value of par for a single golf hole.
 """
# Get input for number of strokes
strokes = int(input("How many strokes? "))
# Get input for par value
par = int(input("What is par? "))
# Check for invalid par value
if par not in (3, 4, 5):
    print("Error")
else:
    # Determine result based on strokes and par
    if strokes - par == 2:
        print("That is an Eagle.")
    elif strokes - par == 1:
        print("That is a Birdie.")
    elif strokes - par: 
        print("That is a Par.")
    elif strokes - par == + 1:
        print("That's a bogey")
    # Display strokes over Bogey for any other cases
    else: 
        print(f"That is {strokes - par} over Bogey.")
