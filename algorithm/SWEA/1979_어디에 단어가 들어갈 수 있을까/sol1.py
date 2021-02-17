import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    # 이차원 배열 만들기
    res = []
    for _ in range(n):
        res.append(list(map(int, input().split())))

    # 들어갈 수 있는 곳 : 1, 못들어감 : 0
    # 전체 들어갈 수 있는 갯수
    ans = 0

    # 가로축 찾기
    for row in range(n):
        # k개에 딱 맞는 1의 개수 구하기
        cnt = 0
        for col in range(n):
            # 1을 만나면 cnt 1씩 증가
            if res[row][col] == 1:
                cnt += 1
            # 0을 만나면
            else:
                # 만약 01110 이고 k가 3이었을 경우 위의 조건문에서 cnt가 3이 되고 들어갈 수 있으므로 최종 결과값에 +1을 해준 뒤
                if cnt == k:
                    ans += 1
                # 0을 만났으므로 다시 cnt 초기화
                cnt = 0
        # 한 행에 대해 모든 열을 다 보았을 때 cnt가 k이면 최종 결과 값에 +1
        if cnt == k:
            ans += 1

    # 세로축에서 찾기 위의 방법과 동일
    for col in range(n):
        cnt = 0
        for row in range(n):
            if res[row][col] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1

    
    print("#{} {}".format(tc, ans))

