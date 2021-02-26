import sys
sys.stdin = open("input.txt")
T = int(input())

def omok(n, arr):
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 'o':
                # continue
            # 오른쪽으로
                if y + 4 < n and five_check(arr, 0, 1, x, y):
                    return 'YES'
                # 오른쪽 밑에
                if x + 4 < n and y + 4 < n and five_check(arr, 1, 1, x, y):
                    return 'YES'
                # 그냥 아래
                if x + 4 < n and five_check(arr, 1, 0, x, y):
                    return 'YES'
                # 좌측 아래
                if x + 4 < n and y - 4 >=0 and five_check(arr, 1, -1, x, y):
                    return 'YES'
    return 'NO'

def five_check(arr, dx, dy, x, y):
    for i in range(1,5):
        if arr[x+(dx*i)][y+(dy*i)] != 'o':
            return False
    return True

for tc in range(1, T+1):
    n = int(input())
    arr = [[val for val in input()] for _ in range(n)]

    res = omok(n, arr)
    print(res)