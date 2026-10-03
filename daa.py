def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    edges.sort(key=lambda x: x[2])
    total = 0

    for u, v, cost in edges:
        a, b = find(u), find(v)

        if a != b:
            parent[a] = b
            total += cost
            print(u, "-", v, ":", cost)

    print("Minimum Cost =", total)


n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (1, 2, 5),
    (1, 3, 15),
    (2, 3, 8)
]

kruskal(n, edges)