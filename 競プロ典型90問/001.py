def main():
    from builtins import input,int,map,print

    N,L = map(int,input().split())
    K = int(input())
    A = list(map(int,input().split()))

    def canCut(minLength):
        cut_start = 0
        cut_count = 0
        for i in A:
            if i - cut_start >= minLength:
                cut_start = i
                cut_count += 1

            if cut_count == K:
                if L - cut_start >= minLength:
                    return True
                else:
                    break
        return False

    left = -1
    right = L+1

    while( right - left  > 1):
        mid = int( (left + right)/2 )
        if canCut(mid):
            left = mid
        else :
            right = mid

    print(left)







    return 0


if __name__ == '__main__':
    main()
