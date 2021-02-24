import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    arr = list(map(int, input().split()))
    res = 0
    for ele in arr:
        if ele % 2:
            res += ele
    
    print("#{} {}".format(tc, res))

