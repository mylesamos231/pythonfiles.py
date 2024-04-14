"""
Author:Myles Amos
Date:01/30/2024
Assignment:Lab02a_v2:  Area of Rectangles - Version 2
Description: Create nested if statement
"""
# Get input for the first rectangle
length1 = int(input("What is the length of the first rectangle?:"))
width1 = int(input("What is the width of the first rectangle?:"))
# Get input for the second rectangle
length2 = int(input("What is the length of the second rectangle: "))
width2 = int(input("What is the width of the second rectangle: "))
# Calculate areas
area1 = length1 * width1
area2 = length2 * width2
# Compare areas using max and a conditional expression
result = ("The first rectangle has a greater area." if area1 > area2
else "The second rectangle has a greater area." if area2 > area1
else "Both rectangles have the same area.")
print(result)