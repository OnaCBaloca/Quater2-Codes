# FA4.py
# Program to compute each student's average and the class average

# Ask for number of students and subjects
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

# Initialize total for class average
class_total = 0

# Loop through each student
for i in range(1, num_students + 1):
    print(f"\nStudent {i}")
    student_total = 0

    # Loop for each subject
    for j in range(1, num_subjects + 1):
        score = float(input(f"Enter score {j}: "))
        student_total += score

    # Compute and display student's average
    student_average = student_total / num_subjects
    print(f"Average for Student {i} = {student_average:.1f}")

    # Add to class total
    class_total += student_average

# Compute and display class average
class_average = class_total / num_students
print(f"\nClass Average = {class_average:.1f}")
