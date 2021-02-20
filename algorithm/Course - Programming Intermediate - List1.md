# Course - Programming Intermediate - List1



## 1. min_max

```python
import sys
sys.stdin = open("input.txt")

'''
-------- 내장함수 -----------
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    print("#{} {}" .format(tc, max(arr) - min(arr)))
------------------------------
'''

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    mx = arr[0]
    mn = arr[0]
```



## 2. 전기버스

```python
T = int(input())

for tc in range(1,T+1):

    # k: 최대한 이동 가능 거리, n: 종점번호, m : 충전기가 설치된 정류장 번호개수
    k,n,m = map(int, input().split())
    # 종점까지 포함한 정류장을 의미하는 list
    bus_stop = [0]*(n+1)
    charge_stations = map(int, input().split())

    for charge_station in charge_stations:
        bus_stop[charge_station] += 1

    # 이게 내 현재 위치
    my_direction = 0
    # 정찰병 느낌?
    next_direction = k
    cnt = 0
    while True:
        # 만약 충전기가 있는 정류장 이라면 내 위치가 지금 정찰병 위치로
        if bus_stop[next_direction] == 1:
            my_direction = next_direction
            next_direction += k
            cnt += 1
            if next_direction >= n:
                break
        else:
            next_direction -= 1
            if next_direction == my_direction:
                cnt = 0
                break
    print("#{} {}".format(tc, cnt))

```



## 3. 숫자 카드

```PYTHON
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    cnt = [0]*10
    n = int(input())
    numbers = [int(val) for val in input()]

    for i in numbers:
        cnt[i] += 1


    # cnt의 인덱스와 그 인덱스의 값 출력
    mx = 0
    for i in range(len(cnt)):
        # 같은 값이 있을 수도 있으니까 무조건 = 들어가야함
        if cnt[i] >= mx:
            mx = cnt[i]
            res_idx = i

    print('#{} {} {}'.format(tc, res_idx, cnt[res_idx]))

```



## 4. 구간합

```		PYTHON
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr =list(map(int, input().split()))

    ans = []
    for i in range(n-m+1):
        res = 0
        for j in range(m):
            res += arr[i+j]
        ans.append(res)
    print(max(ans) - min(ans))

```

