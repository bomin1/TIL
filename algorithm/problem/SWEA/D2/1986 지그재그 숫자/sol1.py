import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    res = 0
    for i in range(0,n):
        # 홀수
        if (i+1) % 2:
            res += i+1
        # 짝수
        else:
            res -= i+1

    print("#{} {}".format(tc, res))

