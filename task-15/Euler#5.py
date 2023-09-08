import math
t=int(input())
for i in range(t):
    n=int(input())
    lst = []
    for item in range(1,n+1): 
        lst.append(item)
    print(math.lcm(*lst))