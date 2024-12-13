str=int(input("enter starting number"))
end=int(input("enter ending number"))
for i in range(str,end):
    for j in range(1,6):
        print(i*j,end=" ")
    print()
