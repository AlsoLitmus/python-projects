students = {}

while True:
  name = input("Enter student name (or 'q' to quit): ")
  if name == 'q':
    break

  grade = float(input("Enter grade: "))
  students[name] = grade

average = sum(students.value()) / len(students)
print("Class average:", average)