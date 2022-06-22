def main():
    from builtins import input,int,map,print,list

    N = int( input() )

    def printBrackets(current:str , leftBracket,rightBracket) -> None:

        if rightBracket == leftBracket == 0:
            print(current)
            return

        if leftBracket > 0 :
            leftBracket_next = leftBracket -1
            rightBracket_next = rightBracket + 1
            printBrackets(current+"(",leftBracket_next,rightBracket_next)

        if rightBracket > 0 :
            rightBracket_next = rightBracket -1
            printBrackets(current+")", leftBracket , rightBracket_next)

    if N%2 == 1: return 0
    printBrackets("",int(N/2),0)

    return 0


if __name__ == '__main__':
    main()
