num_students = int(input("Enter number of students: "))

for s in range(num_students):
    print("\nEntering details for student", s+1)

    name = input("Enter student name: ")
    marks_list = []

    print("\n--- Student Marks Report ---")
    print("Subject\tMarks")

    for i in range(5):
        marks = int(input("Subject " + str(i+1) + ": "))
        marks_list.append(marks)

    total = sum(marks_list)
    average = total / 5

    # Grade calculation
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Final report for each student
    print("\n--- Report for", name, "---")
    for i in range(5):
        print("Subject", i+1, ":", marks_list[i])

    print("------------------")
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)



"""
Example Output:

Enter number of students: 1

Entering details for student 1
Enter student name: Akshaya

--- Student Marks Report ---
Subject    Marks
Subject 1: 80
Subject 2: 90
Subject 3: 85
Subject 4: 95
Subject 5: 88

--- Report for Akshaya ---
Subject 1 : 80
Subject 2 : 90
Subject 3 : 85
Subject 4 : 95
Subject 5 : 88
------------------
Total: 438
Average: 87.6
Grade: B
"""


