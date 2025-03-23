from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.medication import MedicationUpdate, MedicationCreate, MedicationResponse
from app.db.models.medication import Medication

router = APIRouter()

@router.get("/", response_model=list[MedicationResponse])
def get_medications(db: Session = Depends(get_db)):
    medications = db.query(Medication).all()
    return medications

@router.get("/{medication_id}", response_model=MedicationResponse)
def get_medication(medication_id: int, db: Session = Depends(get_db)):
    medication = db.query(Medication).filter(Medication.id == medication_id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    return medication

@router.post("/", response_model=MedicationResponse)
def create_medication(medication_data: MedicationCreate, db: Session = Depends(get_db)):
    new_medication = Medication(
        medicine_id=medication_data.medicine_id,
        dosage=medication_data.dosage,
        start_date=medication_data.start_date,
        end_date=medication_data.end_date,
        notes=medication_data.notes,
        patient_id=medication_data.patient_id
    )
    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)

    return new_medication

@router.put("/{medication_id}", response_model=MedicationResponse)
def update_medication(medication_id: int, medication_data: MedicationUpdate, db: Session = Depends(get_db)):
    medication = db.query(Medication).filter(Medication.id == medication_id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    if medication_data.medicine_id:
        medication.medicine_id = medication_data.medicine_id
    if medication_data.dosage:
        medication.dosage = medication_data.dosage
    if medication_data.start_date:
        medication.start_date = medication_data.start_date
    if medication_data.end_date:
        medication.end_date = medication_data.end_date
    if medication_data.notes:
        medication.notes = medication_data.notes
    db.commit()
    db.refresh(medication)
    return medication

@router.delete("/{medication_id}")
def delete_medication(medication_id: int, db: Session = Depends(get_db)):
    medication = db.query(Medication).filter(Medication.id == medication_id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(medication)
    db.commit()
    return {"message": "Medication deleted successfully"}
