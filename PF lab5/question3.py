def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n

n=0
while n <11:
    print(f"factorial of {n} = {fact(n)}")
    n+=1