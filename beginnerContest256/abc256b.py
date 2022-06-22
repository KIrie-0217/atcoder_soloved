import numpy as np

def main():
    from builtins import input,int,print

    N = int(input())
    ai = list(map(int, input().split())) # list of integers

    mass = np.zeros(N)
    for i in range(N):
        mass[:i+1] += ai[i]

    mass = mass[mass >3]

    print(int(mass.shape[0]))

    return 0

if __name__ == '__main__':
    main()
