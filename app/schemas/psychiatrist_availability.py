from pydantic import BaseModel
from datetime import time

from app.utils.constant import Weekday


class PsychiatristAvailabilityCreate(BaseModel):
    day_of_week: Weekday
    start_time: time
    end_time: time

    class Config:
        orm_mode = True

class PsychiatristAvailabilityResponse(BaseModel):
    id: int
    psychiatrist_id: int
    day_of_week: Weekday
    start_time: time
    end_time: time

    class Config:
        orm_mode = True

class PsychiatristAvailabilityUpdate(BaseModel):
    day_of_week: Weekday | None
    start_time: time | None
    end_time: time | None

    class Config:
        orm_mode = True