test = int(input())
while test != 0:
    n = (input())
    rev = n[::-1]
    for _ in range(len(rev)):
        print(rev[_], end = " ")
    print()
    test -= 1