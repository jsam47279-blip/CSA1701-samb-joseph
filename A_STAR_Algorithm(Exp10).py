import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):

    open_list = [(0, start)]

    came_from = {start: None}
    g = {start: 0}

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:

            path = []

            while current:
                path.append(current)
                current = came_from[current]

            return path[::-1]

        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:

            neighbour = (
                current[0] + dx,
                current[1] + dy
            )

            if (
                0 <= neighbour[0] < len(grid)
                and
                0 <= neighbour[1] < len(grid[0])
                and
                grid[neighbour[0]][neighbour[1]] == 0
            ):

                new_cost = g[current] + 1

                if neighbour not in g or new_cost < g[neighbour]:

                    g[neighbour] = new_cost

                    priority = new_cost + heuristic(
                        neighbour,
                        goal
                    )

                    heapq.heappush(
                        open_list,
                        (priority, neighbour)
                    )

                    came_from[neighbour] = current

    return None

grid = [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0]
]

path = astar(grid, (0,0), (4,4))

print("Path:", path)
