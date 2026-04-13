from fastapi import APIRouter, HTTPException
from app.services.robot_services import RobotService
from app.services.grid_services import GridService
from app.services.task_services import TaskService


router = APIRouter()


@router.post("/move")
def move(req: dict):
    robot_id = req["robot_id"]
    goal = tuple(req["goal"])
    grid = req["grid"]
    robot = RobotService.get_robot(robot_id)
    start = (robot["x"], robot["y"])

    path = GridService.find_path(grid, start, goal)
    if not path:
        raise HTTPException(
            status_code=400,
            detail=f"No path found for robot {robot_id} from {start} to {goal}",
        )

    TaskService.add_task({"robot_id": robot_id, "path": path})
    return {"message": f"Move task added for robot {robot_id}", "path": path}
