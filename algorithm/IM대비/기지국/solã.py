import sys
sys.stdin = open("input.txt")
import pprint

T = int(input())
#우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for tc in range(1, T+1):
    n = int(input())
    arr = [[val for val in input()] for _ in range(n+1)]
    print("-----------------원본 --------------")
    pprint.pprint(arr)

    coor_a = []
    coor_b = []
    coor_c = []

    for i in range(n+1):
        for j in range(n):
            if arr[i][j] == 'A':
                coor_a.append((i,j))
            elif arr[i][j] == 'B':
                coor_b.append((i,j))
            elif arr[i][j] == 'C':
                coor_c.append((i, j))

    d_idx = 0

    for x,y in coor_a:
        for i in range(1,2):
            while True:
                next_x = x + (dx[d_idx]*i)
                next_y = y + (dy[d_idx]*i)

                if 0<=next_x<n+1 and 0<=next_y<n and arr[next_x][next_y] == 'H':
                    arr[next_x][next_y] = 'X'


                if d_idx != 3:
                    d_idx += 1
                else:
                    d_idx = 0
                    break

    print("-----------------A처리 --------------")
    pprint.pprint(arr)


    for x,y in coor_b:
        for i in range(1,3):
            while True:
                next_x = x + (dx[d_idx]*i)
                next_y = y + (dy[d_idx]*i)

                if 0<=next_x<n+1 and 0<=next_y<n and arr[next_x][next_y] == 'H':
                    arr[next_x][next_y] = 'X'


                if d_idx != 3:
                    d_idx += 1
                else:
                    d_idx = 0
                    break

    print("-----------------B처리 --------------")
    pprint.pprint(arr)



    for x,y in coor_c:
        for i in range(1,4):
            while True:
                next_x = x + (dx[d_idx]*i)
                next_y = y + (dy[d_idx]*i)

                if 0<=next_x<n+1 and 0<=next_y<n and arr[next_x][next_y] == 'H':
                    arr[next_x][next_y] = 'X'


                if d_idx != 3:
                    d_idx += 1
                else:
                    d_idx = 0
                    break

    print("-----------------B처리 --------------")
    pprint.pprint(arr)


    print("#{} ".format(tc, ))

