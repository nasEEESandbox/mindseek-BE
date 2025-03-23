from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.models import Patient, Psychiatrist
from app.db.session import get_db

from app.schemas.appointment import AppointmentCreate, AppointmentResponse, AppointmentUpdate
from app.db.models.appointment import Appointment

router = APIRouter()

@router.get("/", response_model=list[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    appointments = db.query(Appointment).all()
    return appointments

@router.post("/", response_model=AppointmentResponse)
def create_appointment(appointment_data: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = Appointment(
        datetime=appointment_data.datetime,
        status=appointment_data.status,
        purpose_of_visit=appointment_data.purpose_of_visit,
        planned_assessment=appointment_data.planned_assessment,
        session_summary=appointment_data.session_summary,
        patient_id=appointment_data.patient_id,
        psychiatrist_id=appointment_data.psychiatrist_id
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    Patient.appointments.append(new_appointment)
    Psychiatrist.appointments.append(new_appointment)

    return new_appointment

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.put("/", response_model=AppointmentResponse)
def update_appointment(appointment_data: AppointmentUpdate, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_data.appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    if appointment_data.datetime:
        appointment.datetime = appointment_data.datetime

    if appointment_data.status:
        appointment.status = appointment_data.status

    if appointment_data.purpose_of_visit:
        appointment.purpose_of_visit = appointment_data.purpose_of_visit

    if appointment_data.planned_assessment:
        appointment.planned_assessment = appointment_data.planned_assessment

    if appointment_data.session_summary:
        appointment.session_summary = appointment_data.session_summary

    if appointment_data.patient_id:
        appointment.patient_id = appointment_data.patient_id

    if appointment_data.psychiatrist_id:
        appointment.psychiatrist_id = appointment_data.psychiatrist_id

    db.commit()
    db.refresh(appointment)

    return appointment

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(appointment)
    db.commit()
    return {"message": "Appointment deleted successfully"}

