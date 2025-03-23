from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.models import Psychiatrist
from app.db.session import get_db
from app.schemas.patient import PatientResponse, PatientCreate, PatientUpdate
from app.db.models.patient import Patient
from app.utils.constant import generate_nip

router = APIRouter()

@router.get("/", response_model=List[PatientResponse])
def read_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients

@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    display_id = generate_nip()
    while db.query(Patient).filter(Patient.display_id == display_id).first():
        display_id = generate_nip()

    psychiatrist = db.query(Psychiatrist).order_by(func.random()).first()
    if not psychiatrist:
        raise HTTPException(status_code=400, detail="No psychiatrists available")

    db_patient = Patient(
        **patient.model_dump(exclude={"display_id", "psychiatrist_id"}, exclude_unset=True),
        display_id=display_id,
        psychiatrist_id = int(psychiatrist.id)
    )

    psychiatrist.patients.append(db_patient)

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient

@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    for key, value in patient.dict().items():
        setattr(db_patient, key, value)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(db_patient)
    db.commit()
    return {"message": "Patient deleted successfully"}

