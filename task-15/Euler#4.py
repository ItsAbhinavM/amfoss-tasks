def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindromic_products(limit):
    palindrome_products = []
    for i in range(100, limit):
        for j in range(100, i + 1):
            product = i * j
            if is_palindrome(product):
                palindrome_products.append(product)
    palindrome_products.sort(reverse=True)
    return palindrome_products

def main():
    the_list = find_palindromic_products(1000)
    
    inp = int(input())
    for _ in range(inp):
        n = int(input())
        for i in the_list:
            if i < n:
                print(i)
                break

main()
