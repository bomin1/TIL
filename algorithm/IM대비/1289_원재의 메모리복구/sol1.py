import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    string = list(input())
    res = ['0']*len(string)

    print(string)
    print(res)

    cnt = 0
    for i in range(len(res)):
        if res[i] != string[i]:
            res[i:] = string[i]*(len(res)-i)
            cnt += 1

    print("#{} {}".format(tc, cnt))

