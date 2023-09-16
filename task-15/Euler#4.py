def is_palindrome(n):
    return str(n) == str(n)[::-1]
the_list=[]

for i in range(100,1000):
    for j in range(100,i+1):
        p=i*j
        if is_palindrome(p):
            the_list.append(p)
the_list.sort(reverse=True)

inp = int(input())
for _ in range(inp):
    n = int(input())
    for i in the_list:
        if i<n:
            print(i)
            break
