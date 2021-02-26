import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n,m = map(int, input().split())
    box = []
    res = 0
    # 이차원 배열 만들기
    for i in range(n):
        box.append(list(map(int, input().split())))
    # 전체 박스 접근
    for row in range(n-m+1):
        for col in range(n-m+1): # 정사각형이니까 범위 똑같이
            hit = 0
            # 파리채 부분 m*m 접근
            for k in range(m):
                for l in range(m):
                    # 오른쪽으로 이동히면서 보는 느낌?
                    hit += box[row+k][col+l]
            if res < hit:
                res = hit

    print("#{} {}".format(tc,res ))

