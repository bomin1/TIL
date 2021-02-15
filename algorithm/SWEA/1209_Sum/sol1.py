import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    a = int(input())
    arr = []
    # a = list(map(int, input().split()))
    # 비어 있는 리스트를 100x100으로 만들기
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    # 각 행, 열 대각선들의 합을 담을 리스트
    res = []
    # 행 순회
    # 행에 해당하는 row는 가만히 있고 col이 증가해야하므로 row가 가장 바깥족 for문
    for row in range(len(arr)):
        sum_row = 0
        for col in range(len(arr[row])):
            sum_row += arr[row][col]
        res.append(sum_row)

    # 열 순회
    for col in range(len(arr[0])):
        sum_col = 0
        for row in range(len(arr)):
            sum_col += arr[row][col]
        res.append(sum_col)

    # 대각선 순회
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0

    for i in range(len(arr)):
        sum_diagonal_1 += arr[i][i]
        sum_diagonal_2 += arr[i][99-i]
    res.append(sum_diagonal_1)
    res.append(sum_diagonal_2)


    max_val = res[0]
    for ele in res:
        if ele > max_val:
            max_val = ele

    print("#{} {}".format(tc, max_val))

