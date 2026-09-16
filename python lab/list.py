n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input(f"Enter student {i + 1} name: ")
    students.append(name)

print("\nOriginal List:", students)

# Add a student
new_student = input("Enter a student name to add: ")
students.append(new_student)

# Insert a student
insert_name = input("Enter a student name to insert: ")
position = int(input("Enter position (0-based index): "))

students.insert(position, insert_name)

# Remove a student
remove_name = input("Enter student name to remove: ")

if remove_name in students:
    students.remove(remove_name)
else:
    print("Student not found!")

# Sort list
students.sort()

print("Final Student List:", students)
print("Total Students:", len(students))