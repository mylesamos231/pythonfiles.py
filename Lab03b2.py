"""
Author:  Myles Amos 
Course:  CSC 121
Assignment:  Lab03B (While Loop Version):  Rewrite For Loop as a While Loop
Description: modify this program, so that it does the same thing, but uses a while loop instead of a for loop.
"""
age = input("How old are you? ")
age = int(age)
print("Happy Birthday To You ! ")
count = 1
while count <= age:
    print(f"Are you {count}")
    count += 1
