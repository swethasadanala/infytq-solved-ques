def groovingmonkeys(n):
  a=n
  b=[0]*len(n)
  c=0
  while(b!=n):
    c+=1
    b=[0]*len(n)
    for i in range(len(n)):
      b[n[i]-1] = a[i]
    a=b
  return c      
x=int(input())
y=int(input())
z=list(map(int,input().split()))
print(groovingmonkeys(z)) 
