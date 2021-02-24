import sys
sys.stdin = open("input.txt")

T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for tc in range(1, T+1):
    n = int(input())
    snail = [[0 for _ in range(n)]for _ in range(n)]

    snail[0][0] = 1
    x = 0
    y = 0
    d_idx = 0

    for i in range(2, n*n+1):
        x += dx[d_idx]
        y += dy[d_idx]
        snail[x][y] = i

        if  x + dx[d_idx] < n and y + dy[d_idx] < n and snail[x + dx[d_idx]][y + dy[d_idx]] == 0:
            continue

        if d_idx != 3:
            d_idx += 1
        else:
            d_idx = 0




    print("#{} ".format(tc, ))
    for i in range(n):
        print(*snail[i])


