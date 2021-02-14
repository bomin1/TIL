import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    tot_sum = []
    # N,M 개의 숫자
    # N개의 숫자로 이루어진 A_list
    # M개의 숫자로 이루어진 B_list
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    # 갯수가 큰 리스트의 인데스가 바뀌면서 계산해야하므로 두개의 케이스로 나눠서 진행
    for i in range(abs(N-M)+1):
        res = 0
        '''
        B_list가 더 클 경우  A_list의 인덱스는 가만히 있고 B_list의 인덱스를 바꿔가면서 진행
        예를들어
        012
        01234
        (012,012)(012,123)(012,234)
        '''
        if M > N:
            for j in range((N)):
                res += A_list[j] * B_list[i+j]
            tot_sum.append(res)
        else:
            for j in range((M)):
                res += A_list[i+j] *  B_list[j]
            tot_sum.append(res)

    max_val = tot_sum[0]
    for ele in tot_sum:
        if ele > max_val:
            max_val = ele

    print("#{} {}".format(tc, max_val))