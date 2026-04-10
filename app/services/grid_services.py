from app.utils.pathfinding import astar

class GridService:
    @staticmethod
    def find_path(grid,start,end):
        return astar(grid, tuple(start), tuple(end))