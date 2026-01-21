from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Habit Tracker API')

class HabitCreate(BaseModel):
    name: str
    frequency: str

habits:HabitCreate = []

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/habits")
def create_habits(habit: HabitCreate):
    habits.append(habit)
    return {
        "message": "Habit created successfully",
        "habit": habit
    }
    

@app.get("/habits")
def list_habits() -> list[HabitCreate]:
    return habits
