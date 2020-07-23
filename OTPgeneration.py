n=input()
s=""
for i in n:
    if int(i)%2==0:
        continue
    else:
        s+=str(int(i)**2)
print(s[:4])
