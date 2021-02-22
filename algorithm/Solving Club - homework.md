# homework

##  view

```python

import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    n = int(input())
    heights = list(map(int, input().split()))
    four = []
    ans = 0
    i = 2
    while i < n-2:
        if heights[i] <= heights[i-1] or heights[i] <= heights[i-2] or heights[i] <= heights[i+1]:
            i += 1
        elif heights[i] <= heights[i+2]:
            i += 2
        else:
            mx = max(heights[i-2], heights[i-1], heights[i+1], heights[i+2])
            ans += heights[i] - mx
            i+=3
    print(ans)


```



## flatten

```python

```



## Sum

```python
import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    mx = sum(arr[0])

    for i in range(100):
        if mx <= sum(arr[i]):
            mx = sum(arr[i])

    v_arr = list(zip(*arr))
    for i in range(100):
        if mx <= sum(v_arr[i]):
            mx = sum(v_arr[i])


    tot1 = 0
    tot2 = 0
    for i in range(100):
        tot1 += arr[i][i]
        tot2 += arr[i][99-i]

    print(max(mx, tot1, tot2))


```



## ladder1

```python
import sys
sys.stdin = open("input.txt")

T = 1

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        if arr[99][j] == 2:
            x = 99
            y = j

    direction = 0
    while x > 0:
        # 오른쪽 방향 탐색
        if (direction == 0 or direction == 1) and y < 99 and arr[x][y+1] == 1:
            y += 1
            direction = 1
        # 왼쪽 방향 탐색
        elif (direction == 0 or direction == -1) and y > 0 and arr[x][y -1] == 1:
            y-=1
            direction = -1
        # 양옆에 다 0이면 위로 올라가기
        else:
            x -= 1
            direction = 0

    print(y)

```



## GNS - 다시보기

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(1, T+1):
    tc, n = input().split()
    alien = list(input().split())
    # 외계문자를 숫자로 바꿔주는 dict
    num_dict = {"ZRO": 0,
                "ONE": 1,
                "TWO": 2,
                "THR": 3,
                "FOR": 4,
                "FIV": 5,
                "SIX": 6,
                "SVN": 7,
                "EGT": 8,
                "NIN": 9}
    # 숫자를 외계문자로 바꿔주는 dict
    alien_dict = {v: i for i, v in num_dict.items()}

    # 외계문자를 하나하나 숫자로 바꿔준다.
    alien2earth = [num_dict.get(i) for i in alien]
    print(alien2earth)
    # 정렬
    alien2earth.sort()

    # 정렬된 숫자를 하나하나 외계문자로 바꿔준다.
    result = [alien_dict.get(i) for i in alien2earth]

    # 한칸뛰고 join
    print("{} {}".format(tc, ' '.join(result)))

```



## 회문1

```python
import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    search_length = int(input())

    arr = [input() for _ in range(8)]
    v_arr = list(zip(*arr))
    
    '''
    v_arr = []
    for col in range(8):
        res = ''
        for row in range(8):
            res += arr[row][col]
        v_arr.append(res)
	'''

    cnt = 0
    for i in range(8):
        for j in range(8-search_length+1):
            if arr[i][j:j+search_length] == arr[i][j:j+search_length][::-1]:
                cnt += 1
            if v_arr[i][j:j+search_length] == v_arr[i][j:j+search_length][::-1]:
                cnt += 1
    print("#{} {}".format(tc,cnt))
```



## 회문2

```python
import sys
sys.stdin = open("input.txt")

T = 10

def pali(arr, v_arr):
    cnt = 0
    for search_length in range(100,0,-1):
        for i in range(100):
            for j in range(100-search_length+1):
                if arr[i][j:j+search_length] == arr[i][j:j+search_length][::-1]:
                    cnt += 1
                    return search_length, True
                if v_arr[i][j:j+search_length] == v_arr[i][j:j+search_length][::-1]:
                    cnt += 1
                    return search_length, True
    return 1,False

for tc in range(1, T+1):
    n = int(input())

    arr = [input() for _ in range(100)]
    v_arr = list(zip(*arr))

    aa = pali(arr, v_arr)

    print("#{} {}".format(tc,aa[0]))
```

