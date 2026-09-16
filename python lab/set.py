count1 = int(input("Enter number of subjects in Set 1: "))

subjects1 = set()

for i in range(count1):
    subject = input(f"Enter subject {i + 1}: ")
    subjects1.add(subject)

count2 = int(input("\nEnter number of subjects in Set 2: "))

subjects2 = set()

for i in range(count2):
    subject = input(f"Enter subject {i + 1}: ")
    subjects2.add(subject)

print("\nSet 1:", subjects1)
print("Set 2:", subjects2)

print("Union:", subjects1.union(subjects2))
print("Intersection:", subjects1.intersection(subjects2))
print("Difference (Set 1 - Set 2):",subjects1.difference(subjects2))
