# Course - Programming Intermediate - String



## 문자열 비교

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = input() # 찾을거
    str2 = input() # 찾음 당하는거

    res = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            res = 1
            break
        else:
            res = 0

    print("#{} {}".format(tc, res))
    
'''
    str1 = input() # 찾을거
    str2 = input() # 찾음 당하는거

    if str1 in str2:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))
'''
```





## 회문

```PYTHON
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(input())
    res = ''

    v_arr = []
    for col in range(n):
        str1 = ''
        for row in range(n):
            str1 += arr[row][col]
        v_arr.append(str1)

    for row in range(n):
        for col in range(n-m+1):
            if arr[row][col:col+m] == arr[row][col:col+m][::-1]:
                res = arr[row][col:col+m]
            if v_arr[row][col:col+m] == v_arr[row][col:col+m][::-1]:
                res = v_arr[row][col:col+m]
    print(res)
```



## 글자수

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = input() # 찾을거
    str2 = input() # 찾음 당하는거

    str1_dict = {}
    res = {}

    for i in str1:
        if i not in str1_dict:
            str1_dict[i] = 1
        else:
            str1_dict[i] += 1
    for idx in str1_dict.keys():
        res[idx] = 0


    for idx in str1_dict.keys():
        for ele in str2:
            if ele == idx:
                res[idx] += 1
    print(res)

    print("#{} 제일 많은 알파벳 : {} 그 개수는 {}".format(tc, max(res),res[max(res)]))

```

