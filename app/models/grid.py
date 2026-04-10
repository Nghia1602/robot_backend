from pydantic import BaseModel
from typing import List

class PathRequest(BaseModel):
    grid:List[List[int]]
    start:List[int]
    goal:List[int]
    
class PathResponse(BaseModel):
    path:List[List[int]]
