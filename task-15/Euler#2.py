def calculate_even_fibonacci_sum(limit):
    a,b= 0, 1
    lst= []
    
    while limit >= a:
        lst.append(a)
        a,b= b, a + b
    
    even_sum = 0
    for num in lst:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum

n = int(input("Enter the number of test cases: "))

for _ in range(n):
    k = int(input("Enter a number: "))
    result = calculate_even_fibonacci_sum(k)
    print("Sum of even Fibonacci numbers up to", k, "is:", result)
