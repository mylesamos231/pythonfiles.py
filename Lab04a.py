"""
Author:  Myles Amos 
Course:  CSC 121
Assignment: LAB04A:  Feet to Inches
Description: Write a function named feet_to_inches that accepts a number of feet as an argument 
 returns the number of inches in that many feet.  
 Use the feet_to_inches function in a program that prompts the user to enter a n umber of feet and displays the number of inches in that many feet. 
"""
# Convert feet to inches
def feet_to_inches(feet):
    inches = feet * 12
    return inches
# Ask the user to enter the number of feet
def main():
    feet = float(input("What's the number of feet: "))
 # Change feet to inches using the feet_to_inches function
    inches = feet_to_inches(feet)
# Get the results
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == "__main__":
    main()
