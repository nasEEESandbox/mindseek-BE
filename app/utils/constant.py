import enum
import random


class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"

class Weekday(enum.Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"

class Severity(enum.Enum):
    MILD = "Mild"
    MODERATE = "Moderate"
    SEVERE = "Severe"

class AppointmentStatus(enum.Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

def default_photo_url(name: str) -> str:
    return f"https://ui-avatars.com/api/?name={name}&background=random&rounded=true&bold=true"

def generate_nip() -> str:
    part1 = random.randint(100000, 999999)
    part2 = random.randint(1000, 9999)
    return f"{part1}-{part2}"