
def main():
    from builtins import input,int,map,print

    N ,K = map(int, input().split() )
    S = input()

    stringTmp = S
    result = ""

    while True:
        for i in range(26):
            string = chr(97 + i)
            stringIndex = stringTmp.find(string)

            if stringIndex == -1:
                continue
            if stringIndex <= len(stringTmp) - K + len(result):
                break

        result += string
        stringTmp = stringTmp[stringIndex+1:]

        if K == len(result):
            print(result)
            break

    return 0


if __name__ == '__main__':
    main()