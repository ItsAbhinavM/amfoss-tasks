import math
var=int(input())
for i in range(var):
    n=int(input("Enter the range  : "))
    lst = []
    for item in range(1,n+1): 
        lst.append(item)
    print(math.lcm(*lst)) # prints the lcm of the numbers given in the list named lst
