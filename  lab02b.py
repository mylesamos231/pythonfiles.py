"""
Name:Myles Amos
Date:02/01/2024
Description: Write a program named lab02b.py that asks a user to enter a person's age.
"""
# Get the person's age
Age = int(input ("what is your age?"))
# Use if/elif/else statement to find out which age range the pereson is
# An error occurs cause a person cannot have an negetative number
if Age <= 0:
    print("Error: A person cannot have a negative age.")
#greater than 1 but less than 13 years old
elif Age <= 1:
    print("This person is an infant.")
#If at least 13 but less than 20 years old
elif Age <= 13:
    print("This person is a child.")
#If at least 20 but less than 100 years old
elif Age <= 20:
    print("This person is a teenager.")
#If at least 100 years old
elif Age <= 100:
    print("This person is an adult.")
#Over 100
else: 
    print("This person is a centenarian.")

