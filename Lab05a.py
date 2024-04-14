'''
Name:Myles Amos 
Date:02/27/2024
Description: Write a python program that opens a file, 
reads all of the lines into a list of strings, and closes the file. 
Use the readlines() method or a for loop.
'''
import random

myNames = []
myTitles = []
myDescriptors = []

def main():
    with open('names.txt', 'r') as fNames:
        for line in fNames:
            line = line.replace("\n", "")  
            myNames.append(line)

    with open('titles.txt', 'r') as fTitles:
        for line in fTitles:
            line = line.replace("\n", "")  
            myTitles.append(line)

    with open('descriptors.txt', 'r') as fdescriptors:
        for line in fdescriptors:
            line = line.replace("\n", "") 
            myDescriptors.append(line)

    fTitles = random.choice(myTitles).strip()
    fNames = random.choice(myNames).strip()
    fdescriptors = random.choice(myDescriptors).strip()

    random_name = f"{fTitles} {fNames} the {fdescriptors}"
    print(random_name)

if __name__ == "__main__":
    main()
