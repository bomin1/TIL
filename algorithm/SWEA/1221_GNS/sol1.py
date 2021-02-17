import sys
sys.stdin = open("input.txt")

T = int(input())
naming = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    test,length = input().split()
    arr = input().split()

    res = []

    for i in range(10):
        for ele in arr:
            if naming[i] == ele:
                res.append(ele)

    print(test)
    print( *res)

