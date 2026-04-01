from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Đã chạy server thành công!"}


@app.get("/grid")
def get_grid():
    return {"size": 20}