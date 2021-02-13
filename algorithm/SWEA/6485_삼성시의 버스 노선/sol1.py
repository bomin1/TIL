import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 5000개의 정류장
    count = [0] * 5001
    # 버스 노선 개수
    N = int(input())
    '''
    1 3 
    2 5
    인풋이 이런식으로 들어오는데 
    첫번째 노선은 1~3까지 모든 정류장 이동, 두번쨰 노선은 2~5까지 모든 정류장 이동.
    '''
    for i in range(N):
        A, B = input().split()
        for n in range(int(A), int(B)+1):
            # 첫번째 노선이 1~3정류장 이동하니까 1,2,3 정류장에 +1해줌
            # 두번째 노선은 2~5정류장 이동하니까 2,3,4,5 정류장 +1 해줌
            count[n] += 1

    # 각 정류장에 몇개의 노선이 다니는지?
    res = ""
    # P = 5, 즉 다섯개의 정류장 각각에 몇개의 노선이 다니는지
    P = int(input())
    for j in range(P):
        # C = 1,2,3,4,5 => 첫번째 정류장에 몇개? 두번째 정류장에 몇개 노선? ...
        C = int(input())
        res += str(count[C])
        res += ' '

    print('#{} {}'.format(tc, res))
