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
