#printing the prime numbers upto the limit given by the user .
a=int(input("Enter the nunber here : "))
for n in range(a+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)