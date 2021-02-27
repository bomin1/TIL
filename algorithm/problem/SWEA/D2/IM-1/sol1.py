import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = []

    for i in range(n+1):
        arr.append(input())

    print(arr)

    
    print("#{} ".format(tc, ))

