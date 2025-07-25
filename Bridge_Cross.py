from collections import deque

# People and their crossing times
people_times = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}

# Initial state: everyone on left, umbrella on left, time = 0
initial_state = (frozenset(people_times.keys()), frozenset(), 'left', 0)

def get_next_states(state):
    left, right, umbrella, time = state
    next_states = []
    
    if umbrella == 'left':
        # Choose 2 or 1 people to cross to right
        left_list = list(left)
        for i in range(len(left_list)):
            for j in range(i, len(left_list)):
                p1 = left_list[i]
                p2 = left_list[j]
                new_left = set(left)
                new_left.remove(p1)
                if p1 != p2:
                    new_left.remove(p2)
                new_right = set(right)
                new_right.update([p1, p2])
                crossing_time = max(people_times[p1], people_times[p2])
                new_state = (frozenset(new_left), frozenset(new_right), 'right', time + crossing_time)
                next_states.append((new_state, [p1, p2], crossing_time))
    else:
        # One person returns to left with umbrella
        right_list = list(right)
        for p in right_list:
            new_left = set(left)
            new_left.add(p)
            new_right = set(right)
            new_right.remove(p)
            crossing_time = people_times[p]
            new_state = (frozenset(new_left), frozenset(new_right), 'left', time + crossing_time)
            next_states.append((new_state, [p], crossing_time))
    return next_states

def bfs():
    queue = deque()
    visited = set()
    queue.append((initial_state, []))  # (state, path)
    
    while queue:
        state, path = queue.popleft()
        left, right, umbrella, time = state
        
        if time > 60:
            continue
        
        if len(right) == 4:
            return path + [(state, None, 0)]
        
        if state in visited:
            continue
        visited.add(state)
        
        for next_state, moved, move_time in get_next_states(state):
            queue.append((next_state, path + [(state, moved, move_time)]))
    
    return None

# Run BFS
result = bfs()

# Display result
if result:
    print(" Solution Found:")
    for step in result:
        state, moved, move_time = step
        left, right, umbrella, time = state
        print(f"Time: {time} mins | Left: {sorted(left)} | Right: {sorted(right)} | Umbrella: {umbrella}", end="")
        if moved:
            print(f" | Moved: {moved} ({move_time} mins)")
        else:
            print()
else:
    print(" No solution within 60 minutes.")
