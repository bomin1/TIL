# List

## Baby-gin Game

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    nums = input()
    cnt = [0]*12
    for num in nums:
        cnt[int(num)] += 1

    run = 0
    tri = 0
    i = 0
    while i < len(cnt)-2:
        if cnt[i] >= 3:
            tri += 1
            cnt[i] -=3
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt [i+2] >= 1:
            run += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            continue

    if run + tri == 2:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))

```



