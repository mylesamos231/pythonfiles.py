"""
Author:  Myles Amos 
Course:  CSC 121
Assignment: LAB04C:   Test Average and Grade
Description: Write a program that asks the user to enter 5 test scores.  
The program should display a letter grade for each score and the average test score.  
Write and use the following functions in the program.
"""
def calc_average(scores):
    # Give the total sum of all scores
    total = sum(scores)
    # Calculate the average score by dividing the total by the number of scores
    average = sum(scores) / len(scores)
    return average

def determine_grade(score):
    # Determine the letter grade based on the given score
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return 'F'
# Enter the Test Scores for the 5 days
def main():
    test_scores = []
    # Prompt the user to enter test scores
    for i in range(1, 6):
        score = float(input(f"Enter score for test {i}: "))
        test_scores.append(score)

    # Calculate the average test score
    average_score = calc_average(test_scores)
    print("Average test score:", average_score)

    # Print the letter grade for each test score
    print("Letter grades:")
    for score in test_scores:
        grade = determine_grade(score)
        print(f"Test score: {score} - Grade: {grade}")

if __name__ == "__main__":
    main()
