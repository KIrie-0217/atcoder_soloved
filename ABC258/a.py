
def main():
    from builtins import int,input,map,chr,print

    K = int( input() )

    hour = 21 + K // 60
    hour = str ( int(hour ))
    min = K % 60
    min = str(min).zfill(2)

    print(hour+":"+min)
    return 0


if __name__ == '__main__':
    main()