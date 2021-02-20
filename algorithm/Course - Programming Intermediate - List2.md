# Course - Programming Intermediate - List2



## 색칠하기

```python
import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    cnt = 0

    for i in range(n):
        x1,y1,x2,y2,color = map(int, input().split())
        for x in range(x2-x1+1):
            for y in range(y2-y1+1):
                arr[x1+x][y1+y] += color
    for i in range(len(arr)):
        for j in arr[i]:
            if j == 3:
                cnt += 1
    print("#{} {}".format(tc, cnt))

```





## 이진탐색

```PYTHON
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    P, Pa, Pb = map(int, input().split())
    l = 1
    r = P

    cnt_a = 0
    cnt_b = 0

    while True:
        c = int((l + r) / 2)
        cnt_a += 1
        if c == Pa:
            break
        elif Pa < c:
            r = c
        else:
            l = c

    l = 1
    r = P
    while True:
        c = int((l + r) / 2)
        cnt_b += 1
        if c == Pb:
            break
        elif Pb <= c:
            r = c
        else:
            l = c

    if cnt_a > cnt_b:
        print("#{} B".format(tc))
    elif cnt_a == cnt_b:
        print("#{} 0".format(tc))
    else:
        print("#{} A".format(tc))
```



## 특별한 정렬

```python
import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    new_arr=[]
    for i in range(n):
        if i % 2 == 0:
            new_arr.append(arr[(n-1)-(i//2)])
        else:
            new_arr.append(arr[i//2])

    print("#{} {}".format(tc, " ".join(map(str, new_arr[0:10]))))
```

