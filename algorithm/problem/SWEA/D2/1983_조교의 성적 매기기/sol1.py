import sys
sys.stdin = open("input.txt")

scores = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
T = int(input())

for tc in range(1, T+1):
    n,k = list(map(int, input().split()))
    ans = []

    for i in range(n):
        mid, fin, hw = list(map(int,input().split()))
        res = mid*0.35 + fin*0.45 + hw*0.2
        ans.append(round(res,1))

    # print(ans)
    kk = ans[2]
    col = 0

    sorted_list = sorted(ans, reverse=True)
    col = sorted_list.index(kk)
    # print(col)
    print("#{} {}".format(tc, scores[(col//(n//10))-1]))

