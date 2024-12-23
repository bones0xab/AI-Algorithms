# Exericices 
---

Exercice 1 A preliminary question about DFS and topological sorting for a hydroelectric power plant project
Exercise 2 about connecting 9 machines (minimum spanning tree problem)
Exercise 3 about installing a communication network
Exercise 4 about PERT network analysis for a roundabout construction project
Exercise 5 about path finding algorithms
Exercise 6 about finding the most reliable path in a telecommunication network
Exercise 7 about analyzing and modifying a shortest path algorithm


---

# Solutions
---

**1/ PRELIMINARY QUESTION:**


stateDiagram-v2
    direction LR
    %% Original Graph with DFS numbering
    state "Original Graph with DFS" as G1 {
        α --> A
        α --> B
        α --> C
        α --> D
        A --> E
        B --> E
        C --> E
        C --> F
        D --> F
        E --> G
        F --> G
        G --> H
        H --> I
    }

    %% Topologically Sorted Graph
    state "Topologically Sorted" as G2 {
        direction LR
        α1: α(1)
        A1: A(2)
        B1: B(3)
        C1: C(4)
        D1: D(5)
        E1: E(6)
        F1: F(7)
        G1: G(8)
        H1: H(9)
        I1: I(10)
        
        α1 --> A1
        α1 --> B1
        α1 --> C1
        α1 --> D1
        A1 --> E1
        B1 --> E1
        C1 --> E1
        C1 --> F1
        D1 --> F1
        E1 --> G1
        F1 --> G1
        G1 --> H1
        H1 --> I1
    }
---


a) DFS Traversal:
The DFS algorithm will visit nodes in this order:

Start at α (root)
Visit A → E → G → H → I
Backtrack and visit B
Backtrack and visit C → F
Finally visit D

b) Topological Sort:
The topological ordering of the tasks would be:
α → A,B,C,D → E → F → G → H → I
This ordering ensures that all dependencies are met before starting any task.

EXERCISE 2 (Minimum Spanning Tree):


1/ This is a Minimum Spanning Tree (MST) problem. The most appropriate algorithm would be either Kruskal's or Prim's algorithm. Since we're asked to start with vertex A, Prim's algorithm is the most suitable choice.
Let's apply Prim's algorithm starting from vertex A:


graph TD
    A((A))--4---B((B))
    A--7---F((F))
    B--3---C((C))
    B--2---D((D))
    F--5---H((H))
    D--4---E((E))
    C--3---G((G))
    E--6---I((I))

    style A fill:#d4f1f4
    style B fill:#d4f1f4
    style C fill:#d4f1f4
    style D fill:#d4f1f4
    style E fill:#d4f1f4
    style F fill:#d4f1f4
    style G fill:#d4f1f4
    style H fill:#d4f1f4
    style I fill:#d4f1f4

---

Steps of Prim's algorithm:

Start with A
Add edge A-B (weight 4)
Add edge B-D (weight 2)
Add edge B-C (weight 3)
Add edge D-E (weight 4)
Add edge A-F (weight 7)
Add edge C-G (weight 3)
Add edge F-H (weight 5)
Add edge E-I (weight 6)


The total cost of the minimum spanning tree is: 4 + 2 + 3 + 4 + 7 + 3 + 5 + 6 = 34 units

This solution ensures that all 9 machines are connected with the minimum possible total cost while maintaining connectivity between all nodes.


---

# Exercise 3 : Communication Network Installation.
---


This is also a Minimum Spanning Tree (MST) problem since we want to connect all sites with minimum total cost, ensuring all sites are connected without cycles.
Let's solve using Prim's algorithm:


graph TD
    A((A))--5---B((B))
    B--7---E((E))
    A--7---F((F))
    F--10---H((H))
    B--17---C((C))
    A--9---D((D))
    C--20---G((G))

    style A fill:#d4f1f4
    style B fill:#d4f1f4
    style C fill:#d4f1f4
    style D fill:#d4f1f4
    style E fill:#d4f1f4
    style F fill:#d4f1f4
    style G fill:#d4f1f4
    style H fill:#d4f1f4


Steps:

Start with A
Add A-B (cost: 5)
Add A-F (cost: 7)
Add B-E (cost: 7)
Add A-D (cost: 9)
Add F-H (cost: 10)
Add B-C (cost: 17)
Add C-G (cost: 20)

Total cost = 5 + 7 + 7 + 9 + 10 + 17 + 20 = 75 units
EXERCISE 4 - PERT Network Analysis:
a) Let's create the PERT network and calculate all required values:
graph LR
    Start((Start))-->A[A:30]
    Start-->B[B:15]
    A-->C[C:40]
    A-->D[D:35]
    A-->E[E:25]
    B-->D
    A-->J[J:11]
    C-->F[F:15]
    D-->F
    B-->F
    C-->G[G:10]
    D-->G
    F-->G
    E-->H[H:100]
    G-->H
    G-->I[I:55]
    H-->End((End))
    I-->End
Early dates (ES/EF):

A: 0/30
B: 0/15
C: 30/70
D: 30/65
E: 30/55
F: 70/85
G: 85/95
H: 95/195
I: 95/150
J: 30/41

Late dates (LS/LF):

