
def main():
    from builtins import input,int,map,print,list

    def even(Ai):
        tmp_Ai = [        ]

        for num in Ai:
            if num%2 == 1:
                return 0
            else:
                temp_Ai.append(num/2)
        return temp_Ai


    N = int(input())
    Ai =  list(map(int, input().split())) # list of integers

    for r in range(200):
        Ai = even(Ai)
        if Ai == 0:
            print(r)
            break

    return 0


if __name__ == '__main__':
    main()