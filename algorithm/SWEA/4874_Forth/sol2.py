import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    equation = list(input().split())
    s = []
    res = 0
    for ele in equation:
        if ele.isdigit():
            s.append(ele)
        else:
            if ele == '.':
                print("#{} {}".format(tc, s.pop()))
                break

            try:
                b=int(s.pop())
                a = int(s.pop())

                if ele == '+':
                    c = a + b
                elif ele == '-':
                    c = a - b
                elif ele == '*':
                    c = a * b
                elif ele == '/':
                    c = a // b
                s.append(c)
            except:
                res = -1

    if res == -1 or len(s) >=2:
        print("#{} error".format(tc))
