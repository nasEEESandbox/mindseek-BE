from fastapi import FastAPI

from app.routes.user import router as user_router
from app.routes.auth import router as auth_router
from app.routes.patient import router as patient_router
from app.routes.psychiatrist import router as psychiatrist_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(patient_router, prefix="/patient", tags=["patient"])
app.include_router(psychiatrist_router, prefix="/psychiatrist", tags=["psychiatrist"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

