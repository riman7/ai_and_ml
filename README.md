# 🤖 AI and ML – Learning by Building

This repository is a practical journey into **Artificial Intelligence (AI)** and **Machine Learning (ML)** through beginner-friendly, project-based learning. We implement foundational concepts in code to develop a deeper understanding of how intelligent systems work.

---

## 📘 Concept: Search Algorithms

Search algorithms are at the heart of many AI systems, used for problem-solving and pathfinding. The first topic we explore is **uninformed search**, using:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**

These are implemented in a maze-solving scenario.

---

## 🌱 The Node Data Structure

In AI search problems, we represent each state in the problem space as a **Node**.

Each node keeps track of:
- `state`: The current location or configuration.
- `parent`: The node that generated this node.
- `action`: The move taken to reach this node from its parent.
- `path cost`: The cumulative cost from the start to this node (used in other algorithms like UCS or A*).

---

## 🔁 General Search Algorithm Steps

1. **Initialize** the frontier with the starting node.
2. Set the **explored set** as empty.
3. Repeat:
   - If the frontier is empty, **no solution exists**.
   - Remove a node from the frontier.
   - If the node contains the **goal**, return the solution path.
   - Add the node to the **explored set**.
   - **Expand** the node: generate its neighbors.
   - For each neighbor:
     - If it’s not in the frontier or explored set, **add it to the frontier**.

---

## 🧠 DFS vs BFS

| Algorithm | Data Structure | Behavior | Guarantees |
|----------|----------------|----------|------------|
| **DFS** (Depth-First Search) | Stack (LIFO) | Explores deeply before backtracking | May not find shortest path |
| **BFS** (Breadth-First Search) | Queue (FIFO) | Explores shallow nodes first | Always finds the shortest path (if one exists) |

### Summary:
- **Stack** = Last In, First Out → DFS
- **Queue** = First In, First Out → BFS

---

## 🧪 Maze Solver Implementation

This project demonstrates both DFS and BFS by solving a maze from a `.txt` file. You can select the search strategy using a simple argument.

### 🔧 How It Works

- The maze is loaded from a file with:
  - `A`: Start
  - `B`: Goal
  - `#`: Wall
  - ` `: Walkable space
- Uses `Node`, `StackFrontier`, and `QueueFrontier` classes.
- The solution path is printed using `*` symbols.

### ▶️ How to Run

```bash
python maze.py maze.txt
```

> Requires Python 3.

### 📁 Example maze.txt

```
########
#A #   #
# ### ##
#   #  #
### #B##
#      #
########
```

### ✅ Sample Output

```bash
DFS States Explored: 38
BFS States Explored: 14
```

Printed maze with solution path:

```
A***    
  *###  
  * # * 
### #*##
#   * B#
```

---

## 🎯 Learning Goals

By working through this project, you will:
- Understand node-based problem solving.
- Learn the inner workings of DFS and BFS.
- Grasp the importance of data structures in algorithm design.
- Build a solid foundation for more advanced AI topics like:
  - A* Search
  - Minimax (used in games)
  - Reinforcement Learning
  - Pathfinding in robotics

---

## 🧱 Folder Structure

```
.
├── maze(bfs_dfs).py          # Main program
├── maze1.txt         # Sample maze input
├── maze2.txt         # Sample maze input
├── README.md        # You're here!
```

---

## 🚀 Coming Up Next

- A* Search for smarter pathfinding
- Tic-Tac-Toe with Minimax
- Reinforcement Learning simulation
- ML classifiers: k-NN, SVM, Decision Trees

---

## 📜 License

MIT License — Free to use, learn, and build upon.
