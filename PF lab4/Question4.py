name=input("enter your name")
fathers_name=input("enter fathers name")
rollno=int(input("enter your roll no"))
calculus=int(input("enter calculus marks"))
FIT=int(input("enter FIT marks"))
PF=int(input("enter PF marks"))
DS=int(input("enter DS marks"))
FE=int(input("enter FE marks"))

obt_marks=calculus+FIT+PF+DS+FE
percentage=obt_marks/500*100

# Function to calculate grade based on score
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
grade = calculate_grade(percentage)

print(f"student name={name}\nFathers name={fathers_name}\nsubjects=FIT Calculus PF DS FE"
      f"\nobtained_marks={obt_marks} percentage={obt_marks/500*100}% Grade={grade}")
