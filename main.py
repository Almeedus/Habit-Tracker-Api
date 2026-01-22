from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title='Habit Tracker API')

class HabitCreate(BaseModel):
    name: str
    frequency: str

class HabitOut(HabitCreate):
    id: int
    
habits:HabitOut = []

@app.get("/health")
def health_check():
    return {"status": "ok"}


def create_id() -> int:
    global ID
    
    id = ID
    id += 1
    ID = id
    return id
ID = 0

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


def search_habit(id: int) -> HabitOut:
    for habit in habits:
        if habit.id == id:
            return habit
        
    raise HTTPException(status_code=404, detail="Habit not found")

@app.get("/habits/{id}")
def return_habit(id: int) -> HabitOut:
    return search_habit(id)

@app.delete("/habits/{id}", status_code=204)
def delete_habit(id: int) -> None:
    habits.remove(search_habit(id))
