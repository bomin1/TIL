import sys
sys.stdin = open("input.txt")

T = int(input())

def rot(arr):
    new_arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_arr[j][n-1-i] =  arr[i][j]

    return new_arr

for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    rot_90 = rot(arr)
    rot_180 = rot(rot_90)
    rot_270 = rot(rot_180)

    # print(rot_90)
    # print(rot_180)
    # print(rot_270)
    # print(arr)

    print("#{}".format(tc))

    for i in range(n):
        print("{} {} {}".format("".join(map(str, rot_90[i])), "".join(map(str, rot_180[i])), "".join(map(str, rot_270[i]))))