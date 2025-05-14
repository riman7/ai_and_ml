import sys
import heapq

import itertools


# expand to node with lowest g(n) + h(n)
# g(n) = cost to reach node
# h(n) = estimated cost to reach goal

class Node():
    def __init__(self, state, parent, action, g, h):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h
        self.f = g + h

class PriorityQueueFrontier:
    def __init__(self):
        self.frontier = []
        self.counter = itertools.count()  # tie-breaker
    
    def add(self, node):
        count = next(self.counter)
        heapq.heappush(self.frontier, (node.f, count, node))
    
    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)

    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        
        return heapq.heappop(self.frontier)[2]
    
class Maze():
    def __init__(self, filename):
        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines() # "###\n# #\n###" => ['###', '# #', '###']
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
    
    def heuristic(self, a, b):
        return abs(self.goal[0] - a) + abs(self.goal[1] - b)

    def solve(self):
        self.num_explored = 0
        self.explored = set()

        start = Node(state= self.start, parent=None, action= None, g = 0, h = self.heuristic(self.start[0], self.start[1]))

        frontier = PriorityQueueFrontier()
        frontier.add(start)

        while(True):
            if frontier.empty():
                raise Exception("No solution")
            
            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                cells = []
                actions = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action, g = node.g + 1, h = self.heuristic(self.start[0], self.start[1]))
                    frontier.add(child)
            

    
    
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
m.print()
m.solve()
print("States Explored:", m.num_explored)
m.print()