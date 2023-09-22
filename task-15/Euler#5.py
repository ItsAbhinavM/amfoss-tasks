import math
for i in range(int(input())):
    n=int(input())
    lst = []
    for j in range(1,n+1): 
        lst.append(j)
    print(math.lcm(*lst))
