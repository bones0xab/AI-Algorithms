Graph = {
    'G' : ['A','C'],
    'A' : ['G','B','D','H'],
    'B' : ['A','F'],
    'D' : ['A','G','E'],
    'H' : ['A','B','K'],
    'C' : ['G','D'],
    'F' : ['B'],
    'E' : ['D','A','C','K'],
    'K' : ['E','B']
}

def Iterative_DFS(graph, start, end):
    visited = []
    stack = []
    disctance = []
    stack.append(start)
    disctance.append((start, 0))

    while stack :
        node = stack.pop()
        if node == end :
            break
        if node not in visited :
            visited.append(node)
            unvisited = [n for n in reversed(graph[node]) if (n not in visited) & (n not in stack)]
            stack = stack + unvisited
        if node != start:
            for n in disctance:
                if n[0] == graph[node][0]:
                    disctance.append((node,n[1] + 1))
    return disctance, visited



