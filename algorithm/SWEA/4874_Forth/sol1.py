import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    equation = list(input().split())
    s = []
    res = 0
    for i in range(len(equation)-1):
        check = equation[i]
        if check.isdigit():
            s.append(check)
        else:
            try:
                b = int(s.pop())
                a = int(s.pop())

                if check == '+':
                    c = a+b
                elif check == '-':
                    c = a-b
                elif check == '*':
                    c = a*b
                elif check == '/':
                    c = a//b
                s.append(c)
            except:
                res = -1

    if res == -1 or len(s) >= 2:
        print("#{} error".format(tc))
    else:
        print("#{} {}".format(tc, s.pop()))