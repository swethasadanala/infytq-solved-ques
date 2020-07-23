array=list(map(int,input().split(",")))
array=sorted(array)
j=[]
j.append(array[0])
j.append(array[1])
for i in range(2,len(array)):
    if j[i-1]+j[i-2] in array:
        j.append(j[i-1]+j[i-2])
    else:
        break
print(j)
