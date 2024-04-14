"""
Author:  Myles Amos 
Course:  CSC 121
Assignment:  Lab03A:  The Bug Collector Problem
Description: A bug collector collects bugs for five days. 
 Write a program that keeps a running total of the number of bugs collected during the five days.  
 The loop should ask for the number of bugs collected each day, and when the loop is finished, the program should display the total number of bugs collected.  
"""
total_bugs = 0
 # This is the days you are collecting the bugs
for day in range(1, 6):
 # Ask How many bugs are collected from day 1-5
        bugs_collected = int(input(f"How many bugs you collected on day {day}?: ")) 
# Total amount of bugs collected
        total_bugs += bugs_collected
print(f"\n You collected {total_bugs} in five days")