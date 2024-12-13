lis=[1,2,3,4,5,6,7,8]
lis.sort()
lis.pop()
del lis[0]
lis.remove(5)
lis.insert(8,8)
tup2=(9,10,11)
lis.extend(list(tup2))
print(lis)