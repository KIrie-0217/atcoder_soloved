#　ヒストグラムで並べたとき、左右どちらか見た時の崖の高さの和がそのまま答えになる

def main():
    import numpy as np
    from builtins import int,input,len
    N = int( input() )

    h = list( map( int, input().split() ) )
    h.append(0)
    difference_height = np.array( [ h[i] - h[i+1] for i in range( N ) ] )

    print( difference_height[difference_height>0].sum() ) #高いほうだけ見る

    return 0


if __name__ == '__main__':
    main()