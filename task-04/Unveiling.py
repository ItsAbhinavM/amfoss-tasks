num_tests = int(input())

for _ in range(num_tests):
    a = "amfoss"
    s = input().lower()
    count = 0
    for i in range(len(a)):
        if a[i] != s[i]:
            count += 1
    print(count)