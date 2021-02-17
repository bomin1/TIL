import sys
sys.stdin = open("input.txt")

T = 2

for tc in range(1, T+1):
    # 덤프 횟수
    # boxes 박스들의 각각 높이
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 박스 높이는 100이 최대니까 해당 높이의 박스가 몇개 있는지 세는 리스트
    box_count = [0 for i in range(101)]
    # 최대 최소를 찾아 나가야하니까 제일 작은 값을 max로 초기화, 제일 큰 값을 min으로 초기화
    max_val = 1
    min_val = 100

    for i in range(100):
        # 해당 높이의 idx에 접근해서 +1 해주고
        box_count[boxes[i]] += 1
        # 최대 높이와 최소 높이를 찾아 나간다.
        if boxes[i] > max_val:
            max_val = boxes[i]
        if boxes[i] < min_val:
            min_val = boxes[i]


    while dump > 0:
        # 가장 작은 높이에 있는 박스에 하나가 추가되니까 원래 값에는 -1
        box_count[min_val] -= 1
        # 하나가 추가되니까 상자의 개수가 하나 들어난 상태이므로 +1
        box_count[min_val +1] += 1
        '''
        예를들어 높이가 1인 상자가 2개 2인 상자가 3개가 있을때 
        가장 높은 곳에서 낮은곳인 (높이 = 1)로 상자를 보내면
        높이가 1인 상자는 1개가 되고 (box_count[min_val] -= 1)
        높이가 2인 상자는 3개가 된다.( box_count[min_val +1] += 1)
        '''
        # 위와 동일한 원리
        # 박스를 하나 내리니까 원래값은 감소하고 max 값보다 하나 작은 값이 +1
        box_count[max_val] -= 1
        box_count[max_val -1] += 1

        # 가장 낮은 값이 없다면 다음 값을 가장 낮은 값으로 지정
        if box_count[min_val] == 0:
            min_val += 1
        # 가장 높은 값이 없다면 그 전 값을 가장 높은 값으로 지정
        if box_count[max_val] == 0:
            max_val -= 1

        dump -= 1

        res = max_val - min_val

    print("#{} {}".format(tc,res ))
