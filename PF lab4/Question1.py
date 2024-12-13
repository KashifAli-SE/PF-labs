# 1.	Write a program which solves the quadratic equation. The user will enter the value of a, b 
# and c. The program will then check the denominator that if denominator is zero or not. If its zero 
# it can reply the equation cannot solve as there is a zero division else, it will execute the
# program and will generate two solutions.

from math import *
a=int(input("enter value of a "))
b=int(input("enter value of b"))
c= int(input("enter value of c"))
x1,x2=0,0
if a==0:
    print("equation can not be solved due to zero division error")
else:
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(f"the roots of equation are {x1} and {x2}")