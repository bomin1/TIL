import sys
sys.stdin = open("input.txt")

T = int(input())
def pali(string):
    if string == string[::-1]:
        return 1
    else:
        return 0

for tc in range(1, T+1):
    string = list(input())
    res = pali(string)

    print("#{} {}".format(tc,res ))

