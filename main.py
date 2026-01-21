from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Habit Tracker API')

class HabitCreate(BaseModel):
    name: str
    frequency: str

class HabitOut(HabitCreate):
    id: int
    
habits:HabitOut = []

def create_id() -> int:
    global ID
    
    id = ID
    id += 1
    ID = id
    return id
ID = 0

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/habits")
def create_habits(habit: HabitCreate) -> dict:
    id = create_id()
    habit_dict = habit.model_dump()
    intern_habit = HabitOut(id= id, **habit_dict)
    habits.append(intern_habit)

    return {
        "message": "Habit created successfully",
        "habit": intern_habit
    }


@app.get("/habits")
def list_habits() -> list[HabitOut]:
    return habits
