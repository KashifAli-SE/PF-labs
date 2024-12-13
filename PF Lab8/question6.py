def month(n):
    months="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
    months_list=months.split(" ")
    print(months_list[n-1])
    
n=int(input("enter the month number "))
month(n)


