import sys


def shortestReach():
    print("Enter no of Test Cases: ", end='')
    testCases = int(input())

    if 1 > testCases > 10:
        print("Test cases can't be greater than 10 or smaller than 1")
    else:
        counter = 0
        while counter < testCases:
            print("Test Case# ", counter + 1)
            nodesEdges = input()
            nodesEdges = nodesEdges.split(' ')

            nodes = int(nodesEdges[0])
            edges = int(nodesEdges[1])

            if 3000 < nodes < 2:
                print("The graph must have nodes between 2 and 3000")
            else:
                if 1 > edges > nodes * (nodes - 1) / 2:
                    print("The graph must have edges between 1 and " + str(nodes * (nodes - 1) / 2))
                else:
                    graph = generateGraph(nodes)

                    while edges > 0:
                        data = input()
                        data = data.split(' ')

                        graph[int(data[0]) - 1][int(data[1]) - 1] = int(data[2])

                        edges -= 1

                    print("User's Graph")

                    printGraph(graph)

                    print("Enter the node for calculating shortest path: ", end='')
                    startingNode = int(input())

                    dijkstra(graph, nodes, startingNode)

                    print('\n')

                    counter += 1

    pass


def generateGraph(nodes):
    graph = []
    for a in range(0, nodes):
        col = []
        for b in range(0, nodes):
            col.append(-1)
        graph.append(col)

    return graph


def printGraph(graph):
    for a in graph:
        for b in a:
            print(b, end=' ')
        print()


def getMinDistance(dist, processed, nodes):
    minimum = sys.maxsize
    minIndex = -1

    for a in range(0, nodes):
        if not processed[a] and dist[a] <= minimum:
            minimum = dist[a]
            minIndex = a

    return minIndex


def dijkstra(graph, nodes, startingNode):
    dist = []
    processed = []

    for a in range(0, nodes):
        dist.append(sys.maxsize)
        processed.append(False)

    dist[startingNode - 1] = 0

    for a in range(0, nodes - 1):
        minIndex = getMinDistance(dist, processed, nodes)

        processed[a] = True

        for b in range(0, nodes):
            if not processed[b] and graph[minIndex][b] != -1 and dist[minIndex] != sys.maxsize and dist[minIndex] + \
                    graph[minIndex][b] < dist[b]:
                dist[b] = dist[minIndex] + graph[minIndex][b]

    print("Shortest path from node: ", startingNode)
    for a in range(0, nodes):
        if dist[a] == sys.maxsize:
            dist[a] = -1

        if (a + 1) != startingNode:
            print(startingNode, " -->", a + 1, ':', dist[a])


if __name__ == '__main__':
    shortestReach()
