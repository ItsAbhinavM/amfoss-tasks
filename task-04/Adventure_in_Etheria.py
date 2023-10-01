number=int(input())
a=input()
b=list(map(int,a.split()))
mini=min(b)
cnt=b.count(mini)
if cnt>1:
    print("Still Aetheria")
else:
    print(b.index(mini)+1)