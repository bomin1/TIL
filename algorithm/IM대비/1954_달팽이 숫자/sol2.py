import sys
sys.stdin = open("input.txt")

T = int(input())
# 오-아-왼-위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    arr[x][y] = 1
    d_idx = 0

    for i in range(2,n*n+1):
        x += dx[d_idx]
        y += dy[d_idx]
        arr[x][y] = i

        if 0<=x + dx[d_idx] < n and 0<=y + dy[d_idx] < n and arr[x + dx[d_idx]][y + dy[d_idx]] == 0:
            continue
        else:
            if d_idx != 3:
                d_idx += 1
            else:
                d_idx = 0
    print(arr)
