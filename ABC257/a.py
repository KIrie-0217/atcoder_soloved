
def main():
    from builtins import int,input,map,chr,print

    N ,X = map(int, input().split() )

    str_num = 0

    for i in range( N*26 ):

        if i == X-1:
            print( chr( 97 + str_num).upper() )

        if (i + 1)%N  == 0: str_num += 1


    return 0


if __name__ == '__main__':
    main()