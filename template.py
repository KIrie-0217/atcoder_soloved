#https://qiita.com/c-yan/items/dbf2838cdd89864ef5ac
from numba import jit



def main():
    from builtins import input,int,map,print
    from sys import stdin
    readline = stdin.readline

    return 0


if __name__ == '__main__':
    main()


def inputs():
    x = int(input())  # int
    s = input() # string

    a,b,c = map(int,input().split()) #int 複数
    xyz = list(map(int, input().split())) # list of integers

    # 複数行
    for _ in range(n):
        x,y,z = map(int,stdin.readline().split()) # integers

    for _ in range(n):
        s = stdin.readline()[:-1]  # string

def outpts():
    #1つ出力
    print(x)

    #複数出力（空白）
    print(*xs)

    #改行区切りで複数出力
    print(*xs,sep="\n")

def list():
    #一次元
    #[0 for _ in range(n)]より早い
    xs = [0]*n

    #二次元
    t = [[0]*m for _ in rannge(n)]