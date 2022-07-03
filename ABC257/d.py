
def main():
    from builtins import int,input,map,print,list,sum,format
    import random
    import numpy as np



    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        _x , _y ,_P = map(int, input().split() )
        x.append(_x)
        y.append(_y)
        P.append(_P)

    x = np.array(x)
    y = np.array(y)
    P = np.array(P)

    need_S = []
    path = [False]*N
    for i in range(N):
        x_tmp = x - x[i]
        y_tmp = y - y[i]
        s_tmp = ( np.absolute( x_tmp) +  np.absolute( y_tmp ) )/P[i]
        need_S.append(s_tmp)
    need_S = np.array(need_S)

    def dfs(i,s,path):
        cost_next = need_S[i]
        path[i] = True
        for j in range(N):
            if i == j : continue
            elif cost_next[j] > s:
                continue
            else:
                dfs(j,s)

        if all( path ):

        return 0

    for i in range(N):
        continue
if __name__ == '__main__':
    main()