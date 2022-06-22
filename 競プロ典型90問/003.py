
def main():
    from builtins import input,int,map,print

    N = int(input())
    graph = [ [] for i in range(N)]
    for i in range(N-1):
        a,b = map( int , input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)


    def dijkstra(startPoint):
        dist = [ -1 ] * N
        dist[startPoint] = 0
        queue = [startPoint]
        while queue:
            tempPoint = queue.pop()
            for nextPoint in graph[tempPoint]:
                if dist[nextPoint] == -1:
                    dist[nextPoint] = dist[tempPoint] + 1
                    queue.append(nextPoint)
        return dist

    dist0 = dijkstra(0)
    maxPoint = dist0.index( max(dist0) )

    maxLength = max( dijkstra(maxPoint) ) + 1

    print( maxLength )



    return 0


if __name__ == '__main__':
    main()
