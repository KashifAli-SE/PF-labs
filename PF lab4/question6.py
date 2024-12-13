list1=[[1,2,3],[1,2,3],[1,2,3]]
list2=[[1,2,3],[1,2,3],[1,2,3]]
list3=[]
row=[]
for i in range(len(list1)):
    row=[]
    for j in range(len(list1)):
        row.append(list1[i][j]+list2[i][j])
    list3.append(row)

print(list3)
