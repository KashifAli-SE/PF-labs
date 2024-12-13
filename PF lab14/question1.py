list1 = [10, 20, 30]
list2 = [2, 0, 5]  

try:
    for i in range(4):  # Index 3 will be out of range, causing an IndexError
        result = list1[i] / list2[i]
        print(f"Result of list1[{i}] / list2[{i}] is {result}")

except IndexError:
    print("IndexError: Attempted to access an index that is out of range.")
except ArithmeticError:
    print("ArithmeticError: Division by zero occurred.")
