import random

students = ['kashif', 'Daniyal', 'Ahad', 'Afnan', 'Agha', 'Bilal']
removed_student = students.pop(2)  # 'Charlie' will be removed
new_list = students.copy()  # Create a copy of the remaining students
scholarship_winners = random.sample(new_list, 2)

print(f'Removed student: {removed_student}')
print(f'Scholarship winners: {scholarship_winners}')
