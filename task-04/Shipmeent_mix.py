def finding_missing_number(numbers):
    for i in range(len(numbers) + 1):
        if i not in numbers:
            return i

def main():
    num= int(input())
    for j in range(num):
        n = int(input())
        lst = list(map(int, input().split()))
        a = []
        b = []

        def separate_numbers(lst,a,b):
            while lst:
                mini= min(lst)
                if not a or mini - 1 == a[-1]:
                    k=lst.index(mini)
                    a.append(lst.pop(k))
                else:
                    q=lst.index(mini)
                    b.append(lst.pop(q))
    
            return a, b
        separate_numbers(lst,a,b)
        n1 = finding_missing_number(a)
        n2 = finding_missing_number(b)
        print(n1 + n2)
main()