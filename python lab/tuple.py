m = int(input("Enter number of marks: "))

marks_list = []

for i in range(m):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks_list.append(mark)

# Convert List into Tuple
marks = tuple(marks_list)

print("\nMarks Tuple:", marks)
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Total Marks:", sum(marks))
print("Average Mark:", sum(marks) / len(marks))
