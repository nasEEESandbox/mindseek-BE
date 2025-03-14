from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routes.user import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

