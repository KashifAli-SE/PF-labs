list=[1,2,3,4,5,6,7,8,9]
# (a) Find the index of the middle element of lst
middle_index = len(list) // 2

# (b) Access the middle element of lst
middle_element = list[middle_index]

# (c) Sort lst in descending order
list=[1,2,3,4,5,6,7,8,9]
list.sort(reverse=True)
print(list)


# (d) Remove the first element and place it at the end of lst
list=[1,2,3,4,5,6,7,8,9]
list.append(list.pop(0))
print(list)
