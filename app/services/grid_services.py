from app.utils.pathfinding import astar

class GridService:
    @staticmethod
    def find_path(grid,start,end):
        print(f"Finding path from {start} to {end} on grid:")
        return astar(grid, tuple(start), tuple(end))