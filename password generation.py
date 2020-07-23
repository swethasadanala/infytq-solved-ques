s=input().split(",")
print(s)
stt=[]
num1=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num1.append(n)
print(stt)
print(num1)
def pas(ss,n):
    l=len(ss)
    while l!=0:
        if str(l) in n :
            return ss[l-1]
        else:
            l-=1
    return "x"
for i in range(len(num1)):
    print(pas(stt[i],num1[i]),end="")
