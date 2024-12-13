'''''
2.   A dartboard of radius 10 and the wall it is hanging on are represented using the two dimensional coordinate 
system, with the board’s center at coordinate (0; 0). Variables x and y store the x- and y-coordinate of a hit. 
Write an expression using variables x and y that evaluates to True if the dart hits (is within) the dartboard, 
and evaluate the expression for these dart coordinates:
(a) (0; 0)
(b) (10; 10) (c) (6; 6)
(d) (7; 8)'''''




from math import *
r=10 #radius
x,y=0,0
x1,y1=0,0 #centre(x1,y1)
eq_of_circle= x**2+y**2-r**2

x2=int(input("enter x co-ordinate of point hitted "))
y2=int(input("enter y co-ordinate of point hitted "))

#checking whether the point lies on the the dartboard or not
if (x2**2+y2**2)<=r**2:
    print("the dart hitted on the board")
elif  x2**2+y2**2>r**2:
    print("the dart hitted outside the board")
    
