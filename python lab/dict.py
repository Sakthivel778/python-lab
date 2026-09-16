student = {}

student["Roll No"] = int(input("Enter Roll Number: "))
student["Name"] = input("Enter Student Name: ")
student["Department"] = input("Enter Department: ")
student["Marks"] = float(input("Enter Marks: "))

print("\nStudent Details:")

for key, value in student.items():
    print(key, ":", value)

# Add Grade
marks = student["Marks"]

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

student["Grade"] = grade

# Update marks
new_marks = float(input("\nEnter updated marks: "))
student["Marks"] = new_marks

print("\nUpdated Student Details:")

for key, value in student.items():
    print(key, ":", value)