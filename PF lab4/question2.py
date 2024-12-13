first_term=int(input("enter first term "))
diff=int(input("enter common difference "))
while True:
    n=int(input("enter the number of sequence "))
    num=first_term+(n-1)*diff
    print(f"nth number of the sequence is {num} ")
    fb=input("enter c to continue and s to stop ")
    if fb=="c":
        continue
    else:
        break