class Solution(object):
    def numIslands(self, grid):
        from collections import deque
        if not grid:
            return []

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        lands = 0

        def traverse(i, j):
            queue = deque([(i, j)])
            while queue:
                curr_i, curr_j = queue.popleft()
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))
                # Traverse neighbors.
                    for direction in directions:
                        next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                        if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1":
                            # Add in question-specific checks, where relevant.
                            queue.append((next_i, next_j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    traverse(i, j)
                    lands += 1
        return lands