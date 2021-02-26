import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    k,n,m = map(int, input().split())
    chargings = list(map(int, input().split()))

    station = [0]*(n+1)

    for charge in chargings:
        station[charge] += 1

    print(station)

    next_directioin = k
    now = 0
    cnt = 0
    while True:
        if next_directioin >= n:
            print("#{} {}".format(tc, cnt))
            break
        if station[next_directioin] == 1:
            now = next_directioin
            next_directioin += k
            cnt += 1
        else:
            next_directioin-=1
            if now == next_directioin:
                print("#{} 0".format(tc,))
                break

