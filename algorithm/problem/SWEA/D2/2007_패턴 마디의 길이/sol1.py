import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    string = input()
    s = ''
    for i in range(len(string)):
        s += string[i]
        if s == string[i+1:i+1+len(s)]:
            print("#{} {}".format(tc, len(s)))
            break

