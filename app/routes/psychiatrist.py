from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.db.models.psychiatrist import Psychiatrist
from app.db.models.psychiatrist_availability import PsychiatristAvailability
from app.db.session import get_db
from app.schemas.psychiatrist import PsychiatristUpdate, PsychiatristCreate, PsychiatristResponse
from app.schemas.psychiatrist_availability import PsychiatristAvailabilityUpdate, PsychiatristAvailabilityResponse, PsychiatristAvailabilityCreate

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

from app.db.models.psychiatrist_availability import PsychiatristAvailability

@router.post("/", response_model=PsychiatristResponse)
def create_psychiatrist(psychiatrist: PsychiatristCreate, db: Session = Depends(get_db)):
    print("psy", psychiatrist)
    print("psy gen", psychiatrist.gender.value)
    print(type(psychiatrist.gender.value))
    print("psy pass", psychiatrist.password)

    new_psychiatrist = Psychiatrist(
        **psychiatrist.model_dump(exclude={"availability", "gender", "password"}, exclude_unset=True),
        gender=psychiatrist.gender.value if psychiatrist.gender else None,
        hashed_password=get_password_hash(psychiatrist.password)
    )
    db.add(new_psychiatrist)
    db.commit()
    db.refresh(new_psychiatrist)

    availability_data = psychiatrist.availability or []
    for availability in availability_data:
        availability_instance = PsychiatristAvailability(
            psychiatrist_id=new_psychiatrist.id,
            **availability.model_dump(exclude_unset=True)
        )
        db.add(availability_instance)

    db.commit()
    db.refresh(new_psychiatrist)

    return new_psychiatrist


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
        psychiatrist_data.model_dump(exclude_unset=True, exclude={"email", "nip"})
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

@router.get("/{psychiatrist_id}/availability", response_model=PsychiatristAvailabilityResponse)
def read_psychiatrist_availability(psychiatrist_id: int, db: Session = Depends(get_db)):
    psychiatrist = db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).first()
    if psychiatrist is None:
        raise HTTPException(status_code=404, detail="Psychiatrist not found")
    return psychiatrist.availability

@router.put("/{psychiatrist_id}/availability", response_model=PsychiatristResponse)
def update_psychiatrist_availability(
    psychiatrist_id: int,
    availability_data: PsychiatristAvailabilityUpdate,
    db: Session = Depends(get_db)
):
    # ✅ Ensure the psychiatrist exists
    psychiatrist = db.query(Psychiatrist).filter(Psychiatrist.id == psychiatrist_id).first()
    if not psychiatrist:
        raise HTTPException(status_code=404, detail="Psychiatrist not found")

    # ✅ Find and update the psychiatrist's availability
    availability = db.query(PsychiatristAvailability).filter(
        PsychiatristAvailability.psychiatrist_id == psychiatrist_id
    ).first()

    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found")

    for field, value in availability_data.model_dump(exclude_unset=True).items():
        setattr(availability, field, value)

    db.commit()
    db.refresh(psychiatrist)
    return psychiatrist