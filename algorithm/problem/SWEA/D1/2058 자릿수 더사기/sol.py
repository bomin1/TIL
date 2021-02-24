import sys

sys.stdin = open("input.txt")


a = input()
res = 0
for i in range(len(a)):
    res += int(a[i])
print(res)

