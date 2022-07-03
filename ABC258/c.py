
def main():
    from builtins import int,input,map,chr,print
    from collections import deque
    import copy

    N , Q = map( int, input().split() )
    S = input()
    outQue = deque(list(S))

    def query1(x:int):
        for i in range(x):
            outQue.rotate()


    def query2(x:int) ->None:
        print(outQue[x-1])

        return None


    for i in range( Q ):
        query = list(map(int,input().split() ) )
        if query[0] == 1:
            query1(query[1])
        else:
            query2(query[1])



    return 0


if __name__ == '__main__':
    main()