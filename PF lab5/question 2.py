# a part
n=4
for i in range(4):
    for j in range(14):
        print("*",end="")
    print()
print()

# b part
for i in range(int(input("enter num of lines"))):
    for j in range(i):
        print("*", end="")
    print()
    
print()
#c part
n=int(input("enter number of lines"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()