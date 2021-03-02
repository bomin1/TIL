import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(x,y):
    global res

    if arr[x][y] == 3:
        res = 1
        return
    else:
        stack.append((x,y))
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0<=nx<n and 0 <= ny < n and (arr[nx][ny] == 0 or arr[nx][ny] == 3) and (nx,ny) not in stack:
                dfs(nx,ny)



for tc in range(1,T+1):
    n = int(input())
    arr = [[int(val) for val in input()] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if arr[i][j] == 2:
                x,y = i,j

    #우하좌상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    stack = []
    res = 0
    dfs(x,y)
    print("#{} {}".format(tc, res ))


