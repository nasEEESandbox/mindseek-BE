from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.diagnosis import DiagnosisCreate, DiagnosisResponse, DiagnosisUpdate
from app.db.models.diagnosis import Diagnosis

router = APIRouter()

@router.get("/", response_model=list[DiagnosisResponse])
def get_diagnoses(db: Session = Depends(get_db)):
    diagnoses = db.query(Diagnosis).all()
    return diagnoses

@router.get("/{diagnosis_id}", response_model=DiagnosisResponse)
def get_diagnosis(diagnosis_id: int, db: Session = Depends(get_db)):
    diagnosis = db.query(Diagnosis).filter(Diagnosis.id == diagnosis_id).first()
    if not diagnosis:
        raise HTTPException(status_code=404, detail="Diagnosis not found")
    return diagnosis

@router.post("/", response_model=DiagnosisResponse)
def create_diagnosis(diagnosis_data: DiagnosisCreate, db: Session = Depends(get_db)):
    new_diagnosis = Diagnosis(
        diagnosis_name=diagnosis_data.diagnosis_name,
        appointment_id=diagnosis_data.appointment_id,
        patient_id=diagnosis_data.patient_id,
        diagnosed_date=diagnosis_data.diagnosed_date,
        status=diagnosis_data.status,
        severity=diagnosis_data.severity
    )
    db.add(new_diagnosis)
    db.commit()
    db.refresh(new_diagnosis)

    return new_diagnosis

@router.put("/{diagnosis_id}", response_model=DiagnosisResponse)
def update_diagnosis(diagnosis_id: int, diagnosis_data: DiagnosisUpdate, db: Session = Depends(get_db)):
    diagnosis = db.query(Diagnosis).filter(Diagnosis.id == diagnosis_id).first()
    if not diagnosis:
        raise HTTPException(status_code=404, detail="Diagnosis not found")
    if diagnosis_data.diagnosis_name:
        diagnosis.diagnosis_name = diagnosis_data.diagnosis_name
    if diagnosis_data.appointment_id:
        diagnosis.appointment_id = diagnosis_data.appointment_id
    if diagnosis_data.patient_id:
        diagnosis.patient_id = diagnosis_data.patient_id
    if diagnosis_data.diagnosed_date:
        diagnosis.diagnosed_date = diagnosis_data.diagnosed_date
    if diagnosis_data.status:
        diagnosis.status = diagnosis_data.status
    if diagnosis_data.severity:
        diagnosis.severity = diagnosis_data.severity
    db.commit()
    db.refresh(diagnosis)
    return diagnosis

@router.delete("/{diagnosis_id}")
def delete_diagnosis(diagnosis_id: int, db: Session = Depends(get_db)):
    diagnosis = db.query(Diagnosis).filter(Diagnosis.id == diagnosis_id).first()
    if not diagnosis:
        raise HTTPException(status_code=404, detail="Diagnosis not found")
    db.delete(diagnosis)
    db.commit()
    return {"message": "Diagnosis deleted successfully"}
