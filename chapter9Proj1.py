# Dictionary containing course numbers and room numbers
room_numbers = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}

# Dictionary containing course numbers and instructors
instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

# Dictionary containing course numbers and meeting times
meeting_times = {
    'CS101': '8:00am',
    'CS102': '9:00am',
    'CS103': '10:00am',
    'NT110': '11:00am',
    'CM241': '1:00pm'
}

# Get user input for course number
course_number = input("Enter a class name:")

# Check if the course number is in the dictionaries
if course_number in room_numbers and course_number in instructors and course_number in meeting_times:
    print("Class:", course_number)
    print("Room:", room_numbers[course_number])
    print("Instructor:", instructors[course_number])
    print("Time:", meeting_times[course_number])
else:
    print("Invalid course number.")
