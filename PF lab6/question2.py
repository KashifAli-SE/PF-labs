from math import *

def calculate_height(angle, length):
    angle_in_radians = pi * (angle / 180)
    height = length * sin(angle_in_radians)
    return height


angle = int(input("Enter angle in degrees: "))
length = int(input("Enter length: "))
height = calculate_height(angle, length)
print(f"Height = {height}")
