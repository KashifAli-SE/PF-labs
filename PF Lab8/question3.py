# 3.   Write function even() that takes a positive integer n as input and prints on the screen all 
# numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
# >>> even(17)
# 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,

def even(n):
    for i in range(2, n+1):
        if i % 2 == 0 or i % 3 == 0:
            print(i, end=', ')
            
n = int(input("Enter a positive integer: "))
even(n)