import sys
sys.stdin = open("input.txt")
import pprint

T = int(input())

#우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check(arr, coor, range_list, d_idx):
    for x_b, y_b in coor:
        for i in range_list:
            while True:
                next_x = x_b + (dx[d_idx] * i)
                next_y = y_b + (dy[d_idx] * i)
                if 0 <= next_x < n + 1 and 0 <= next_y < n and arr[next_x][next_y] == 'H':
                    arr[next_x][next_y] = 'X'
                if d_idx != 3:
                    d_idx += 1
                else:
                    d_idx = 0
                    break
    return arr

for tc in range(1, T+1):

    n = int(input())
    arr = [[val for val in input()] for _ in range(n+1)]
    pprint.pprint(arr)
    print("----------원본 ----------")

    d_idx = 0
    coor_a = []
    coor_b = []
    coor_c = []
    for i in range(n+1):
        for j in range(n):
            if arr[i][j] == 'A':
                coor_a.append((i,j))
            elif arr[i][j] == 'B':
                coor_b.append((i, j))
            elif arr[i][j] == 'C':
                coor_c.append((i, j))

    range_list_a = [1]
    range_list__b = [1,2]
    range_list_c = [1,2,3]
    res = check(arr, coor_a, range_list_a, d_idx)
    res1 = check(res, coor_b, range_list__b, d_idx)
    res2 = check(res1, coor_c, range_list_c, d_idx)

    ans = 0
    for i in range(n+1):
        for j in range(n):
            if res2[i][j] == 'H':
                ans += 1
    pprint.pprint(res2)
    print(ans)
