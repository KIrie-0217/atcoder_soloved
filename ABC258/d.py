
def main():
    from builtins import int,input,map,chr,print

    N , X = map( int, input().split() )
    early = 0
    faster = float("inf")
    for i in range(N):
        A , B = map( int, input().split() )
        early += A + B
        if i < X:
            total = early + B*(X - i -1 )
            if total < faster: faster = total
    print(faster)


    return 0


if __name__ == '__main__':
    main()