
def main():

    N = int( input() )
    classRate =  sorted(list( map( int, input().split()) ) )
    Q = int( input())

    def binarySearch( memRate : int ):
        left = -1
        right = N+1

        while( right - left  > 1):
            mid = int( (left + right)/2 ) 
            if classRate[mid] < memRate:
                left = mid
            else :
                right = mid
        return right

    for _ in range( Q ):
        memberRate = int(input())

        nearClass = binarySearch( memberRate )

        if nearClass == 0:
            print( classRate[nearClass] - memberRate )
        elif classRate[nearClass] - memberRate < memberRate - classRate[nearClass -1]:
            print( classRate[nearClass] - memberRate )
        else:
            print( memberRate - classRate[ nearClass-1 ])


    return 0


if __name__ == '__main__':
    main()