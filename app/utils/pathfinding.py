import heapq

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_neighbors (node, grid):
    directions = [(0,1),(1,0),(0,-1), (-1,0)]
    neighbors=[]
    for dx, dy in directions:
        nx = node[0] + dx
        ny = node[1] + dy  
        if (nx, ny) in grid and grid[nx, ny]==1:
            neighbors.append((nx, ny))
    return neighbors
def astar (grid, start,goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(list(current))
                current = came_from[current]

            path.append(list(start))
            path.reverse()
            return path

        for neighbor in get_neighbors(current, grid):
            temp_g = g_score[current] + 1

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    return []
