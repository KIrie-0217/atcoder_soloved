
def main():
    from builtins import map,int,input,print
    a,b = map(int,input().split()) #int 複数

    if( (a*b)%2 == 0 ):
        print("Even")
    else:
        print("Odd")
    return 0




if __name__ == '__main__':
    main()