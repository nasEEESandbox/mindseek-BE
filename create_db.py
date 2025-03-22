from app.db.session import engine, Base
from app.db.models.user import User
from app.db.models.patient import Patient
from app.db.models.psychiatrist import Psychiatrist, PsychiatristAvailability
from app.db.models.appointment import Appointment
from app.db.models.medication import Medication
from app.db.models.medicine import Medicine
from app.db.models.diagnosis import Diagnosis

# Create tables in the database
Base.metadata.create_all(bind=engine)

print("Database and tables created successfully!")
