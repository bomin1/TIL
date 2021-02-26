import sys
sys.stdin = open("input.txt")

T = int(input())
def check(cards):
    cnt_s = [0] * 13
    cnt_D = [0] * 13
    cnt_H = [0] * 13
    cnt_c = [0]*13
    for i in range(0,len(cards),3):
        if cards[i] == 'S':
            num = int(cards[i+1:i+3])
            cnt_s[num-1] += 1
            if cnt_s[num-1] > 1:
                return 'ERROR'
        elif cards[i] == 'D':
            num = int(cards[i+1:i+3])
            cnt_D[num-1] += 1
            if cnt_D[num-1] > 1:
                return 'ERROR'
        elif cards[i] == 'H':
            num = int(cards[i+1:i+3])
            cnt_H[num-1] += 1
            if cnt_H[num-1] > 1:
                return 'ERROR'
        elif cards[i] == 'C':
            num = int(cards[i+1:i+3])
            cnt_c[num-1] += 1
            if cnt_c[num-1] > 1:
                return 'ERROR'
    return  cnt_s.count(0),cnt_D.count(0),cnt_H.count(0),cnt_c.count(0)

for tc in range(1, T+1):
    cards = input()
    res = check(cards)

    if res != 'ERROR':
        print("#{} ".format(tc), end='')
        print(*res)
    else:
        print("#{} ERROR".format(tc))
