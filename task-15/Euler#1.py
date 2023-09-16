for i in range(int(input())):
    var=0
    abs_number=abs(int(input()))
    for j in range(abs_number):
        if i%3==0 or i%5==0:
            var+=i
        else:
            continue
    print(var)
