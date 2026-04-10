from pydamics import BaseModel

class RobotState(BaseModel):
    x: int
    y: int
    status:str