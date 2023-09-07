for i in range(int(input())):
    a,b=0,1
    cnt=[]
    inp=int(input())
    while inp>=a:
        cnt.append(a)
        #print(a,end=" ")
        a,b=b,a+b
        
    print(set(cnt))
    sm=0
    for i in cnt:
        if i%2==0:
            sm+=i
    print(sm)