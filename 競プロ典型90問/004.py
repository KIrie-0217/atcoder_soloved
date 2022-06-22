import numpy as np

def main():
    from builtins import input,int,map,print

    H , W = map(int, input().split() )
    trout = np.array ( [ list(map(int,input().split() ) ) for i in range(H) ] )

    troutList= trout.tolist()
    crossSum = np.empty( ( H,W) ).tolist()
    columnSum = np.sum(trout , axis= 0).tolist()
    rowSum = np.sum(trout , axis=1 ).tolist()

    for i,j in np.ndindex( trout.shape):
        crossSum[i][j] = columnSum[j] + rowSum[i] - troutList[i][j]

    for i in range(H):
        print( *crossSum[i][:] )


    return 0


if __name__ == '__main__':
    main()
