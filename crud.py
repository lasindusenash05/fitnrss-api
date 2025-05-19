from db import db
from datetime import date
from models import WorkoutReport

async def get_today_report():
    today = date.today().isoformat()
    result = await db.reports.find_one({"date": today})
    if result:
        result.pop("_id", None)
        return result
    return {"message": "No report for today."}

async def add_report(report: WorkoutReport):
    await db.reports.insert_one(report.dict())
    return {"status": "Report added"}