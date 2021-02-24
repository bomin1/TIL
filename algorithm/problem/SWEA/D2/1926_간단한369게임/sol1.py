import sys
sys.stdin = open("input.txt")

T = 1

for tc in range(1, T+1):
    n = int(input())

    res = []
    for i in range(1, n+1):
        res.append(str(i))

    ans = []
    cnt = 0

    for check in res:
        if check.count('3') != 0 or check.count('6') != 0 or check.count('9') != 0:
            cnt_3 = check.count('3')
            cnt_6 = check.count('6')
            cnt_9 = check.count('9')

            clap  = '-'*(cnt_3+cnt_6+cnt_9)
            ans.append(clap)

        else:
            ans.append(check)


    print(*ans)
