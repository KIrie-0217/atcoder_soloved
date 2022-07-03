
def main():
    from builtins import list,map,int,input,abs,sum
    import heapq
    N,M = map( int, input().split() )
    X = list( map( int, input().split()) )
    X.sort()

    distance = [ abs( X[i+1] - X[i] ) *(-1) for i in range( M -1 )]
    heapq.heapify(distance)


    for i in range( min( M-1,N-1)):
        heapq.heappop(distance)

    print(sum(distance)*(-1))


    return 0


if __name__ == '__main__':
    main()