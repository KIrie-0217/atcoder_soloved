import numpy as np

def main():
    from builtins import input,int,print

    s = list(map(int, input().split())) # list of integers
    if sum(s[:3]) != sum(s[3:]):
        print("0")
        return 0
    else:
        count = 0
        h,w = s[:3],s[:3]
        for a1 in range(1,29):
            for a2 in range(1,29):
                for b1 in range(1,29):
                    for b2 in range(1,29):
                        c1 = h[0] - a1 -b1
                        c2 = h[1] - a2 -b2
                        a3 = w[0] - a1 -a2
                        b3 = w[1] - b1 -b2
                        c3 = w[2] - a3 -b3
                        if (    c1 > 0 and
                                c2 > 0 and
                                a3 > 0 and
                                b3 > 0 and
                                c3 > 0 and
                                c1+c2+c3 == h[2]): count += 1
        print( count )
        return count

if __name__ == '__main__':
    main()
