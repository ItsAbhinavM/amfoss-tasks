for i in range(int(input())):
    j=0
    a=abs(int(input()))
    for i in range(a):
        if i%3==0 or i%5==0:
            j+=i
    print(j)
