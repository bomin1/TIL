import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # K:이동거리 N:종점, M:충전기 설치 개수
    K,N,M = map(int,input().split())
    # station : 충전기 설치 된 정류장 번호. M만큼일거로 예상.
    station_num = list(map(int, input().split()))
    # 충전기 설치할 list
    station_lst = [0] * (N+1)

    for i in station_num:
        station_lst[i] =1
    '''
    station_lst
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    '''
    # --- 충전기 설치 완료

    cnt = 0
    origin_pos = 0 # 내 원래 위치
    now = K # K만큼 이동한 거리 (가상위치?) 한번에 갈 수있는 최대 거리 가기.
    while True:
        # 마지막 도착.
        if now >= N:
            print("#{} {}".format(tc, cnt))
            break;
        # 내가 간 자리에 충전기가 있는 경우
        if station_lst[now] == 1:
            # 충전 횟수 +1
            cnt += 1
            # 원래 위치를 지금으로 바꾸고
            origin_pos = now
            # 가상의 위치는 또 k만큼 가봄.
            now += K
        # 내가 간 위치에 정류소가 없으면
        else:
            now -= 1 # 뒤로 한칸 가서 충전소가 있느지 확인해야함
            if now == origin_pos: # 이건 종점에 도달할 수 없는 경우
                print("#{} {}".format(tc, 0))
                break

