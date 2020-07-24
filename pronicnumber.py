def pronic(n):
    for i in range(1,(n//2)+1):
        if i*(i+1)==n:
            return True
    return False
x=input()
ara=[x[i:j+1]for i in range(len(x)) for j in range(i,len(x))]
final=set()
for i in ara:
    if pronic(int(i)):
        final.add(int(i))
print(sorted(final))
