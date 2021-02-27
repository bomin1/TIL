import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n,k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    v_arr = list(zip(*arr))
    # 들어갈 수 있는 곳이 1 못들어가는 곳은 0

    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1
    # print(ans)


    for i in range(n):
        cnt = 0
        for j in range(n):
            if v_arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1


    print("#{} {}".format(tc,ans ))

