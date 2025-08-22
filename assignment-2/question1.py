# Print outputs in assignment format
def print_example_outputs():
    examples = [
        ("Example 1", [[0,1],[1,0]]),
        ("Example 2", [[0,0,0],[1,1,0],[1,1,0]]),
        ("Example 3", [[1,0,0],[1,1,0],[1,1,0]]),
    ]

    for name, grid in examples:
        bfs_len, bfs_path = best_first_search(grid, heuristic_type="chebyshev")
        ast_len, ast_path = a_star_search(grid, heuristic_type="chebyshev")
        
        print(name)
        if bfs_len == -1:
            print("Best First Search  →  Path length: -1")
        else:
            print(f"Best First Search  →  Path length: {bfs_len}, Path: {[(x,y) for (x,y) in bfs_path]}")
        
        if ast_len == -1:
            print("A* Search          →  Path length: -1")
        else:
            print(f"A* Search          →  Path length: {ast_len}, Path: {[(x,y) for (x,y) in ast_path]}")
        
        print()

# Run and check
print_example_outputs()
