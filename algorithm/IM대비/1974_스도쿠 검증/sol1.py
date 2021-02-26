import sys
sys.stdin = open("input.txt")

T = int(input())

def sudoku(arr):

    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
            if cnt[arr[i][j]] != 1:
                return 0

    for j in range(9):
        cnt = [0] * 10
        for i in range(9):
            cnt[arr[i][j]] += 1
            if cnt[arr[i][j]] != 1:
                return 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            cnt =[0]*10
            for row in range(3):
                for col in range(3):
                    cnt[arr[i+row][j+col]]+=1
                    if cnt[arr[i+row][j+col]] != 1:
                        return 0
    return 1

for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]
    res = sudoku(arr)

    print("#{} {}".format(tc, res))

