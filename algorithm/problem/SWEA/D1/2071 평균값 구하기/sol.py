import sys
sys.stdin  = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    res = round(sum(arr)/len(arr))

    print("#{} {}".format(tc, res))
