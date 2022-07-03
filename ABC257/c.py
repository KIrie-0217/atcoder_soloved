
def main():
    from builtins import int,input,map,print,list,sum,format
    import random


    N = int(input())
    S = input()
    W  = list( map(int, input().split() ) )
    S_list = [ int(i) for i in list(S)]

    def score_checker( truth ):
        score = truth
        bit_inv = int( "1"*N , 2 )
        score = score^bit_inv^bit_inv
        return sum( [ int(i) for i in list( format(score,"b").zfill(N) )  ] )


    set = []
    for i in range(N):
        set.append([ W[i],S_list[i] ])
    set.sort()

    ans = int(S,2)
    ans_max = score_checker( ans )
    ans = ans_max

    boundary = [0]*N
    for i in range(N-1):
        if set[i][0]  != set[i+1][0]:
            boundary[i] = 1
    boundary[-1] = 1



    for i in range(N):

        if set[i][1] == 0 :
            ans += 1
        else:
            ans -= 1

        if ans_max < ans and boundary[i] == 1:
            ans_max = ans


    print(ans_max)



if __name__ == '__main__':
    main()