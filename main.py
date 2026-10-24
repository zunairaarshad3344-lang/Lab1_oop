
from course import Course,InvalidMarksError, load_course

# Task 2: Test the Course class
c = Course("Programming for AI")

c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

print("Number of students:", len(c))
print("Average:", c.average())
print("Top student:", c.top_student())

# Task 3: Test custom exception
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:",e)

print(c)

# Task 4: Load students from marks.txt
course = load_course("Programming for AI", "marks.txt")

print(course)
print("Top student:", course.top_student())

# Test missing file
try:
    load_course("Programming for AI", "mark.txt")
except FileNotFoundError as e:
    print("File error:", e)

# Task 5: Test remove_student()
c2 = Course("X")
c2.add_student("Ali", 88)

c2.remove_student("Ali")
print("Students after removal:", len(c2))

try:
    c2.remove_student("Zara")
except KeyError as e:
    print("KeyError:", e)