import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 10*10 mat.
    arr = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(n):
        # 좌표 받아오기
        x1, y1, x2, y2, color = map(int, input().split())
        # 가로 세로 길이만큼 해당 영역에 색칠해주기
        # 가로 방향으로 색이 칠해지는 중
        for i in range(x2-x1+1):
            for j in range(y2-y1+1):
                arr[x1+i][y1+j] += color

    # 파란색과 빨간색이 같이 칠해져야하므로 빨강 + 파랑 = 3, 빨강 + 빨강 + 파랑일 수도 있으니까 3이상으로 조건식 지정
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                cnt += 1

    print("#{} {}".format(tc, cnt))

