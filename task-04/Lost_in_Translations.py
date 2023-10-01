a=input()
a=a.lower()
right="hello"
b=len(a)
j=0
cnt=0
for i in a:
    if j<len(right) and i==right[j]:
        j+=1
        cnt+=1
    else:
        continue
if cnt==5:
    print("YES")
else:

    print("NO")