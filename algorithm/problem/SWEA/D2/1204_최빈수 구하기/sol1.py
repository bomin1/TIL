import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    test = input()
    scores = list(map(int, input().split()))

    cnt = [0]*101

    for score in scores:
        cnt[score] += 1
    # print(cnt)
    max_cnt = max(cnt)
    # print(max_cnt)

    res = 0
    for i in range(100,-1,-1):
        if cnt[i] == max_cnt:
            res = i
            break

    
    print("#{} {}".format(tc, res))

