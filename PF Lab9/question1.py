# 1. sWrite a program which will add your best five students name in a set. You will use a loop
# to insert names in set.

students=set()
for i in range(5):
    name=input("Enter the name of student: ")
    students.add(name)
print(students)
