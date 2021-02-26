import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())

    arr = [[int(val) for val in input()] for _ in range(n)]

    m = n//2
    res = 0
    if i <= j:
        for i in range(n):
            for j in range(m-i,m+i+1):
                res += arr[i][j]
    else:
        for i in range(n):
            for j in range(m-(i-m),m+(i-m)+1):
                res += arr[i][j]



    print(arr)





    print("#{} ".format(tc, ))

