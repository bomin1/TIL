import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(input().split())
    res = []

    half = n//2
    if n % 2 == 0:
        for i in range(half):
            res.append(arr[i])
            res.append(arr[i+half])
    else:
        n = n+1
        half = n // 2
        for i in range(half):
            if i == (half-1):
                res.append(arr[i])
                break
            else:
                res.append(arr[i])
                res.append(arr[i+half])


    print(*res)

    
    print("#{} ".format(tc, ))

