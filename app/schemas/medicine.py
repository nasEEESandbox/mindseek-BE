from pydantic import BaseModel

class MedicineResponse(BaseModel):
    id: int | None
    medicine_name: str | None

class MedicineCreate(BaseModel):
    medicine_name: str

class MedicineUpdate(BaseModel):
    medicine_id: int | None
    medicine_name: str | None