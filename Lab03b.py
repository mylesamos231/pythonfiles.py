"""
Author:  Myles Amos 
Course:  CSC 121
Assignment:  Lab03B:  Rewrite For Loop as a While Loop
Description: modify this program, so that it does the same thing, but uses a while loop instead of a for loop.
"""
# Ask you how old are you
age = input("How old are you? ")
# put in your age
age = int(age)
# Tells you Happy Birthday
print("Happy Birthday To You ! ")
for i in range(age):
    print(f"Are you {i+1}")

