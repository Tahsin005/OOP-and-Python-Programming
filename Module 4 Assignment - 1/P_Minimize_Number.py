n = int(input())

arr = list(map(int, input().split()))

def function(arr):
    cnt = 0
    while True:
        for i in arr:
            if i % 2 == 1:
                return cnt
        cnt += 1
        arr = list(map(lambda v : v / 2, arr))

print(function(arr))
