from fastapi import FastAPI

from app.core.config import setup_cors
from app.routes.auth import router as auth_router
from app.routes.patient import router as patient_router
from app.routes.psychiatrist import router as psychiatrist_router
from app.routes.medicine import router as medicine_router
from app.routes.medication import router as medication_router
from app.routes.appointment import router as appointment_router
from app.routes.diagnosis import router as diagnosis_router

app = FastAPI()

setup_cors(app)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(patient_router, prefix="/patient", tags=["Patient"])
app.include_router(psychiatrist_router, prefix="/psychiatrist", tags=["Psychiatrist"])
app.include_router(medicine_router, prefix="/medicine", tags=["Medicine"])
app.include_router(medication_router, prefix="/medication", tags=["Medication"])
app.include_router(appointment_router, prefix="/appointment", tags=["Appointment"])
app.include_router(diagnosis_router, prefix="/diagnosis", tags=["Diagnosis"])
