import numpy as np

# https://atcoder.jp/contests/abc256/tasks/abc256_d
#imos法による実装
# １行ごとに入退時間ととらえて、一人以上が存在している時間を記載する、と解釈するとわかりやすい

def main():
    from builtins import input,int,print,sorted,str

    N = int(input())

    S = [0]*2*10**5

    for i in range(N) :
        L,R = map(int,input().split())
        S[L] += 1
        S[R] -= 1

    pre = 0

    for i in range(2*10**5 +1):
        S[i] += S[i-1]
        if pre == 0 and S[i] != 0:
            pre = i
        if pre != 0 and S[i] == 0:
            print(pre,i)
            pre = 0


if __name__ == '__main__':
    main()
