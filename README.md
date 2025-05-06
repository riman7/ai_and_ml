# AI and ML


## node
a data structure that keeps track of
- a state
- a parent (node that generated this node)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)

## steps
Start with a frontier that contains the initial state.
- Start with an empty explored set.
- Repeat:
- If the frontier is empty, then no solution.
- Remove a node from the frontier.
- If node contains goal state, return the solution.
- Add the node to the explored set.
- Expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set


stack = last in first out
queue = first in first out

if stack(last in first out), depth-frist search

if queue(first in first out), breadth-first search