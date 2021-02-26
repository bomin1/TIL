import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    word = [0] * 5
    max_len = 0

    for i in range(5):
        word[i] = list(input())

        if max_len < len(word[i]):
            max_len = len(word[i])
    res = ''

    for j in range(max_len):
        for i in range(len(word)):
            if len(word[i]) > j:
                res += word[i][j]

    
    print("#{} {}".format(tc, res ))

