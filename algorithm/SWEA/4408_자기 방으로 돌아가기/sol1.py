import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    cnt = [0]*201
    n = int(input())

    for _ in range(n):
        s_e = sorted(list(map(int, input().split())))
        start = s_e[0]
        end = s_e[1]

        for i in range((start+1)//2, ((end+1)//2)+1):
            cnt[i] += 1
    # print(cnt)
    print("#{} {}".format(tc,max(cnt) ))

