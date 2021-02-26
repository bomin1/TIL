import sys
sys.stdin = open("input.txt")
import pprint

T = int(input())
#우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check(coor_a, coor_b, coor_c, range_list):
    for x_b, y_b in coor_b:
        for i in range(1, 3):
            while True:
                next_x = x_b + (dx[d_idx] * i)
                next_y = y_b + (dy[d_idx] * i)
                if 0 <= next_x < n + 1 and 0 <= next_y < n and arr[next_x][next_y] == 'H':
                    arr[next_x][next_y] = 'X'
                if d_idx != 3:
                    d_idx += 1
                else:
                    d_idx = 0


    for x_a, y_a in coor_a:
        while True:
            next_x = x_a + dx[d_idx]
            next_y = y_a + dy[d_idx]
            if 0 <= next_x < n + 1 and 0 <= next_y < n and arr[next_x][next_y] == 'H':
                arr[next_x][next_y] = 'X'
            if d_idx != 3:
                d_idx += 1
            else:
                d_idx = 0
                break



    for x_c, y_c in coor_c:
        for i in range(1, 4):
            while True:
                next_x = x_c + (dx[d_idx] * i)
                next_y = y_c + (dy[d_idx] * i)
                if 0 <= next_x < n + 1 and 0 <= next_y < n and arr[next_x][next_y] == 'H':
                    arr[next_x][next_y] = 'X'
                if d_idx != 3:
                    d_idx += 1
                else:
                    d_idx = 0
                    break
    pprint.pprint(arr)



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


    def check(coor_a, coor_b, coor_c, range):

    # for x_b,y_b in coor_b:
    #     for i in range(1,3):
    #         while True:
    #             next_x = x_b + (dx[d_idx]*i)
    #             next_y = y_b + (dy[d_idx]*i)
    #             if 0<=next_x<n+1 and 0<=next_y<n and arr[next_x][next_y] == 'H':
    #                 arr[next_x][next_y] = 'X'
    #             if d_idx != 3:
    #                 d_idx += 1
    #             else:
    #                 d_idx = 0
    #                 break
    # pprint.pprint(arr)
    # print("-------------bb----------")
    #
    # for x_a,y_a in coor_a:
    #     while True:
    #         next_x = x_a + dx[d_idx]
    #         next_y = y_a + dy[d_idx]
    #         if 0<=next_x<n+1 and 0<=next_y<n and arr[next_x][next_y] == 'H':
    #             arr[next_x][next_y] = 'X'
    #         if d_idx != 3:
    #             d_idx += 1
    #         else:
    #             d_idx = 0
    #             break
    #
    # pprint.pprint(arr)
    # print("-----------a--------------")
    #
    # for x_c,y_c in coor_c:
    #     for i in range(1,4):
    #         while True:
    #             next_x = x_c + (dx[d_idx]*i)
    #             next_y = y_c + (dy[d_idx]*i)
    #             if 0<=next_x<n+1 and 0<=next_y<n and arr[next_x][next_y] == 'H':
    #                 arr[next_x][next_y] = 'X'
    #             if d_idx != 3:
    #                 d_idx += 1
    #             else:
    #                 d_idx = 0
    #                 break
    # pprint.pprint(arr)


    ans = 0
    for i in range(n+1):
        for j in range(n):
            if arr[i][j] == 'H':
                ans += 1
    print(ans)



