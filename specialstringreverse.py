s=input()
d=dict()
rev=""
for i in range(len(s)):
    if s[i].isalnum()==False:
        d.update({1:s[i]})
    else:
        rev+=s[i]
rev=list(rev[::-1])
for i,j in d.items():
    rev.insert(i,j)
print("".join(rev))
