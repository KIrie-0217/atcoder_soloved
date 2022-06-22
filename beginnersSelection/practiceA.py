from numba import jit

@jit
def main():

    a = int(input())
    b,c = map(int,input().split())
    s = input()

    print(str(a+b+c)+" "+s)
    return 0



if __name__ == '__main__':
    main()
