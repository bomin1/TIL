import sys

sys.stdin = open("input.txt")


length = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = length//2
print(arr[m])


