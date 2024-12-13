myfile=open("filesectionB.txt","r")
line=0
while  True:
    data=myfile.readline()
    if data:
        line+=1
    else:
        break
print(line) 