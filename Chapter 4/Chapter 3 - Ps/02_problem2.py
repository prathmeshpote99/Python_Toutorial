# Write a program to accept marks of 6 students and display them in a sorted manner

marks = []

f1 = int(input("Enter mark for student 1: "))
marks.append(f1)
f2 = int(input("Enter mark for student 2: "))
marks.append(f2)
f3 = int(input("Enter mark for student 3: "))
marks.append(f3)
f4 = int(input("Enter mark for student 4: "))
marks.append(f4)
f5 = int(input("Enter mark for student 5: "))
marks.append(f5)
f6 = int(input("Enter mark for student 6: "))
marks.append(f6)

marks.sort()
print(marks)