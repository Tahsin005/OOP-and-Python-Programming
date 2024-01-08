t = int(input())
while t != 0:
    n = int(input())
    s = input()
    plus = 0
    minus = 0
    for i in s:
        if i == '+':
            plus += 1
        elif i == '-':
            minus += 1
    ans = (n - (2 * (min(plus,minus))))
    print(ans)
    t -= 1