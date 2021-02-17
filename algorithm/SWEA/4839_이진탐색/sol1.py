import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    cntA = 0
    cntB = 0
    l = 1
    r = P
    while 1:
        c = int((l+r)/2)
        cntA += 1
        if c == A:
            break
        elif c <= A:
            l = c
        else:
            r = c
    l = 1
    r = P
    while 1:
        c = int((l+r)/2)
        cntB += 1
        if c == B:
            break
        elif c <= B:
            l = c
        else:
            r = c

    if cntA == cntB:
        print("#%d %d" %(tc, 0))
    elif cntA > cntB:
        print("#%d %c" %(tc, 'B'))
    else:
        print("#%d %c" %(tc, 'A'))
