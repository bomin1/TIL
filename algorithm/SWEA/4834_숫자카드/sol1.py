import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 카드 장 수
    N = int(input())
    # 한줄로 들어오는 숫자를 따로따로 분리
    # [4, 9, 6, 7, 9] 이런식
    numbers = list(map(int, input()))
    print(numbers)

    # 0~9(10개)까지니까 각 숫자의 갯수를 담아줄 cnt리스트 만듬
    cnt = [0] *10
    # 자기 자신에 해당하는 cnt의 idx값에 들어가서 +1 해주기
    for number in numbers:
        cnt[number] += 1
    # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    print(cnt)

    # 제일 큰 값을 cnt의 0번째로 지정하고
    max_cnt_val = cnt[0]
    # 위에서 0번째를 max_cnt_val정했으니까 1번째 인덱스부터 max_cnt_val와 값 비교
    for i in range(1, 10):
        # 카드 장수가 같은 경우도 봐줘야하니까 = 넣어야하고
        if cnt[i] >= max_cnt_val:
            # 카드 장수가 같으면 그 해당 인덱스 값을 res라는 새로운 변수에 저장
            res = i
            max_cnt_val = cnt[i]
    print("#{} {} {}".format(tc, res , max_cnt_val))

