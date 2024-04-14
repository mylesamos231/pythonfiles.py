"""
Author:  Myles Amos 
Course:  CSC 121
Assignment: LAB04B: Random Counter
Description: The function should use a loop and generates 100 random numbers. 
 In the loop  keeps a count of how many of those random numbers are even, and how many of them are odd.  
 (Hint:  remember the modulus function to determine a number is even or odd.  Also remember to import random). 
The function should be a void function and not return anything, but should instead print out the number of even and odd numbers found after the loop ends.
"""
import random

def random_counter():
    even_count = 0
    odd_count = 0
    
    for _ in range(100):
        random_number = random.randint(1, 1000)
        if random_number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")

def main():
    random_counter()

if __name__ == "__main__":
    main()

