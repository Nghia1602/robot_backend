from fastapi import FastAPI
import socketio

from app.socket.socket_manager import socket
from app.api.v1.endpoints.grid import router as grid_router
from app.api.v1.endpoints.move import router as move_router
from app.services.robot_engine import start_robot_engine

app = FastAPI()

app.include_router(grid_router, prefix="/api/v1", tags=["grid"])
app.include_router(move_router, prefix="/api/v1", tags=["robot"])


@app.get("/")
def read_root():
    return {"message": "Đã chạy server thành công!"}


@app.on_event("startup")
def startup_event():
    start_robot_engine()


socket_app = socketio.ASGIApp(socket, other_asgi_app=app)
