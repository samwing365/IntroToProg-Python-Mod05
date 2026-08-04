# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Sam Nguyen, 7/28/26, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str ="" # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
file = open(FILE_NAME, "r")
data = json.load(file)
file.close()



# Check if a file object exists and is still open
if file is not None and file.closed == False:
    file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")


        student_data = {"student_first_name": student_first_name,"student_last_name": student_last_name,"course_name": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        #added for __ in __
        print("-" * 50)
        for student in students:
            print(
                f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        json.dump(students, file, indent=4)
        file.close()

        # Check if a file object exists and is still open
        if file is not None and file.closed == False:
            file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")