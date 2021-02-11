# 4828_min max

* **문제조건**

  N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를  출력하시오.

* **Input**

  * 첫 줄에 테스트 케이스의 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
  * 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
  * 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

  ```
  3
  5
  477162 658880 751280 927930 297191
  5
  565469 851600 460874 148692 111090
  10
  784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
  ```

* **Output**

  * 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

  ```
  #1 630739
  #2 740510
  #3 838110
  ```

---

* **Idea**

1. 가장 큰 값, 작은 값을 주어진 양수들 중 제일 앞의 것으로 지정한 다음에 하나하나 살펴보기
2.  처음부터 정렬을 이용해서 모두 정렬한 다음에 바로 인덱스 값 접근 - 버블소트 이용해보기
3. 내장함수 이용 - max, min등등?

---

* **Code**

  1.  idea - 1

     ```python
     import sys
     sys.stdin = open("input.txt")
     
     T = int(input())
     
     for tc in range(1, T+1):
         # 각 케이스의 양수의 갯수
         length = int(input())
     
         # 비교해야하는 number리스트
         numbers = list(map(int, input().split()))
     
         max_val = numbers[0]
         for number in numbers:
             if max_val < number:
                 max_val = number
     
         min_val = numbers[0]
         for number in numbers:
             if min_val > number:
                 min_val = number
     
     
         print("#{} {}".format(tc, max_val-min_val))
     ```

  2. idea - 2

     ```PYTHON
     import sys
     sys.stdin = open("input.txt")
     
     T = int(input())
     
     def bubble_sort(arr):
         for i in range(len(arr) - 1, 0, -1):
             for j in range(i):
                 if arr[j] > arr[j + 1]:
                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
     
     
     for tc in range(1, T+1):
         # 각 케이스의 양수의 갯수
         length = int(input())
         numbers = list(map(int, input().split()))
     
         bubble_sort(numbers)
         res = numbers[length-1] - numbers[0]
     
         print("#{} {}".format(tc, res))
         
     ```
     
     ```python
        # 앞에서부터
        def bubble_sort(arr):
            for i in range(len(arr) - 1):
                for j in range(len(arr) - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
     ```
  3. idea - 3
  
     ```python
     import sys
     sys.stdin = open("input.txt")
     
     T = int(input())
     
     for tc in range(1, T+1):
         length = int(input())
         numbers = list(map(int, input().split()))
         
         max_val = max(numbers)
         min_val = min(numbers)
     
         print("#{} {}".format(tc, max_val-min_val))
     ```

---

* **review**
  * 1번 같은 경우는 max_val과 min_val의 초기값을 잡을 때 처음에는 그냥 0 0이런 식으로 잡고 했었는데 그럼 다른 테스트 케이스를 생각해 보았을 때 지금 이 문제 같은 경우는 주어지는 수가 양수라고 나와있지만 만약 음수라면 min_val을 찾을 때 음수값에 접근하지 못하게 된다. 그래서 그냥 초기값을 첫번째 값으로 접근해서 사용하고 있다.
  * 정렬하는 방법이 코딩처음 배울 때 버블소트를 많이 쓰긴 했는데 버블 소트 말고 다른것도 있었던거같은데 한번 찾아봐야겠당.. 