A: 0/30
B: 55/70
C: 30/70
D: 30/65
E: 95/120
F: 70/85
G: 85/95
H: 95/195
I: 140/195
J: 184/195

Critical path: Start → A → C → F → G → H → End
Project duration: 195 days
Total Float (TF) and Free Float (FF):

A: TF=0, FF=0 (critical)
B: TF=55, FF=55
C: TF=0, FF=0 (critical)
D: TF=5, FF=5
E: TF=65, FF=65
F: TF=0, FF=0 (critical)
G: TF=0, FF=0 (critical)
H: TF=0, FF=0 (critical)
I: TF=45, FF=45
J: TF=154, FF=154

b) For the sub-project H (from Figure 3):
graph LR
    Start((Start))-->K[K:10]
    Start-->L[L:20]
    K-->M[M:5]
    L-->P[P:4]
    M-->W[W:3]
    P-->Q[Q:12]
    P-->U[U:5]
    Q-->O[O:10]
    U-->V[V:15]
    O-->N[N:40]
    V-->N
    N-->End((End))
Early dates for sub-project H:

K: 0/10
L: 0/20
M: 10/15
P: 20/24
W: 15/18
Q: 24/36
U: 24/29
O: 36/46
V: 29/44
N: 46/86

Critical path in sub-project H: Start → L → P → Q → O → N → End
Sub-project duration: 86 days


---


# EXERCISE 5 - Path Finding Algorithm:

Let's apply the algorithm to the graph in Fig. 4:


# Initial Matrix V(0)
V0 = [
    [0, 6, ∞, 9],
    [∞, 0, 8, ∞],
    [∞, ∞, 0, 7],
    [∞, ∞, 4, 0]
]

# After k=1
V1 = [
    [0, 6, ∞, 9],
    [∞, 0, 8, ∞],
    [∞, ∞, 0, 7],
    [∞, ∞, 4, 0]
]

# After k=2
V2 = [
    [0, 6, 14, 9],
    [∞, 0, 8, 15],
    [∞, ∞, 0, 7],
    [∞, ∞, 4, 0]
]

# After k=3
V3 = [
    [0, 6, 14, 9],
    [∞, 0, 8, 15],
    [∞, ∞, 0, 7],
    [∞, ∞, 4, 0]
]

# Final Matrix V(4)
V4 = [
    [0, 6, 13, 9],
    [∞, 0, 8, 15],
    [∞, ∞, 0, 7],
    [∞, ∞, 4, 0]
]

Complexity: O(n³) where n is the number of vertices
Circuit absorbant detection: If after n iterations, we find a negative value on the diagonal of the matrix, there exists an absorbing circuit.
For maximization:


Replace min with max in the algorithm
Replace +∞ with -∞ in initialization
Keep the rest of the algorithm the same


To memorize intermediate vertices:


# Add a predecessor matrix P
P = [[None for _ in range(n)] for _ in range(n)]

# In the main loop, add:
if (v[i][k] + v[k][j] < v[i][j]):
    v[i][j] = v[i][k] + v[k][j]
    P[i][j] = k  # Store intermediate vertex

# Function to reconstruct path
def get_path(i, j, P):
    if P[i][j] is None:
        return [i, j]
    else:
        k = P[i][j]
        path1 = get_path(i, k, P)
        path2 = get_path(k, j, P)
        return path1[:-1] + path2
EXERCISE 6 - Most Reliable Path:
To find the most reliable path between 'a' and 'i', we need to modify Dijkstra's algorithm:

Instead of adding probabilities, we multiply them
Instead of finding minimum distance, we find maximum probability
Take -log of probabilities to convert multiplication to addition
graph LR
    a((a))--0.9-->b((b))
    b--0.85-->d((d))
    d--0.95-->i((i))
    
    style a fill:#d4f1f4
    style b fill:#d4f1f4
    style d fill:#d4f1f4
    style i fill:#d4f1f4
Most reliable path: a → b → d → i
Total reliability = 0.9 × 0.85 × 0.95 ≈ 0.727 or 72.7%
# EXERCISE 7 - Algorithm Machin1:

Let's apply the algorithm:

# Initial state:
λ[0] = 0; P[0] = 0
λ[1...n-1] = ∞; P[1...n-1] = -1

# First iteration:
λ = [0, 6, ∞, 9]
P = [0, 0, -1, 0]

# Second iteration:
λ = [0, 6, 14, 9]
P = [0, 0, 1, 0]

# Third iteration:
λ = [0, 6, 13, 9]
P = [0, 0, 3, 0]

# Final state:
λ = [0, 6, 13, 9]
P = [0, 0, 3, 0]

Shortest Path Tree:


Root: vertex 0
Path to vertex 1: 0 → 1 (cost 6)
Path to vertex 2: 0 → 3 → 2 (cost 13)
Path to vertex 3: 0 → 3 (cost 9)


To detect absorbing circuits, add a counter for the number of modifications. If this counter exceeds n-1 (where n is the number of vertices), there exists an absorbing circuit.

# Add counter
iterations = 0
max_iterations = n - 1

while (modification == true and iterations < max_iterations):
    modification = false
    # ... rest of the algorithm ...
    iterations += 1

if iterations == max_iterations and modification:
    print("Absorbing circuit detected!")
