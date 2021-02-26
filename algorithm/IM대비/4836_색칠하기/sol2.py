import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = [[0 for _ in range(10)] for _ in range(10)]


    for i in range(n):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x2-x1+1):
            for j in range(y2-y1+1):
                arr[x1+i][y1+j] += color


    ans = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                ans += 1
    print(ans)



