from collections import deque

# Initial and Goal States
initial_state = ['W', 'W', 'W', '_', 'E', 'E', 'E']
goal_state = ['E', 'E', 'E', '_', 'W', 'W', 'W']

def get_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i] == 'W':
            # Move right
            if i+1 < len(state) and state[i+1] == '_':
                new_state = state.copy()
                new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
                next_states.append(new_state)
            # Jump over one to right
            if i+2 < len(state) and state[i+1] in ['E', 'W'] and state[i+2] == '_':
                new_state = state.copy()
                new_state[i], new_state[i+2] = new_state[i+2], new_state[i]
                next_states.append(new_state)

        elif state[i] == 'E':
            # Move left
            if i-1 >= 0 and state[i-1] == '_':
                new_state = state.copy()
                new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
                next_states.append(new_state)
            # Jump over one to left
            if i-2 >= 0 and state[i-1] in ['W', 'E'] and state[i-2] == '_':
                new_state = state.copy()
                new_state[i], new_state[i-2] = new_state[i-2], new_state[i]
                next_states.append(new_state)
    return next_states

def bfs(start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(tuple(current))
        for next_state in get_next_states(current):
            if tuple(next_state) not in visited:
                queue.append((next_state, path + [next_state]))
    return None

def dfs(start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        visited.add(tuple(current))
        for next_state in get_next_states(current):
            if tuple(next_state) not in visited:
                stack.append((next_state, path + [next_state]))
    return None

# Run BFS and DFS
bfs_result = bfs(initial_state, goal_state)
dfs_result = dfs(initial_state, goal_state)

# Output
if bfs_result:
    print("BFS Solution Path:")
    for state in bfs_result:
        print(state)
else:
    print("No BFS solution found.")

if dfs_result:
    print("\nDFS Solution Path:")
    for state in dfs_result:
        print(state)
else:
    print("No DFS solution found.")
