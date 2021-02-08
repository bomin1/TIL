# Babygin

> 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때. 
>
> 3장의 카드가 연속적인 번호를 갖는 경우를 run, 동일한 번호를 갖는 경우를 triplet이라고 한다.
>
> 이 6장의 카드가 run과 triplet으로만 이루어진 경우를 baby-gin이라고 (baby-gin 일 경우 **1,** 아닌 경우 **0** 을 출력한다.)



```txt
3
667767
054060
101123
```

---

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 받아 온 행들의 숫자를 정수로 형변환해서 list로 만들어준다.
    # [6,6,7,7,6,7] 이런식으로 numbers에 저장
    numbers = list(map(int, input()))

    # 숫자의 개수를 누적할 리스트를 만든다
    c = [0] * 12
    # c = [0,0,0,0,0,0,0,0,0,0,0,0]
    # id = 0,1,2,3,4,5,6,7,8,9,10,11
    
    # numbers = [6,6,7,7,6,7] 
    #c[6] + 1 = 1, c[6] + 1 = 2 ...
    for number in numbers:
        c[number] += 1;
    

    i = 0
    tri = 0
    run_ = 0
    # 0~9까지의 숫자니까 반복횟수는 10번
    while i < 10:
        # triplet 확인
        # 3번이 넘게 카운트가 된거면 무조건 3번 반복된거니까 triplet이고  
        if c[i] >= 3:
            tri += 1
            # triplet인것을 확인했으므로 3개 숫자를 없애준다고 생각.
            c[i] -= 3
  			# 다시 i = 0인 부분부터 봐야하니까 밑에 안보고 바로 위로 올라감 = continue
            continue
            
        # run 확인
        '''
        c[0] c[1] c[2]
        c[1] c[2] c[3]
           ...
        c[9] c[10] c[11] <- 여기까지 봐야하니까 애초에 c를 만들어줄 때 인덱스 11까지 (0 12개)를 잡아줘야함.
        '''
        if c[i] >= 1 and c[i+1] >=1 and c[i+2] >= 1:
            run_ += 1
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            continue
        i+=1

    if run_ + tri == 2:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))


```

---

1.  c = [0] * 12 

   숫자 개수 누적하는 리스트를 만들때 0의 개수를  numbers의 최댓값으로 해서 코드짜면 안되는지 확인해보기