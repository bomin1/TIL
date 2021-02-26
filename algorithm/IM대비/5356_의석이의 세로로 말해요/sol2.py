import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    word = [input() for _ in range(5)]
    print(word)
    mx_len = 0
    for i in range(5):
        if mx_len < len(word[i]):
            mx_len = len(word[i])
    print(mx_len)

    res = ''
    for j in range(mx_len):
        for i in range(5):
            if len(word[i]) > j:
                res += word[i][j]
    print(res)