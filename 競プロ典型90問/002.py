def main():
    from builtins import input,int,map,print,list

    N = int( input() )

    def isCorrectBrackets( i :int):
        count0 = 0
        count1 = 0
        binBrackets = format(i,"b").zfill(N)
        listBrackets = list( map(int,binBrackets) )
        for i in listBrackets:
            if i == 0: count0 += 1
            else: count1 += 1

            if count0 < count1: return False
        if count0 == count1: return True
        return False

    if N %2 != 0: return 0
    else:
        for i in range( 2**N ):

            if isCorrectBrackets(i):
                print( format(i,"b").zfill(N).replace("0","(").replace("1",")") )

    return 0


if __name__ == '__main__':
    main()
