# String

## 가장 빠른 문자열

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    n,m = input().split()

    cnt = 0
    res = 0
    i = 0
    while i < len(n):
        if n[i:i+len(m)] == m:
            cnt += 1
            i += len(m)
        else:
            i += 1

    res = len(n)-(len(m)*cnt) + 1*cnt
    print(res)


```



## 쇠막대기 자르기

```python


T = int(input())

for tc in range(1,T+1):
    iron_bar = input()
    s = []
    cnt = 0


    for i in range(len(iron_bar)):
        if iron_bar[i] == "(":
            s.append(iron_bar[i])
        else:
            s.pop()
            if iron_bar[i-1] == "(":
                cnt += len(s)
            else:
                cnt += 1
    print("#{} {}".format(tc, cnt))


```



## 의석이의 세로로 말해요

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    word = [0] * 5
    max_len = 0

    for i in range(5):
        word[i] = list(input())

        if max_len < len(word[i]):
            max_len = len(word[i])
    res = ''
    for j in range(max_len):
        for i in range(len(word)):
            if len(word[i]) > j:
                res += word[i][j]

    
    print("#{} {}".format(tc, res ))
```

