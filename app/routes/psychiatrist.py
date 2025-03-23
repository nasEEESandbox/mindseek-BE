from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.models.psychiatrist import Psychiatrist
from app.db.session import get_db
from app.schemas.psychiatrist import PsychiatristUpdate, PsychiatristCreate, PsychiatristResponse
from app.schemas.psychiatrist_availability import PsychiatristAvailabilityUpdate

router = APIRouter()

@router.get("/", response_model=List[PsychiatristResponse])
def read_psychiatrists(db: Session = Depends(get_db)):
    psychiatrists = db.query(Psychiatrist).all()
    return psychiatrists

@router.get("/{psychiatrist_id}", response_model=PsychiatristResponse)
def read_psychiatrist(psychiatrist_id: int, db: Session = Depends(get_db)):
    psychiatrist = db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).first()
    if psychiatrist is None:
        raise HTTPException(status_code=404, detail="Psychiatrist not found")
    return psychiatrist

@router.post("/", response_model=PsychiatristResponse)
def create_psychiatrist(psychiatrist: PsychiatristCreate, db: Session = Depends(get_db)):
    psychiatrist = Psychiatrist(**psychiatrist.dict())
    db.add(psychiatrist)
    db.commit()
    db.refresh(psychiatrist)
    return psychiatrist

@router.put("/{psychiatrist_id}", response_model=PsychiatristResponse)
def update_psychiatrist(psychiatrist_id: int, psychiatrist_data: PsychiatristUpdate, db: Session = Depends(get_db)):
    psychiatrist = db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).first()
    if not psychiatrist:
        raise HTTPException(status_code=404, detail="Psychiatrist not found")

    if psychiatrist_data.email:
        psychiatrist.user.email = psychiatrist_data.email

    if psychiatrist_data.nip:
        psychiatrist.user.nip = psychiatrist_data.nip


    db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).update(
        psychiatrist_data.dict(exclude_unset=True, exclude={"email", "nip"})
    )

    db.commit()
    db.refresh(psychiatrist)

    return psychiatrist

@router.delete("/{psychiatrist_id}")
def delete_psychiatrist(psychiatrist_id: int, db: Session = Depends(get_db)):
    psychiatrist = db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).first()
    if not psychiatrist:
        raise HTTPException(status_code=404, detail="Psychiatrist not found")
    db.delete(psychiatrist)
    db.commit()
    return {"message": "Psychiatrist deleted successfully"}

@router.put("/{psychiatrist_id}/availability", response_model=PsychiatristResponse)
def update_psychiatrist_availability(psychiatrist_id: int, psychiatrist_data: PsychiatristUpdate, db: Session = Depends(get_db)):
    psychiatrist = db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).first()
    if not psychiatrist:
        raise HTTPException(status_code=404, detail="Psychiatrist not found")

    if psychiatrist_data.availability:
        psychiatrist.availability = psychiatrist_data.availability

    db.commit()
    db.refresh(psychiatrist)

    return psychiatrist




