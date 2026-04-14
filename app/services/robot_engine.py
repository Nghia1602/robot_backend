import asyncio

from app.services.task_services import TaskService
from app.services.robot_services import RobotService


async def robot_task_loop():
    while True:
        task = TaskService.get_tasks()
        if task:
            robot = task["robot_id"]
            path = task["path"]
            RobotService.update_robot_status(robot, "running")
            for step in path:
                RobotService.update_robot_position(robot, step[0], step[1])
                print(f"Robot {robot} moved to {step}")
                await asyncio.sleep(0.5)
            RobotService.update_robot_status(robot, "idle")
        await asyncio.sleep(0.5)


def start_robot_engine():
    asyncio.create_task(robot_task_loop())
