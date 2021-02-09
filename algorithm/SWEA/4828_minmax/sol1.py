import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 각 케이스의 양수의 갯수
    length = int(input())

    # 비교해야하는 number리스트
    numbers = list(map(int, input().split()))


    # 가장 큰 수 찾기
    max_val = numbers[0]
    for number in numbers:
        if max_val < number:
            max_val = number

    # 가장 작은 수 찾기
    min_val = numbers[0]
    for number in numbers:
        if min_val > number:
            min_val = number

    print("#{} {}".format(tc, max_val-min_val))

