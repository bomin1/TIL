import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    test = int(input())

    password = list(map(int, input().split()))
    minus = [-1,-2,-3,-4,-5]
    idx = 0
    while True:
        check = password.pop(0)
        check += minus[idx]
        if check <= 0:
            check = 0
            password.append(check)
            break
        password.append(check)

        if idx != 4:
            idx += 1
        else:
            idx = 0

    print("#{} ".format(tc, ), end='')
    print(*password)

