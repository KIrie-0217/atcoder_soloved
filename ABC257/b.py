
def main():
    from builtins import int,input,map,chr,print
    import numpy as np


    N ,K ,Q = map(int, input().split() )
    A = list( map(int, input().split() ) )
    L  = list( map(int, input().split() ) )

    def piece_index( piece_num ):
        count = 0
        for i in range( N ):


            if trout_map[i] == 1:
                count += 1

            if count == piece_num:
                return i

        return 0

    trout_map = [0]* N

    for i in A:
        trout_map[i-1] = int(1)


    for i in range(Q):
        control_piece_num = L[i]
        control_piece  = piece_index( control_piece_num )

        if control_piece == N -1 :
            continue
        elif trout_map[ control_piece + 1 ] == 1:
            continue
        else:

            trout_map[control_piece +1] = int(1)
            trout_map[control_piece] = 0

    print( *[ i+1 for i , x in enumerate(trout_map) if x == 1])


    return 0


if __name__ == '__main__':
    main()