from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.medicine import MedicineUpdate, MedicineCreate, MedicineResponse
from app.db.models.medicine import Medicine

router = APIRouter()

@router.get("/", response_model=list[MedicineResponse])
def get_medicines(db: Session = Depends(get_db)):
    medicines = db.query(Medicine).all()
    return medicines

@router.get("/{medicine_id}", response_model=MedicineResponse)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine

@router.post("/", response_model=MedicineResponse)
def create_medicine(medicine_data: MedicineCreate, db: Session = Depends(get_db)):
    new_medicine = Medicine(medicine_name=medicine_data.medicine_name)
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)
    return new_medicine

@router.put("/{medicine_id}", response_model=MedicineResponse)
def update_medicine(medicine_id: int, medicine_data: MedicineUpdate, db: Session = Depends(get_db)):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    if medicine_data.medicine_name:
        medicine.medicine_name = medicine_data.medicine_name
    db.commit()
    db.refresh(medicine)
    return medicine

@router.delete("/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    db.delete(medicine)
    db.commit()
    return {"message": "Medicine deleted successfully"}