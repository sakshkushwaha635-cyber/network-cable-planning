# 🌐 Network Cable Planning - Minimum Spanning Tree Optimizer

### DAA Hackathon Project | Team - Network Optimizers

---

## 📌 Problem Statement
A campus has N buildings. Each building can be connected with network cable with different costs. Find the minimum total length of cable required to connect all buildings such that every building can communicate with every other building (directly or indirectly).

This is a classic **Minimum Spanning Tree (MST)** problem.

---

## 🧠 Problem Understanding
- **Input:** Number of buildings (N), List of possible cable connections (u, v, cost)
- **Output:** Minimum total cost to connect all buildings + selected cables
- **Constraints:** 
    - N ≤ 10,000 buildings
    - E ≤ 100,000 possible cables
    - Cost ≤ 10,000 meters
- **Objective:** Minimize total cable length

## 📏 Approach
We need to connect all nodes with minimum cost and without cycles → MST.

We considered:
1.  **Prim's Algorithm** - Good for dense graph, O(V²) with adjacency matrix
2.  **Kruskal's Algorithm** - Good for sparse graph, O(E log E)

**Why Kruskal's?**
- Our campus graph is sparse (not all buildings
