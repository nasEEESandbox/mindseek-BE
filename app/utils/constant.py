import enum


class UserRole(enum.Enum):
    PSYCHIATRIST = "Psychiatrist"
    ADMIN = "Admin"

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