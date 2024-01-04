t = int(input())
while t != 0:
    values = input().split()
    x = int(values[0])
    y = int(values[1])
    # x, y = map(int, input().split())
    sum = 0
    if x > y:
        for i in range(y + 1, x):
            if i & 1:
                sum += i
        
        print(sum)
    elif x <= y:
        for i in range(x + 1, y):
            if i & 1:
                sum += i
        
        print(sum)

    t -= 1