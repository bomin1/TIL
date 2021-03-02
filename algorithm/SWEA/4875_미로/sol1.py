import sys
sys.stdin = open("input.txt")

T = int(input())
#우하좌상
dx = [0, 1, 0, -1]
dy = [1,0,-1,0]

for tc in range(1, T+1):
    n = int(input())
    arr = [[int(val) for val in input()] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if arr[i][j] == 2:
                start = (i,j)
    # print(arr)
    stack=[start]
    ans = 0
    # print(stack)
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    arr[nx][ny] = -1
                elif arr[nx][ny] == 3:
                    ans = 1
                    stack.clear()
                    break

    print("#{} {}".format(tc, ans ))

