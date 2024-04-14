"""
Author:Myles Amos
Date:01/30/2024
Course:  CSC 121
Assignment:  Lab02a_v1:  Area of Rectangles - Version 1
Description:  Compare the Area of Rectangles of Two Rectangles using an if/elif/else approach
"""
# Get input for the first rectangle
length1 = int(input("What is the length of the first rectangle: "))
width1 = int(input("What is the width of the first rectangle: "))
# Get input for the second rectangle
length2 = int(input("Enter the length of the second rectangle: "))
width2 = int(input("Enter the width of the second rectangle: "))
# Calculate the areas
area1 = length1 * width1
area2 = length2 * width2
# Compare areas using if/elif/else
if area1 > area2:
    print("The first rectangle has a greater area.")
elif area2 > area1:
    print("The second rectangle has a greater area.")
else:
    print("Both rectangles have the same area.")
