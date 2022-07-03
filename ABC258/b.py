
def main():
    from builtins import int,input,map,chr,print

    N = int( input() )
    A = []
    as_max = []
    as_max_index = []
    for i in range(N):
        a_tmp = list( map( int , list(input()) ) )
        A.append( a_tmp )
        as_max.append( max(a_tmp) )
        as_max_index.append( [ i for i,v in enumerate(a_tmp) if v == max(a_tmp)] )

    start_index = [ i for i,v in enumerate(as_max) if v == max(as_max)]

    #print(start_index )
    #print(as_max_index) 

    num_best = 0
    for l in range( len(start_index) ):
        row = start_index[ l ]


        for j in range( len(as_max_index[row] ) ):
            column = as_max_index[row][j]

            num_temp = ""

            # →
            for i in range(N):
                
                if column+i >= N:
                    column_tmp = column+i - N
                else:
                    column_tmp = column + i
                num_temp += str( A[row][column_tmp] )
            #print(num_temp)

            if int(num_temp) > num_best:
                num_best = int(num_temp)
            num_temp = ""

            # ←
            for i in range(N):
                num_temp += str( A[row][column - i] )
            #print(num_temp)

            if int(num_temp) > num_best:
                num_best = int(num_temp)

            num_temp = ""


            #　↓
            for i in range(N):
                if row+i >= N:
                    row_tmp = row+i - N
                else:
                    row_tmp = row + i
                num_temp += str( A[row_tmp][column] )
            if int(num_temp) > num_best:
                num_best = int(num_temp)
            #print(num_temp)
            num_temp = ""

            # ↑
            for i in range(N):
                num_temp += str( A[row-i][column] )
            if int(num_temp) > num_best:
                num_best = int(num_temp)
            #print(num_temp)
            num_temp = ""

            for i in range(N):
                if column+i >= N:
                    column_tmp = column+i - N
                else:
                    column_tmp = column + i
                if row+i >= N:
                    row_tmp =  row+i - N
                else:
                    row_tmp = row + i
                num_temp += str( A[row_tmp][column_tmp] )
            #print(num_temp)
            if int(num_temp) > num_best:
                num_best = int(num_temp)

            num_temp = ""

            for i in range(N):

                if column+i >= N:
                    column_tmp = column+i - N
                else:
                    column_tmp = column + i
                num_temp += str( A[row -i][column_tmp] )
            #print(num_temp)
            if int(num_temp) > num_best:
                num_best = int(num_temp)

            num_temp = ""
            for i in range(N):

                if row+i >= N:
                    row_tmp = row+i - N
                else:
                    row_tmp = row + i
                num_temp += str( A[row_tmp][column - i] )
            #print(num_temp)   
            if int(num_temp) > num_best:
                num_best = int(num_temp)

            num_temp = ""
            for i in range(N):
                num_temp += str( A[row -i][column - i] )
            if int(num_temp) > num_best:
                num_best = int(num_temp)
            #print(num_temp)
            num_temp = ""

    print(num_best)
    return 0


if __name__ == '__main__':
    main()