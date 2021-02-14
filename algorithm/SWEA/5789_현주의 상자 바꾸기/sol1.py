import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # N개의 상자 초기값은 0
    cnt = [0] * N

# i번째 작업에 대해 L~R을 i로 변경
    for i in range(1,Q+1):
        L,R = map(int, input().split())
        for j in range(L, R+1):
            cnt[j-1] = i

    print('#{} {}'.format(tc, " ".join(map(str, cnt))))
