from fastapi import FastAPI
from db import connect_db
from crud import get_today_report, add_report
from models import WorkoutReport

app = FastAPI(title="Daily Fitness Report API")

@app.on_event("startup")
async def startup_db():
    await connect_db()

@app.get("/report/today")
async def today_report():
    return await get_today_report()

@app.post("/report")
async def create_report(report: WorkoutReport):
    return await add_report(report)