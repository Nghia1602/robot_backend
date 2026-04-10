from fastapi import APIRouter
from app.services.grid_services import GridService
from app.models.grid import PathRequest, PathResponse

router = APIRouter()
@router.post("/find-path", response_model = PathResponse)
def find_path(req:PathRequest):
    path = GridService.find_path(req.grid, req.start, req.goal)
    return {"path": path}