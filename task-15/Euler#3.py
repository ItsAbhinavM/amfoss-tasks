for i in range(int(input())):
    a=int(input("Enter the number here : "))
    cnt=[]
    for i in range(2,a+1):
        if a%i==0:
            cnt.append(i)
            a=a//2
    print(max(cnt))