import sys
sys.stdin = open("input.txt")

T = int(input())

def bread(sec, order):
    for time in sec:
        if time == 0:
            return 'Impossible'
        else:
            # 내가 만들기 전에 손님이 온 경우
            # 손님 : 30초에오고 내가 31초에 다 만드느 경우
            if time < m:
                return 'Impossible'
            else:
                cnt = (time // m)*k - order
                if cnt <= 0:
                    return 'Impossible'
                else:
                    order += 1

        if order == n:
            return 'Possible'

for tc in range(1, T+1):
    #n 명의 사람에게 팔고
    # m초 동안
    # k개 만들 수 있음
    n,m,k = map(int, input().split())

    # 각 사람들이 도착하는 초(n명의 사람이니까 n개 있음)
    sec = sorted(list(map(int, input().split())))
    # 손님 순서
    order = 0

    res = bread(sec, order)
    print("#{} {}".format(tc, res))


