import sys
sys.stdin = open("input.txt")

T = int(input())
def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)

    res = [0]*n
    for i in range(n):
        if i % 2 == 0:
            res[i] = arr[n-(i//2)-1]
        else:
            res[i] = arr[i//2]

    print("#{} {}".format(tc, " ".join(map(str,res[0:10]))))

