import sys
sys.stdin = open("input.txt")

T = int(input())

# 좌측 위 부터 판별
# dx =[-1,-1,-1,0,0,1,1,1]
# dy =[-1,0,1,-1,1,-1,0,1]

def find(field, n):
    for x in range(n):
        for y in range(n):
            if field[x][y] != 'o':
                continue
            # 오른쪽 체크
            if y + 4 < n and five_check(field, 0, 1, x, y):
                return 'YES'
            # 아래쪽
            if x + 4 < n and five_check(field, 1, 0, x, y):
                return 'YES'
            # 오른쪽 하단
            if x + 4 < n and y +4 < n and five_check(field, 1, 1, x, y):
                return 'YES'
            # 왼쪽 하단
            if x +4 < n and y -4 < n and five_check(field, 1, -1, x, y):
                return 'YES'
    return 'NO'

def five_check(field, dx,dy, x, y):
    for z in range(1,5):
        if field[x+(dx*z)][y+(dy*z)] != 'o':
            return False
    return True



for tc in range(1, T+1):
    n = int(input())

    field = [[val for val in input()] for _ in range(n)]

    res = find(field, n)
    print(res)






    # print("#{} ".format(tc, ))

