# Write Up of BFS
--- 

**Explication of the Algorithm** First of all BFS is an algorithm of non 
informational process, where he test the noeuds each one from the top to bottom ( length path ).

Let's explain more detaily :

-> Imagine you have a graph start with A and the user choose as destination I. 
(See the graph in bottom)

![image](https://github.com/user-attachments/assets/3de6870f-6da5-4ede-bb67-b203af948daa)


The BFS start from the top A and use a queue for hundle the nodes in process,
If a node is tested and their children are in the queue, we can use the methode of colors or we made it in the Close and tested nodes and vice versa...

Also i want to explain that when we made for example A in the queue and next we replace it into the closed nodes and insert their children (we mading the attention to the ordre of the alphabets !!!) and so one ...

This is the code : 

```python

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

```


***

#Write Up of DFS
--- 

**Explication of the algo**

This DFS is also a non informational algorithm, where he search fot the goal or destination,
deeply, not like the BFS.

Let me give detailed explication for better understanding.

DFS use the LIFO concept, where he insert the start first then he take it to the Visited nodes, 
also he take their children element by element (mading the attention to the order of alphabet).

as well, we get off the node in top, and get into the visited part and vice versa untill we reach the destination.

This is the Graph example of the DFS algorithm.



```python 

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



```

In this code i faced a problem in the part of stack, see the part where i add the condition of `n not in visited` cause i don't have any check of repeated nodes in the stack.
