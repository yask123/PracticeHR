from pythonds.basic import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)

    vertQueue = Queue()
    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):
        current_vertex = vertQueue.dequeue()

        for nbr in current_vertex:
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(current_vertex.getDistance() + 1)
                nbr.setPred(current_vertex)
                vertQueue.enqueue(nbr)
        current_vertex.setColor('black')
