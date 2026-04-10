from fastapi import FastAPI
from app.api.v1.endpoints.grid import router

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["grid"])

@app.get("/")
def read_root():
    return {"message": "Đã chạy server thành công!"}