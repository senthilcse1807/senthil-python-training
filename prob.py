no_of_students = int(input("Enter number of students: "))

total = 0
passed_students = 0
failed_students = 0
students = 0  

for student_index in range(1, no_of_students + 1):
    mark = int(input("Enter marks for student : "))
    if mark < 0 or mark > 100:
        print("Invalid marks")

    total += mark 
    students += 1

    if mark >= 40:
        passed_students += 1
    else:
        failed_students += 1

if students > 0:
    average= total / students
else:
    average = 0


print("Total Marks: ", total)
print("Average Marks: ", average)
print("Passed Students: ", passed_students)
print("Failed Students: ", failed_students)

