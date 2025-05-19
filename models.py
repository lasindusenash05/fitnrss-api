from pydantic import BaseModel
from datetime import date

class WorkoutReport(BaseModel):
    date: date
    message: str