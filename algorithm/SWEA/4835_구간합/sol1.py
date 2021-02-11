T = int(input())
for tc in range(1, T+1):
    # N : N개의 정수
    # M : M개 선택하기
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    res_lst = []
    # N-M+1만큼 반복문을 도는 작업이 필요하다.
    for i in range(N-M+1):
        res = 0
        for j in range(M):
            res += numbers[i+j]
        res_lst.append(res)

    max_val = res_lst[0]
    for res_ele in res_lst:
       if res_ele >  max_val:
           max_val = res_ele

    min_val = res_lst[0]
    for res_ele in res_lst:
        if res_ele < min_val:
            min_val = res_ele


    print("#{} {}".format(tc,max_val- min_val))