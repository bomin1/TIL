import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n,m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            res = 0
            for row in range(m):
                for col in range(m):
                    res += arr[i+row][j+col]
            ans.append(res)
    print(ans)
    print(max(ans))


