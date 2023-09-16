for i in range(int(input())):
    a,b=0,1
    counter=[]
    user_inp=int(input())
    while user_inp>=a:
        counter.append(a)
        a,b=b,a+b
    print(set(counter))
    addition=0
    for i in counter:
        if i%2==0:
            addition+=i
    print(addition)
