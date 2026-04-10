import time
import asyncio
from threading import Lock


class RobotService:
    _robot: dict[int, dict] = {}
    _lock = Lock()
    VALUE_STATUS = {"idle", "running", "error"}

    @classmethod
    def create_robot(cls, robot_id: int, x: int = None, y: int = None):
        with cls._lock:
            if robot_id in cls._robot:
                raise ValueError(f"Robot with id {robot_id} already exists")
            if robot_id < 0:
                raise ValueError("Robot id must be non_negative")
            if x is None or y is None or robot_id is None:
                raise ValueError("x, y, and robot_id must be provided")
            cls._robot[robot_id] = {"x": x, "y": y, "status": "idle"}

    @classmethod
    def get_all_robot(cls):
        with cls._lock:
            return list(cls._robot.values())

    @classmethod
    def update_robot(cls, robot_id: int, x: int, y: int, status: str):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("x and y must be integers")
        if status not in cls.VALUE_STATUS:
            raise ValueError(
                f"Invalid status: {status}. Valid statuses are: {cls.VALUE_STATUS}"
            )
        with cls._lock:
            if robot_id not in cls._robot:
                raise ValueError(f"Robot with id {robot_id} does not exist")

            cls._robot[robot_id].update({"x": x, "y": y, "status": status})
    @classmethod
    def delete_robot(cls, robot_id:int):
        with cls._lock:
            if robot_id not in cls._robot:
                raise ValueError(f"Robot with id {robot_id} does not exist")
            del cls._robot[robot_id]
    @classmethod
    def get_idle_robots(cls):
        with cls._lock:
             for robot in cls._robot.values(): 
                 if robot["status"]=="idle":
                     return robot
        return None