from fastapi import FastAPI

from app.core.config import setup_cors
from app.routes.auth import router as auth_router
from app.routes.patient import router as patient_router
from app.routes.psychiatrist import router as psychiatrist_router

app = FastAPI()

setup_cors(app)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(patient_router, prefix="/patient", tags=["Patient"])
app.include_router(psychiatrist_router, prefix="/psychiatrist", tags=["Psychiatrist"])