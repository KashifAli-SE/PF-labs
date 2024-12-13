N=[66,84,24,72,56]
D=[2,0,4,0,6,0]
for i in range(len(N)):
    try:
        result=N[i]/D[i]
        print("last element of N is: ",N[6])
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed",N[i],"/",D[i])
    except IndexError:
        print("cant divide by zero in denominator", N[i],"/",D[i])
    else:
        print(result)
    finally:
        print("Finally it is last lab")
        
