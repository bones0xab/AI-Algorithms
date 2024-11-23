from collections import deque

#Simple BFS code for non orieted Graph
Graph = {
    'A' : ['B','F'],
    'B' : ['A','C','D','G'],
    'C': ['B','E'],
    'D' : ['B','I'],
    'E' : ['C','I'],
    'F' : ['A','G','H'],
    'G' : ['B','F','I'],
    'H' : ['F'],
    'I' : ['D','E','G']
}
def Iterative_bfs(graph, start, end):
    visited = []
    disctance =[]
    queue = deque()
    queue.append(start)
    disctance.append((start,0))

    while queue :
        node = queue.popleft()
        #This is if we arrived to the end
        if node == end:
            break

        #The part where we made the process of BFS
        else :
            if node not in visited :
                visited.append(node)
                unvisited = [n for n in graph[node] if n not in visited]
                queue = queue + deque(unvisited)
        #This is to calculate the distances
        if node != start:
            for n in disctance:
                if n[0] == graph[node][0]:
                    disctance.append((node,n[1] + 1))
    return set(disctance),visited

#a problem with the non oriented graph is he repeat some nodes and i will make to the list a set to see the good results
#BFS with Final State
print(Iterative_bfs(Graph,'A','P'))


