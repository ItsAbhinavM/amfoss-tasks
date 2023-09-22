for i in range(int(input())):
    var=0
    abs_number=int(input())
    for j in range(abs_number):
        if j%3==0 or j%5==0:
            var+=j
    print(var)
