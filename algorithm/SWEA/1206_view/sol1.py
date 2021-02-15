import sys
sys.stdin = open("input.txt")

T = 2
# 가장 높은 층수 찾기
def max_height_func(a,b):
    if a > b:
        return a
    else:
        return b

for tc in range(1, T+1):
    # 빌딩 수
    n = int(input())
    # 빌딩의 높이
    height = list(map(int, input().split()))
    # 조망권 확보 수
    cnt = 0

    #확인 위치 양쪽 두개 비어있으니까 2부터 시작.
    i = 2
    # 마찬가지로 오른쪽 2개 비어있으므로 비교 안해줘도 됨.
    # 왼쪽에 있는 것들보다 작으면 idx 한 칸 이동, 한 칸 오른쪽 옆에 있는 빌딩보다 작으면 한 칸 이동
    while i < n-2:
        # 1. 바로 왼쪽에 있는 것들보다 작으면 다음 빌딩 확인하기
        # 2. 바로 오른쪽에 있는 것보다 작으면 다음 빌딩 확인
        if height[i-2] >= height[i] or height[i-1] >= height[i] or height[i] < height [i+1]:
            i += 1

        # 두 칸 오른쪽 옆에 있는 빌딩보다 작으면 두 칸 이동
        elif height[i] <= height[i + 2]:
            i += 2
        # 조망권 확보
        else:
            # 양 옆의 4개 비교해서 가장 높은 층수 찾기
            max_height = max_height_func(height[i - 2], max_height_func(height[i - 1], max_height_func(height[i + 1], height[i + 2])))
            # 조망권 확보 숫자 더하기
            cnt += height[i] - max_height
            # 바로 3칸 옆으로 뛰기
            i += 3

    print("#{} {}".format(tc, cnt))

