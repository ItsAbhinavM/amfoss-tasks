xcount=[]
ycount=[]
zcount=[]
for i in range(int(input())):
    x,y,z=map(int,input().split())
    xcount.append(x)
    ycount.append(y)
    zcount.append(z)
xc=sum(xcount)
yc=sum(ycount)
zc=sum(zcount)
if xc==yc==zc==0:
    print("YES")
else:
    print("NO")