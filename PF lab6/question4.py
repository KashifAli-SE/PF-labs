monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')
# (a) Insert 'Apr' between 'Mar' and 'May'
monthsL.insert(3, 'Apr')
# (b) Append 'Jun'
monthsL.append('Jun')
# (c) Pop the last element
monthsL.pop()
# (d) Remove the second item
monthsL.pop(1)
# (e) Reverse the order
monthsL.reverse()
monthsL.sort()

# functions on tuple will through errors
# (a) Insert 'Apr' between 'Mar' and 'May'
# monthsT.insert(3, 'Apr')
# # (b) Append 'Jun'
# monthsT.append('Jun')
# # (c) Pop the last element
# monthsT.pop()
# # (d) Remove the second item
# monthsT.pop(1)
# # (e) Reverse the order
# monthsT.reverse()
# monthsT.sort()
# print("Final tuple:", monthsT)
print("Final list:", monthsL)