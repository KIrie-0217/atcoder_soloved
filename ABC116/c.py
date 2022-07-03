
def main():
    import numpy as np
    from builtins import int,input,len
    N = int( input() )

    h = np.array( list( map( int, input().split() ) ) )

    def watering(flower_height:np.ndarray) -> int:
        count = 0
        if flower_height.size == 0: return 0
        else:
            for i in range( 100*100):
                cant_watering_index = np.where( flower_height == 0)[0]

                if cant_watering_index.size > 0:
                    for i in range(len(cant_watering_index)):
                        if i == 0:
                            count+= watering( flower_height[:cant_watering_index[i]])
                        else:
                            count+= watering( flower_height[cant_watering_index[i-1]+1:cant_watering_index[i]])

                        if i == len(cant_watering_index) -1:
                            count+= watering( flower_height[cant_watering_index[i]+1:])

                    break
                else:
                    flower_height = flower_height -1
                    count += 1


            return count

    print( watering(h))




    return 0


if __name__ == '__main__':
    main()